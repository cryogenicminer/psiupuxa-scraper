from bs4 import BeautifulSoup
import requests
import urllib
import os
import re

#check to see if folder exists,
#agains master list, so that you can delete a image and it wont redowload
#Add support for all pages
#Start a cronjob via python

website = 'http://psiupuxa.com/'
mainDir = os.getcwd()
photoDir = mainDir + '/Photos'
deviceType = 'desktop'
downloadLinks = {}

# settings = open('settings.txt','r')
# logs = settings.read()
# settings.close()
# print logs

photoList = os.listdir(photoDir)

r  = requests.get(website)
html = r.text
soup = BeautifulSoup(html, "lxml")

posts = soup.find_all('div', class_='post')
for post in posts:
    pass
    imgPath = post.find('h4').text.replace("#", "").replace(" ", "_").title() + '.jpg'
    if imgPath not in photoList:
        links = post.find_all('a')
        for link in links:
            href = link.get('href')
            if deviceType in href:
                imgURL = href
        downloadLinks[imgPath] = imgURL

if downloadLinks:
    os.chdir(photoDir)
    for name in downloadLinks:
        pass
        print download
        urllib.urlretrieve(downloadLinks[name], name)
