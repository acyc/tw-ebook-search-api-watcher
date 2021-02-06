#! /usr/bin/python

import json
import re
import urllib.parse
import urllib.request
import sys

file = open("watch-list","r")
if len(sys.argv) < 2:
    print("API domain required.")
    print("usage: python3 ebook-watcher.py [apiDomain]")
    exit()

apiDomain = sys.argv[1]

for line in file:
    watchItem = line.split("|",2)
    stores = watchItem[0].split(",")
    searchKeyword = watchItem[1].strip()
    filterWord = watchItem[1].strip()
    if len(watchItem) > 2:
       filterWord = watchItem[2].strip() 

    #print(stores)
    print("================================================")    
    searchUrl = apiDomain+"/search?q="+urllib.parse.quote(searchKeyword)
    print("search for: "+searchKeyword+" "+searchUrl)
    # print(searchUrl)

    searchResult = urllib.request.urlopen(searchUrl)
    # print(searchResult)

    searchResultJson = json.load(searchResult)
    #print(searchResultJson)

    print("filtering the book title with pattern: "+filterWord)
    print("")
    for store in stores:
        storeResult = searchResultJson[store.strip()]
        #print(storeResult)
        match = 0
        for book in storeResult:
            bookTitle = book["title"]            
            if re.search(filterWord,bookTitle):
                #print("")
                print("match found @"+store)
                print(bookTitle)
                print(book["link"])
                print("")
                match+=1
        if match == 0:
        	print("NO match found @"+store+"("+str(len(storeResult))+")")
        	print("")
print("================================================")    
