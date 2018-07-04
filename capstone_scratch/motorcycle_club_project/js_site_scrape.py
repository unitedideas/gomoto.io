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


import dryscrape
from bs4 import BeautifulSoup
session = dryscrape.Session()
session.visit('https://www.dirtrider.com/Off-Road-Motorcycle-search-hub')
response = session.body()
soup = BeautifulSoup(response, "lxml")
print(soup.find_all(class_="result_item"))



    # from selenium import webdriver
    # driver = webdriver.PhantomJS()
    # driver.get("http://avi.im/stuff/js-or-no-js.html")
    # p_element = driver.find_element_by_id(id_='intro-text')
    # print(p_element.text)





