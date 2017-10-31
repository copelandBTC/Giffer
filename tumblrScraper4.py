"""
This script was responsible for pulling the gif files that are to be used by the main script
"""

from bs4 import BeautifulSoup as sopa, SoupStrainer
import urllib.request

baseurl = "http://myprofile.tumblr.com"
url = baseurl + "/archive/"
tumblrSrc = urllib.request.urlopen(url)
linksFile = open("path/to/links.txt", "w+")
listCnt = 0
pgCnt = 0

while pgCnt <= 189:    
    #Get images
    imgs = sopa(tumblrSrc, "html.parser", parse_only = SoupStrainer("div", {"data-imageurl" : True}))

    #put all gif urls in a list
    for i in imgs:
        if str(i['data-imageurl']).endswith(".gif"):
            linksFile.write(str(i['data-imageurl']) + "\n")
            listCnt += 1

    #Get next page
    """
    NOTE: you have to reopen the url. once you pass tumblrSrc through BeautifulSoup with a Soup Strainer, it will affect tumblrSrc directly
    """
    
    tumblrSrc = urllib.request.urlopen(url)
    np = sopa(tumblrSrc, "html.parser", parse_only = SoupStrainer("a", {"id" : "next_page_link"}))

    #update URL
    url = baseurl + np.a["href"]

    tumblrSrc = urllib.request.urlopen(url)
    pgCnt += 1

    #TEST
    print(pgCnt)


#download all gifs from list
with open("path/to/links.txt", "r") as lf:
    index = 1

    while index <= listCnt:
        line = lf.readline()
        urllib.request.urlretrieve(line, "gifs/" + str(index) + ".gif")
        index += 1

