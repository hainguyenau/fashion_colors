import os
import requests
import re
from bs4 import BeautifulSoup
from urllib import urlretrieve

def img_downloader(r, folder):
    '''
    INPUT: BeautifulSoup request r, folder name (string)
    OUTPUT: none
    '''
    # Create folder if not exists
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Parse HTML
    soup = BeautifulSoup(r.text, 'html.parser')

    # Get text containing links
    text = str(soup.body.findAll(text=re.compile("http://assets.vogue.com/photos/"), limit=1))

    # Find the part inside the links to images
    match = re.findall(r'http://assets.vogue.com/(.*?).jpg', text)

    # Remove duplicates
    s = list(set(match))

    # Generate full links, remove irrelevant link
    links = []
    for link in s:
        if 'lemlem' in link:
            link = 'http://assets.vogue.com/' + link + '.jpg'
            links.append(link)

    # Retrieve images
    for i in range(len(links)):
        urlretrieve(links[i], filename = folder + '/' + str(i+1) + '.jpg')

if __name__ == '__main__':
    # Request pages
    r1 = requests.get('http://www.vogue.com/fashion-shows/resort-2017/lemlem/slideshow/collection#1')
    r2 = requests.get('http://www.vogue.com/fashion-shows/resort-2018/lemlem/slideshow/collection#1')


    # Download images
    img_downloader(r1, '2017')
    img_downloader(r2, '2018')
