# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:28:54 2019

@author: Kasia
"""

import requests
from bs4 import BeautifulSoup

titles = []
base_url = 'https://www.nytimes.com'
r = requests.get(base_url)

zmienna = r.text
soup = BeautifulSoup(r.text, features = "html.parser")

for a in soup.find_all('h2'):
    print(a.text)
    
    
for balancedHeadline in soup.find_all('h2'):
    titles.append(balancedHeadline.text)
    
titles = '\n'.join(titles)

print(titles)

