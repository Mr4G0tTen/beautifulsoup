#Beautiful Soup is work in tree structure
from bs4 import BeautifulSoup
import requests

#=====READING HTML FILES=====
#html.parser use to make file html can executed in python module
with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#prettify use for keep the indentation when we call file html
print(doc.prettify()) 

#=====FIND BY TAG NAME=====
#doc.firsttagthatwesearch is to find the first tag that we want to search by the tag name
tag = doc.title
#you can also change string value
tag.string = "hello"
#tag.string is to get string between tag
print(tag.string)

#=====FIND ALL BY TAG NAME=====
#find_all is to find all tag that we want to search by the tag name
tags = doc.find_all('p')
print(tags)

#=====FIND NESTED TAG=====
tags = doc.find_all('p')[0]
print(tags.find_all('b'))

#=====PARSING WEBSITE HTML=====
#parsing external website
url = ''
#request meminta mengakses url
result = requests.get(url)
#hasilnya akan berupa text
doc = BeautifulSoup(result.text, 'html.parser')

#=====LOCATING TEXT=====
#mencari kata dalam website tersebut
kata = doc.find_all(text = 'python')
#to get the entire tag within search word
parent = kata[0].parent
print(parent)

