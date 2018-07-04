from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl

# Set starting URL
my_url = 'https://www.dirtrider.com/Off-Road-Motorcycle-search-hub?filter[2]=17218'

# to get around the ssl error
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
ssl._create_default_https_context = ssl._create_unverified_context

# opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# htmll parsing
page_soup = soup(page_html, 'html.parser')

#grabs each product
container = page_soup.findAll("div",{"class":"result_item"})


print(len(container))




