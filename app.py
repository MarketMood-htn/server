# Server that will automatically update news every 10 minutes for all listed stocks
import time
import atexit
from flask import Flask
from WebScraper import connectToAndParseGoogleNews
from WebScraper import getNewsLinksFromGoogleNews
from WebScraper import getArticleText
from NewsArticle import NewsArticle
from SentimentalAnalysis import analyzeSentiment
from dbservice import postArticles
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

stocks = ['aapl' ,'tsla','amzn','fb','msft', 'amd', 'ibm', 'intc', 'nvda','uber']

def runScan():
    text = {}
    # Get News Articles
    for stock in stocks:
        stockInfo = {'ticker':stock, 'name': stock}
        articles = getNewsLinksFromGoogleNews(
            connectToAndParseGoogleNews(stock))
        articleInfo = []
        print("stock: " + stock)
        c = 0
        for article in articles:
            print("article: " + str(c))
            c=c+1
            text[article] = getArticleText(article)
            sentiment = analyzeSentiment(text[article],article)
            if(sentiment is not None):
                articleInfo.append(sentiment)
        stockInfo['all_articles'] = articleInfo
        postArticles(stockInfo,stock,articleInfo)
runScan()
scheduler = BackgroundScheduler()
scheduler.add_job(func=runScan, trigger="interval", seconds=900)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())