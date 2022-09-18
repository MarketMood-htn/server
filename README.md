Description:
This application is responsible for exploring the web and scraping recent news that may affect the direction of stock prices. 
It then processes the articles, and uses co:here API to read the sentiments of each article. The data is then uploaded to the database. This process occurs every 10 minutes to increase the accuracy of the model.

How to use:

Install Python 3.

Use pip to install BeautifulSoup, Flask, Co:Here

To run, enter "flask run" in the terminal.
