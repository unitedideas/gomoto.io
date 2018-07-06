import dryscrape
from bs4 import BeautifulSoup
import time
import requests
import re

base_url = 'https://www.dirtrider.com'


def full_url(sub_url):
    print('Full url: ' + base_url + sub_url)
    return base_url + sub_url


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')



def bike_page(bike_page_url):

    bike_dict = {}

    # time.sleep(2)


    bike_page_data = requests.get(bike_page_url)

    bike_page_text = bike_page_data.text

    # print(bike_page_text)

    print('Visiting the Bike Page URL...')

    print('Status: ' + str(bike_page_data.status_code))

    bike_soup = BeautifulSoup(bike_page_text, "lxml")

    # print(bike_soup)


    #Start getting the data here
    #These are the first four items

    data_points = bike_soup.find_all(class_="buyers-guide--intro-stats-item")

    for data in data_points:
        if data.find(string='MSRP') is not None:
            print(data.span.text)
            print('<------------>')

        # print(data_points)

    #Need to get the remaining items from below

    # print(bike_page_text)
    #
    # for item in result_items:
    #     for image in item.find_all('img'):
    #         print("Image: " + image.get('src'))
    #
    #     for anchor in item.find_all('a'):
    #         if general_count % 2 == 0:
    #             bike_text = anchor.get_text()
    #             sub_url = anchor.get('href')
    #             bike_page_url = full_url(sub_url)

    return "bike_data " + str(general_count)


def page_session(page_count):
    print('Bike Count: ' + str(page_count))
    page = '?page=' + str(page_count)

    if page_count == 0:
        full_url = base_url + '/Off-Road-Motorcycle-search-hub'
    else:
        full_url = base_url + '/Off-Road-Motorcycle-search-hub' + page

    sess = dryscrape.Session()
    print('Visiting the Main Page URL...')
    sess.set_attribute('auto_load_images', False)

    sess.visit(full_url)

    print('Status: ', sess.status_code())

    response = sess.body()
    page_soup = BeautifulSoup(response, "lxml")
    return page_soup


page_count = 2
general_count = 1

data_list_of_dicts = []


while page_count > 0:
    page_soup = page_session(page_count)
    result_items = page_soup.find_all(class_="result_item")

    print('There are ' + str(len(result_items)) + ' items')

    for item in result_items:

        anchor = item.find_all('a')[0]

        bike_text = anchor.get_text()
        sub_url = anchor.get('href')
        bike_page_url = full_url(sub_url)

        data_list_of_dicts.append(bike_page(bike_page_url))

        print(data_list_of_dicts)

        print('\n')
        # print(str(anchor) + '\n')

    print('Pages Remaining: ' + str(page_count))


        # for anchor in item.find_all('a'):
        #     if general_count % 2 == 0:
        #         bike_text = anchor.get_text()
        #         sub_url = anchor.get('href')
        #         bike_page_url = full_url(sub_url)
        #
        #         data_list_of_dicts.append(bike_page(bike_page_url))
        #
        #         print(data_list_of_dicts)
        #
        #         print('\n')
        #         # print(str(anchor) + '\n')
        #
        #         print('Page count: ' + str(general_count / 2))
        #     general_count += 1
    page_count -= 1



# psudo Process Code:
# loop over ever page
# look over the results on the page
# visit the link for that result


# Failed attempts 1,2,3...
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


# <----------------Another way of doing it ----------------->
# sess = dryscrape.Session()
# url = 'https://www.dirtrider.com/Off-Road-Motorcycle-search-hub'
# print ('Visiting the URL...')
# # sess.set_attribute('auto_load_images', False)
# sess.visit(url)
# print ('Status: ', sess.status_code())
# for link in sess.xpath("//div[@class='result_image']"):
#     print ('Bike Link: ', link.at_xpath(".//a"))
#


# Gets all the items and the div contains an image src, the 'title' of the bike (it contains the year, make, model, and most of the time it has an MSRP (price)


# documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
