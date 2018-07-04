# Fail 1,2,3
# import sys
# import PyQt5
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtCore import QUrl
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# # from PyQt5.QtWebKitWidgets import QWebEngineView
# import bs4 as bs
# import urllib.request as ureq
#
#
# class Client(QWebEngineView):
#
#     def __init__(self, url):
#         self.app = QApplication(sys.argv)
#         QWebEngineView.__init__(self)
#         self.loadFinished.connect(self.on_page_load)
#         self.mainFrame().load(QUrl(url))
#
#     def on_page_load(self):
#         self.app.quit()
#
#
# url = 'https://www.dirtrider.com/Off-Road-Motorcycle-search-hub'
# client_response = Client(url)
#
# source = client_response.mainFrame().toHtml()
# soup = bs.BeautifulSoup(source, 'lxml')
# js_test = soup.find('div', class_='result_item')
# print(js_test.text)
#



    # <!DOCTYPE html>
    # <html>
    # <head>
    #   <meta charset="utf-8">
    #   <title>Javascript scraping test</title>
    # </head>
    # <body>
    #   <p id='intro-text'>No javascript support</p>
    #   <script>
    #      document.getElementById('intro-text').innerHTML = 'Yay! Supports javascript';
    #   </script>
    # </body>
    # </html>



# Gets all the items and the div contains an image src, the 'title' of the bike (it contains the year, make, model, and most of the time it has an MSRP (price)

# documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import dryscrape
from bs4 import BeautifulSoup
session = dryscrape.Session()
session.visit('https://www.dirtrider.com/Off-Road-Motorcycle-search-hub')
response = session.body()
soup = BeautifulSoup(response, "lxml")
result_item = soup.find_all(class_="result_image")
for link in result_item:
    for link in soup.find_all('a'):
        print(link.get('href'))


