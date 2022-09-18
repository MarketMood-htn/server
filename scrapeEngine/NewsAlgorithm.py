# Script that will automatically update news every 10 minutes for all listed stocks
import time
import atexit
from WebScraper import connectToAndParseGoogleNews
from WebScraper import getNewsLinksFromGoogleNews
from WebScraper import getArticleText
from NewsArticle import NewsArticle
# import sys
# sys.path.insert(0, './SentimentAnalysis/SentimentalAnalysis')
# import SentimentalAnalysis
from SentimentalAnalysis import analyzeSentiment


# from apscheduler.schedulers.background import BackgroundScheduler


# def print_date_time():
#     print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


# scheduler = BackgroundScheduler()
# scheduler.add_job(func=print_date_time, trigger="interval", seconds=60)
# scheduler.start()

# # Shut down the scheduler when exiting the app
# atexit.register(lambda: scheduler.shutdown())


stocks = ['aapl']


def runScan():
    text = {}
    # Get News Articles
    for stock in stocks:
        stockInfo = {'ticker':stock}
        articles = getNewsLinksFromGoogleNews(
            connectToAndParseGoogleNews(stock))
        # print(articles)
        articleInfo = [];
        for article in articles:
            text[article] = getArticleText(article)
            # print(text[article])
            sentiment = analyzeSentiment(text[article],article)
            articleInfo.append(sentiment)
            # print(sentiment)
            # Create Object
            # TO DO Store in database
        stockInfo['news'] = articleInfo
        print(stockInfo)

