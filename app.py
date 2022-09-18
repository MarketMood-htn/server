# Server that will automatically update news every 10 minutes for all listed stocks
import time
import atexit
from flask import Flask
from WebScraper import connectToAndParseGoogleNews
from WebScraper import getNewsLinksFromGoogleNews
from WebScraper import getArticleText
from NewsArticle import NewsArticle
from SentimentalAnalysis import analyzeSentiment
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

stocks = ['aapl', 'nnox','tsla','amzn','fb','msft', 'goog', 'intc', 'nvda','uber']

def runScan():
    text = {}
    # Get News Articles
    for stock in stocks:
        stockInfo = {'ticker':stock}
        articles = getNewsLinksFromGoogleNews(
            connectToAndParseGoogleNews(stock))
        articleInfo = []
        for article in articles:
            text[article] = getArticleText(article)
            sentiment = analyzeSentiment(text[article],article)
            articleInfo.append(sentiment)
            # print(sentiment)
            # Create Object
            # TO DO Store in database
        stockInfo['news'] = articleInfo
        print(stockInfo)
runScan()
scheduler = BackgroundScheduler()
scheduler.add_job(func=runScan, trigger="interval", seconds=900)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


