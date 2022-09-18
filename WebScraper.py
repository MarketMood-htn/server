import re
import requests
from bs4 import BeautifulSoup

def connectToAndParseGoogleNews(symbol):
    try:
        url = "https://www.google.com/search?q="+symbol+"+stock&rlz=1C1RXQR_enCA1008CA1008&tbm=nws&sxsrf=ALiCzsbE0o2Uo1nomFMjUeMyv2zghrvn3w:1663463316421&source=lnt&tbs=sbd:1&sa=X&ved=2ahUKEwjgtsbgk536AhWbrYkEHZX1CDwQpwV6BAgBECE&biw=1280&bih=649&dpr=3"
        return BeautifulSoup(requests.get(url).content, "html.parser")
    except:
        print("An error has occured connecting to Google News")


def getNewsLinksFromGoogleNews(result):
    try:
        urls = []
        for link in result.findAll('a'):
            if("https" in link.get('href') and not ("google" in link.get('href'))):
                l = link.get('href').replace("/url?q=","").split("&sa=U")[0]
                urls.append(l)
        return urls
    except:
        print("An error has occured extracting links from Google News")
    
def getArticleText(url):
    try:
        content = ""
        req = requests.get(url)
        texts = BeautifulSoup(req.content, "html.parser").select("h1, h2, h3, p")
        for text in texts:
            content+=text.get_text().strip() + " "
        return content
    except Exception as e: print(e)