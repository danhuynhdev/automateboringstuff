#!/usr/bin/env python3

import requests, sys, webbrowser, bs4

print('Googling....')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.r a')

links = [linkElem.get('href') for linkElem in linkElems]

numOpen = min(5, len(links))

for i in range(numOpen):
    webbrowser.open('http://google.com' + links[i])
