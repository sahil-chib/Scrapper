# Web Scraping Service with FastAPI

This project is a web scraping service that scrapes data from the [Hacker News](https://news.ycombinator.com) website. It scrapes the latest 30 posts with details like points, author, and posted time, along with the latest 5 comments per post. The scraped data is stored in a MySQL database, and the service provides an API to retrieve the data in JSON format.

## Features

- Scrape the latest 30 posts from Hacker News.
- Retrieve post details such as title, link, points, author, and posted time.
- Fetch the latest 5 comments per post.
- Store the scraped data in a MySQL database using SQLAlchemy.
- API endpoints to trigger the scraping process and retrieve the scraped data.

## Requirements

- Python 3.7+
- MySQL
- FastAPI
- SQLAlchemy
- BeautifulSoup
- requests
- dateparser
- Uvicorn

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   
Create a virtual environment and activate it:
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

Install the dependencies:
pip install -r requirements.txt

Update the database connection string in app/database.py:
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/dbname"
Ensure the database specified in the connection string exists. You can create it using a MySQL client:
CREATE DATABASE dbname;


## Usage
Start the FastAPI server:
uvicorn app.main:app --reload
Trigger the scraping process by making a POST request to the /scrape endpoint. You can use tools like curl, Postman, or Python's requests library.

Using curl:
curl -X POST http://127.0.0.1:8000/scrape

Using Python requests:
import requests
response = requests.post("http://127.0.0.1:8000/scrape")
print(response.json())


Retrieve the scraped data by making a GET request to the /data endpoint:
curl http://127.0.0.1:8000/data

Check the status of the scraping service by making a GET request to the /status endpoint:
curl http://127.0.0.1:8000/status

## API Endpoints
POST /scrape: Triggers the scraping process.
GET /data: Returns the scraped data from the database in JSON format.
GET /status: Returns the status of the latest scraping process (e.g., completed, in progress, failed).

## Error Handling
The service implements appropriate error handling to manage scenarios such as scraping failures and database errors. In case of an error, an appropriate HTTP status code and error message will be returned.
