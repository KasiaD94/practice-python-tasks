# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:22:35 2019

@author: Kasia
"""

import requests
from bs4 import BeautifulSoup

def html_to_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for lines in soup.find_all('p'):
        print(str(lines.getText()))
    
if __name__ == "__main__":
    url1 = "https://content.time.com/time/magazine/article/0,9171,2005869,00.html"
    url2 = "https://content.time.com/time/magazine/article/0,9171,2005869-2,00.html"
    html_to_text(url1)
    html_to_text(url2)
    