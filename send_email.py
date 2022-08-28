import json
import requests
import datetime
import os
import yagmail

# Weather API
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
WEATHER_API_URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Jamshedpur?unitGroup=metric&include=days&key={WEATHER_API_KEY}&contentType=json"
weather_req = requests.get(WEATHER_API_URL)
WEATHER = weather_req.json()

# Jokes API
JOKES_API_URL = "https://v2.jokeapi.dev/joke/Any?type=single"
joke_req = requests.get(JOKES_API_URL)
JOKE = joke_req.json()

# NEWS API
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_URL = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
news_req = requests.get(NEWS_API_URL)

NEWS_LIST = news_req.json().get("articles")
TOP_ARTICLES = None
article = NEWS_LIST[0]
article_post = {
    "title": article.get('title'),
    "description": article.get('description'),
    "url": article.get('url'),
}
TOP_ARTICLES = article_post

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
RECEIVER = "adityapriyadarshi669@gmail.com"

MESSAGE = f"""
Hello this is a simple corn job coming from github.
Today's date: {datetime.date.today()}
Today average {WEATHER.get("days")[0].get("temp")}°C with Min {WEATHER.get("days")[0].get("tempmin")}°C and Max {WEATHER.get("days")[0].get("tempmax")}°C
Weather description: {WEATHER.get("days")[0].get("description")}

Today's Joke: {JOKE.get('joke')}

Today News
Title:{TOP_ARTICLES.get("title")}
Description: {TOP_ARTICLES.get("description")}
URL: {TOP_ARTICLES.get("url")}

"""
yag = yagmail.SMTP(EMAIL, PASSWORD)

yag.send(RECEIVER, "Today Corn Job Status", MESSAGE)