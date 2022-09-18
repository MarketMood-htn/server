from urllib import request
import requests
from flask import jsonify
import json


def postArticles(data, ticker, articles):
    try:
        headers = {'Content-type': 'application/json'}
        # Check if ticker already exists
        get = requests.get('http://127.0.0.1:8000/stock/ticker/' + ticker)
        if(get.status_code==200):
            all_articles = get.json()['all_articles']
            all_articles.extend(articles)
            r = requests.put('http://127.0.0.1:8000/stock/id/' + get.json()['_id'], data=json.dumps({
                'all_articles': all_articles
            }))
        else:
            r = requests.post('http://127.0.0.1:8000/stock/', headers=headers, data=json.dumps({
                'ticker': ticker,
                'name': ticker,
                'all_articles': articles
            }))
            # print(r)
            # print(r.json())
    except Exception as e:
        print(e)