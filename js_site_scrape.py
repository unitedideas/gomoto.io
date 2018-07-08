import dryscrape, time, requests, re
import os
import sys
import django
from bs4 import BeautifulSoup
import os, sys




from mysite.gomoto.models import Bike




base_url = 'https://www.dirtrider.com'


def full_url(sub_url):
    print('Full url: ' + base_url + sub_url)
    return base_url + sub_url


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


def check_data_key_top_four(data_points, top_four_keys):

    #for the non-table items
    for key in top_four_keys:
        if data.find(string=key) is not None:
            data_text = data.span.text
            # Regex the string and then change to an int
            print('top four keys')
            print('<------------>')
            return ()

        #if none of the keys exist set value of sent key to None
        else:
            return None

def check_data_key_table_items(data_points, key):

    #for the table items
    if data.find(string=key) is not None:
        data_text = data.span.text
        # Regex the string and then change to an int
        print('table keys')
        print('<------------>')
        return ('table keys')

    #if none of the keys exist set value of sent key to None
    else:
        return None


def bike_page(bike_page_url):

    # time.sleep(2)

    bike_page_data = requests.get(bike_page_url)

    bike_page_text = bike_page_data.content

    # print(bike_page_text)

    print('Visiting the Bike Page URL...')

    print('Status: ' + str(bike_page_data.status_code))

    bike_soup = BeautifulSoup(bike_page_text, "lxml")

    #Start getting individual bike data

    #Data for the non-table items
    data_points = bike_soup.find_all(class_="buyers-guide--intro-stats-item")

    # check_data_key_top_four(data_points, top_four_keys)

    # print(data_points)

    print(' Top Four ' + str(len(data_points)))
    # for key in top_four_keys:
    #     if key in str(data_points):
    #         print('it worked for: ' + key)


    data_points = bike_soup.find(class_='left-cell cell text-cell buyers-guide--specs')
    those = data_points.find_all('span')
    print(those[0].get_text())
    print(' Table Items ' + str(len(data_points)))
    # for key in top_four_keys:
    #     if key in str(data_points):
    #         print('it worked for: ' + key)

    data_points = bike_soup.find(class_='page-title')
    make = data_points.get_text()
    # bike = Bike()
    # bike.make = make
    #     if key in str(data_points):
    #         print('it worked for: ' + key)

    #         class="page-title"

    # table_data_points = ""
    #
    # bike = Bike()
    #
    # bike.year = #...
    # # ...
    # bike.save()


    return "bike_data " + str(general_count)


def page_session(page_count):
    print('Page Count: ' + str(page_count))
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
top_four_keys = [('MSRP','price'),('Displacement (CC)','displacement'), ('Seat Height (in)', 'seatheight'), ('Wet Weight (lbs)','wet_weight'),('Dry Weight (lbs)','dry_weight')]

table_keys = [('Starter','starter'),('Manufacturer Type','category'),('Engine Type','engine_type')]

title_keys = ['year', 'make', 'model', ]


while page_count > 0:
    page_soup = page_session(page_count)
    result_items = page_soup.find_all(class_="result_item")

    print('There are ' + str(len(result_items)) + ' items')

    for item in result_items:

        anchor = item.find_all('a')[0]

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


