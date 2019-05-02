#!/usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup

domain = sys.argv[-1]
omit = {'/','#'}
links = {}

def recursivelyCheckLinks(link):
    res = requests.get(link)
    links[link] = res.status_code

    if res.status_code != 200:
        return

    soup = BeautifulSoup(res.text, "html.parser")

    for link in soup.find_all("a"):
        l = link.get("href")
        checkLink = domain + l
        if checkLink not in links and checkLink not in omit and l.startswith('/'):
            recursivelyCheckLinks(checkLink)

recursivelyCheckLinks(domain)

# for link in filter(lambda l: l not in omit and l.startswith('/'), links):
for link in links:
    print("{url}\t\t{statusCode}".format(url=link, statusCode=links[link]))

print("checked {} links".format(len(links)))
