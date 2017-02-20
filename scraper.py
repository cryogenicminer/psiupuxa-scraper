from bs4 import BeautifulSoup
import requests
import re
import urllib
import os

#check to see if folder exists,
#check if the newest photo is in folder
#run the downloads as a batch from like an array at the end.
#Add support for all pages
#Start a cronjob via python

website = 'http://psiupuxa.com/'
device = 'desktop'
path = 'Photos'

os.chdir(path)
print os.getcwd()

r  = requests.get(website)
html = r.text
soup = BeautifulSoup(html, "lxml")

posts = soup.find_all('div', class_='post')
for post in posts:
#Finding the photo Name.
    name = post.find('h4').text.replace("#", "").replace(" ", "_").title()
    # name = name.replace("#", "").replace(" ", "_").title()
    imgPath = name +".jpg"
    print imgPath

#Finding the device link.
    links = post.find_all('a')
    for link in links:
        href = link.get('href')
        if device in href:
            imgURL = href

    urllib.urlretrieve(imgURL, imgPath)
