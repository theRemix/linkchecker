#!/usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup
from texttable import Texttable

domain = sys.argv[-1]
omit = {'/','#'}
links = {}

print("checking links in {}".format(domain))

def recursivelyCheckLinks(link):
    res = requests.get(link)
    links[link] = res.status_code

    if res.status_code != 200:
        return

    soup = BeautifulSoup(res.text, "html.parser")

    for link in soup.find_all("a"):
        l = link.get("href").split('#')[0]
        checkLink = domain + l
        if checkLink not in links and checkLink not in omit and l.startswith('/'):
            recursivelyCheckLinks(checkLink)

recursivelyCheckLinks(domain)

table = Texttable()
table.set_deco(Texttable.HEADER)
table.set_cols_dtype(['t','i',])
table.set_cols_align(["l", "r"])


for link in links:
    table.add_row([link.replace(domain,''), links[link]])

print(table.draw())

print("checked {} links".format(len(links)))
