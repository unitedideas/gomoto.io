import dryscrape, time, requests, re, csv
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from gomoto.models import Bike

class Command(BaseCommand):

    def handle(self, *args, **options):
        # write the code here
        page_count = 19
        general_count = 1
        data_list_of_dicts = []
        missed_pages = []

    # from mysite.gomoto.models import Bike

        base_url = 'https://www.dirtrider.com'


        def full_url(sub_url):
            print('Full url: ' + base_url + sub_url)
            return base_url + sub_url


        # def has_class_but_no_id(tag):
        #     return tag.has_attr('class') and not tag.has_attr('id')

        def page_session(page_count):
            print('Page Count: ' + str(page_count))
            page = '?page=' + str(page_count)

            if page_count == 0:
                full_url = base_url + '/Off-Road-Motorcycle-search-hub'
            else:
                full_url = base_url + '/Off-Road-Motorcycle-search-hub' + page
                print(full_url)

            sess = dryscrape.Session()

            print('Visiting the Main Page URL...')
            sess.set_attribute('auto_load_images', False)

            sess.visit(full_url)

            # print('Status: ', sess.status_code())

            response = sess.body()
            page_soup = BeautifulSoup(response, "lxml")
            return page_soup


        def bike_page(bike_page_url):
            # time.sleep(2)
            bike_dict = {'img_src': 'https://www.harpersphoto.co.uk/user/products/large/no%20image.gif',
                    'price': 99999, 'displacement': 0, 'seatheight': 0, 'wet_weight': None, 'dry_weight': None,
                    'starter': 'Kick', 'category': 'Off-Road', 'engine_type': 'Four-stroke', 'year': 1900, 'make': 'Unknown',
                    'model': 'Unknown'}

            if bike_page_url == 'https://www.dirtrider.com/2016-husqvarna-701-enduro' or bike_page_url == 'https://www.dirtrider.com/2014-ktm-150-sx' or bike_page_url == 'https://www.dirtrider.com/2014-triumph-tiger-800-xc-abs-se' or bike_page_url == 'https://www.dirtrider.com/2017-beta-125-rr-s':
                bike_dict = {
                    'img_src': 'https://www.dirtrider.com/sites/dirtrider.com/files/styles/1000_1x_/public/buyers_guide/2017/2017_Husqvarna_Enduro_701.jpg?itok=XP0WDuct',
                    'price': 11799, 'displacement': 693, 'seatheight': 36, 'wet_weight': None, 'dry_weight': 320,
                    'starter': 'Electric', 'category': 'Off-Road', 'engine_type': 'Four-stroke', 'year': 2016, 'make': 'Husqvarna',
                    'model': '701 Enduro'}

                print('saving to table')
                print(bike_dict)
                bike = Bike(**bike_dict)
                # bike.make = make
                # bike.year = #...
                bike.save()

            bike_page_data = requests.get(bike_page_url)

            bike_page_text = bike_page_data.content

            # print(bike_page_text)

            # print('Visiting the Bike Page URL...')
            # print(bike_page_url)

            # print('Status: ' + str(bike_page_data.status_code))

            bike_soup = BeautifulSoup(bike_page_text, "lxml")

            # Getbike image src

            data_points = bike_soup.find(class_='field-image')

            image = data_points.find('img')
            if image['data-1000src']:
                bike_dict['img_src'] = image['data-1000src']
            elif image['src']:
                bike_dict['img_src'] = image['src']
            else:
                bike_dict['img_src'] = None


            if Bike.objects.filter(img_src=bike_dict['img_src']).exists():
                print('SKIPPING BIKE ' + bike_dict['img_src'])
                return


            # Data for the non-table items
            data_points = bike_soup.find_all(class_="buyers-guide--intro-stats-item")
            # data_values = data_points[count].span.get_text()
            # print(data_values)

            # check_data_key_top_four(data_points, top_four_keys)

            # print(data_points)
            # print('Top Five ' + str(len(data_points)))
            count = 0
            for key in top_five_keys:
                value = None
                if key[0] in str(data_points):
                    data_value = data_points[count].span.get_text()
                    # print(data_value)
                    # print('it worked for: ' + key[1])
                    value = data_value
                    if key[0] == 'MSRP':
                        # data_value = data_points[count].span.get_text()
                        # re.
                        value = ''.join(re.findall(r'\d+', data_value))

                    if value:
                        ## try/ except is only here because of 1 edge case int conversion
                        try:
                            value = int(value)
                        except:
                            value = 12499

                    bike_dict[key[1]] = value
                    # print(bike_dict[key[1]])
                    count += 1
                else:
                    bike_dict[key[1]] = value
                    # print('No Data for: ' + key[1])

            # Get data from tables

            data_points = bike_soup.find(class_='panel-pane pane-entity-field pane-node-field-page-sections')
            spans = data_points.find_all('span')
            for key in table_keys:
                value = None
                # print(span)
                # print(span[count].get_text())
                for span in spans:
                    if key[0] in span:
                        value = span.next_sibling.get_text()
                        bike_dict[key[1]] = value
                    else:
                        bike_dict[key[1]] = value

                    if key[0] == 'Valve Configuration' and bike_dict[key[1]] == None:
                        bike_dict[key[1]] = 'Electric'

                    if bike_dict[key[1]] == 'Competition':
                        bike_dict[key[1]] = 'Motocross'


                    if bike_dict[key[1]] == 'Reed  Valve':
                        bike_dict[key[1]] = 'Two-stroke'
                    elif bike_dict[key[1]] == 'Electric':
                        bike_dict[key[1]] = 'Electric'

                    if bike_dict['category'] == None:
                        bike_dict['category'] = 'Off-Road'



            # Get year, make, model

            data_points = bike_soup.find(class_='page-title')
            title = data_points.get_text().lower()
            # print(title)

            # year
            year = ''.join(re.findall(r'\d{4}', title))
            bike_dict['year'] = int(year)
            if len(year) > 4:
                year = year[0:4]

            # make
            for make in make_list:
                if make[0] in title:
                    bike_dict['make'] = make[1]  # Could have used title() method here ¯\_(ツ)_/¯

                    # print(bike_dict['make'])

                    # This is still execution todo item
                    # else:
                    #     hope = ''.join(re.findall(r'\b[^\d\W]+a{1}\b', title))
                    #     bike_dict['make'] = hope
                    # model

                    model = ''.join(re.findall(r'(?<=' + make[0] + '\s).*', title))
                    bike_dict['model'] = model.title()

                    # print(bike_dict['model'])

            # print(bike_dict)
            # return bike_dict

            print('saving to table')
            bike = Bike(**bike_dict)
            # bike.make = make
            # bike.year = #...
            bike.save()


        make_list = [
            ('aprilia', 'Aprilia'),
            ('beta', 'Beta'),
            ('bmw', 'BMW'),
            ('ducati', 'Ducati'),
            ('gas gas', 'Gas Gas'),
            ('honda', 'Honda'),
            ('husaberg', 'Husaberg'),
            ('husqvarna', 'Husqvarna'),
            ('hyosung', 'Hyosung'),
            ('kawasaki', 'Kawasaki'),
            ('ktm', 'KTM'),
            ('moto guzzi', 'moto Guzzi'),
            ('suzuki', 'Suzuki'),
            ('triumph', 'Triumph'),
            ('yamaha', 'Yamaha'),
            ('zero', 'Zero')
        ]



        top_five_keys = [('MSRP', 'price'), ('Displacement (CC)', 'displacement'), ('Seat Height (in)', 'seatheight'),
                         ('Wet Weight (lbs)', 'wet_weight'), ('Dry Weight (lbs)', 'dry_weight')]

        table_keys = [('Starter', 'starter'), ('Manufacturer Type', 'category'), ('Valve Configuration', 'engine_type')]

        title_keys = ['year', 'make', 'model', ]

        while page_count > 0:
            page_soup = page_session(page_count)
            result_items = page_soup.find_all(class_="result_item")

            # print('result_items len : ' + str(len(result_items)))

            # print('There are ' + str(len(result_items)) + ' items on this page')

            if len(result_items) == 0:
                missed_pages.append(page_count)
                print('Adding page ' + str(page_count) + ' to missed_pages')
                print('Missed pages are ' + str(missed_pages))
            else:
                for item in result_items:
                    anchor = item.find_all('a')[0]

                    sub_url = anchor.get('href')
                    # print(sub_url)

                    bike_page_url = full_url(sub_url)

                    try:
                        data_list_of_dicts.append(bike_page(bike_page_url))
                    except:
                        print('ERROR GETTING BIKE ' + bike_page_url)
                    # print(data_list_of_dicts)

                    # print('\n','\n','\n')
                    # print(str(anchor) + '\n')

            page_count -= 1

            print('Pages Remaining: ' + str(page_count))

        while len(missed_pages) > 0:

            page_soup = page_session(missed_pages[0])

            result_items = page_soup.find_all(class_="result_item")

            print('There are ' + str(len(result_items)) + ' items on this page')

            if len(result_items) == 0:
                missed_pages.append(missed_pages[0])
                print('Adding page ' + str(missed_pages[0]) + ' back to missed_pages')
            else:
                for i in range(len(missed_pages) - 1, -1, -1):
                    # print(missed_pages[i])
                    if missed_pages[0] == missed_pages[i]:
                        del missed_pages[i]
                        # print('Remaining missed_pages are: ' + str(missed_pages))

                # print(len(missed_pages))
                for item in result_items:
                    anchor = item.find_all('a')[0]

                    sub_url = anchor.get('href')
                    # print(sub_url)

                    bike_page_url = full_url(sub_url)

                    data_list_of_dicts.append(bike_page(bike_page_url))

            print('Missd Pages Remaining: ' + str(len(missed_pages)))

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

        # Write to CSV

        # print('Writting to CSV File...')
        # keys = data_list_of_dicts[0].keys()
        # with open('dirt_bike_data.csv', 'w') as output_file:
        #     dict_writer = csv.DictWriter(output_file, keys)
        #     dict_writer.writeheader()
        #     dict_writer.writerows(data_list_of_dicts)

            #################### NoGo Code Below ################

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
            # page_count -= 1

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

        # def check_data_key_top_four(data_points, top_four_keys):
        #     # for the non-table items
        #     for key in top_four_keys:
        #         if data.find(string=key) is not None:
        #             data_text = data.span.text
        #             # Regex the string and then change to an int
        #             print('top four keys')
        #             print('<------------>')
        #             return ()
        #
        #         # if none of the keys exist set value of sent key to None
        #         else:
        #             return None
        #
        #
        # def check_data_key_table_items(data_points, key):
        #     # for the table items
        #     if data.find(string=key) is not None:
        #         data_text = data.span.text
        #         # Regex the string and then change to an int
        #         print('table keys')
        #         print('<------------>')
        #         return ('table keys')
        #
        #     # if none of the keys exist set value of sent key to None
        #     else:
        #         return None
    pass