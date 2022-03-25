from bs4 import BeautifulSoup
import requests
import re

#html.parser use to make file html can executed in python module
with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#=====SEARCHING FOR TAG=====
#how to edit tag attribut
tag = doc.find("option")

#=====TAG ATTRIBUTES=====
print(tag.attrs)
tag['selected'] = 'false'
tag['color'] = 'blue'
print(tag)

#=====FIND MULTIPLE TAG=====
tags = doc.find_all(['p','div','li'])
print(tags)

#=====FIND ATTRIBUTES=====
#text for the value of string between tag, value is attribute from tag
tags = doc.find_all(['option'], text='undergraduate',value='undergraduate')
print(tags)

#=====FIND CLASS NAMES=====
#class_ for find class name
tags = doc.find_all(class_='btn-item')
print(tags)

#=====FIND WITH REGULAR EXPRESSIONS=====
#find text with regular expression
tags = doc.find_all(text=re.compile('\$.*'))
for tag in tags:
    #to remove whitespace
    print(tag.strip())

#=====FIND LIMIT=====
#limit the amount of the result
tags = doc.find_all(text=re.compile('\$.*'), limit=1)
for tag in tags:
    print(tag.strip())

#make changed into file html
tags = doc.find_all('input',type='text')
for tag in tags:
    tag['placeholder'] = 'I changed you!'

#=====SAVE MODIFIED HTML=====
#saved modified document
with open('changed.html', 'w') as file:
    file.write(str(doc))