from bs4 import BeautifulSoup
# import ConfigParser
import requests
import urllib
import sys
import os
import re

#Add support for all pages

#check to see if folder exists,
#Start a cronjob via python -ifneeded

# get parsed images
# scrape images, if image is in parsed images escape it
# download new images
# write new image list to photos

photoList = open("blacklistPhotos.ini").read().splitlines()
# print(photoList)

website = 'http://psiupuxa.com/'
mainDir = os.getcwd()
photoDir = mainDir + '/Photos'
deviceType = 'desktop'
downloadLinks = {}
nuePhotoList = photoList

r  = requests.get(website)
html = r.text
soup = BeautifulSoup(html, "lxml")

posts = soup.find_all('div', class_='post')
for post in posts:
    # continue
    imgPath = post.find('h4').text.replace("#", "").replace(" ", "_").title() + '.jpg'
    if imgPath not in photoList:
        links = post.find_all('a')
        for link in links:
            href = link.get('href')
            if deviceType in href:
                imgURL = href
                print(imgURL)

        photoList += [imgPath]
        downloadLinks[imgPath] = imgURL

if downloadLinks:

    writePhotos = open('blacklistPhotos.ini', 'w')
    photoList = '\n'.join(photoList)
    writePhotos.writelines(photoList)
    writePhotos.close()

    os.chdir(photoDir)
    for name in downloadLinks:
        # continue
        print('downloading: ' + name)
        print(downloadLinks[name], name)
        # urllib
        urllib.request.urlretrieve(downloadLinks[name], name)

    print('finished downloading images')
