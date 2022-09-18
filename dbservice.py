import requests

def postArticles(ticker, articles):
    r = requests.post('http://127.0.0.1:8000/stock', 
        {
            'ticker':ticker,
            'name':ticker,
            'all_articles':articles,
        }
    )
