# quick program to webscrape and parse html from Gov.UK
# version 1

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.gov.uk/guidance/full-list-of-local-covid-alert-levels-by-area'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


# subset the correct div "govspeak"
# this is not needed but it helps reduce the chance of
# the sting being repeated elsewhere in the html
div = soup.find("div", {"class": "govspeak"})
#div2 = soup("h2")

# this finds a specific string
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
import re
for tag in div.find_all(string=re.compile("Local COVID alert level: high")):
    print(tag)


# this finds all the next h3 but doesn't stop at Local COVID alert level: very high"
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all-next-and-find-next
test= tag.find_all_next("h3")
print(test)



# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-previous-siblings-and-find-previous-sibling
