import requests
import dateparser
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from .models import Post, Comment


def convert_to_timestamp(time_str):
    parsed_time = dateparser.parse(time_str)
    if parsed_time:
        return parsed_time.strftime('%Y-%m-%d %H:%M:%S')
    return None

def scrape_ycombinator(session: Session):
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    posts = soup.find_all('tr', class_='athing', limit=30)
    
    for post in posts:
        title_tag = post.find('span', class_='titleline')
        title = title_tag.get_text(strip=True) if title_tag else None
        link = title_tag.find('a')['href'] if title_tag else None
        
        points_tag = post.find_next_sibling('tr').find('span', class_='score')
        points = int(points_tag.get_text(strip=True).split()[0]) if points_tag else None
        
        author_tag = post.find_next_sibling('tr').find('a', class_='hnuser')
        author = author_tag.get_text(strip=True) if author_tag else None
        
        time_tag = post.find_next_sibling('tr').find('span', class_='age')
        time = time_tag.get_text(strip=True) if time_tag else None
        time = convert_to_timestamp(time_tag.get_text(strip=True)) if time_tag else None
        
        # Save the post
        db_post = Post(title=title, link=link, points=points, author=author, time=time)
        session.add(db_post)
        session.commit()
        
        # Fetch comments for the post
        comments = fetch_latest_comments(link)
        for comment_text in comments:
            db_comment = Comment(text=comment_text, post_id=db_post.id)
            session.add(db_comment)
        
        session.commit()

def fetch_latest_comments(comment_link):
    url = f'https://news.ycombinator.com/{comment_link}'
    response = requests.get(url)
    comment_soup = BeautifulSoup(response.text, 'html.parser')

    # Find the latest five comments
    comments = comment_soup.find_all('tr', class_='athing comtr', limit=5)
    
    # Extract the latest five comments, handling potential None values
    latest_comments = []
    for comment in comments:
        comment_text = comment.find('div', class_='commtext')
        if comment_text:
            latest_comments.append(comment_text.get_text(strip=True))
    
    return latest_comments