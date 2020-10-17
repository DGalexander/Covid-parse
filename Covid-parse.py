# quick program to webscrape and parse html from Gov.UK
# version 1

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# BS setup
url = 'https://www.gov.uk/guidance/full-list-of-local-covid-alert-levels-by-area'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# setup csv
file = open('Covid_level.csv', 'w')
writer = csv.writer(file)
# row header
writer.writerow(['Covid_level'])


# subset the correct div "govspeak"
# this is not needed but it helps reduce the chance of the sting being repeated elsewhere in the html
div = soup.find("div", {"class": "govspeak"})

# subset by finding the tag 'name'
for name in div.find_all(["h2", "h3"]):
    name = name.contents[0]
    print(name)
    writer.writerow([name])

file.close()
