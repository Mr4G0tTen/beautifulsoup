from bs4 import BeautifulSoup
import requests
url='https://coinmarketcap.com/'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')

#=====TREE STRUCTURE=====
#to get a tag tbody from html
tbody = doc.tbody
print(tbody)

#=====TREE SIBLINGS (all tag inside same parent)=====
#to get all the sibling in the same parent tag
trows = tbody.contents
#to see the info of previous and next sibling
print(trows[0].next_sibling)
print(trows[1].previous_sibling)
#see generator object of next sibling
print(trows[0].next_siblings)
#see all table rows that come after the first table
print(list(trows[0].next_siblings))

#=====TREE PARENTS AND DESCENDANTS====
#give all the information of parent tag
print(trows[0].parent)
#give the name of parent tag
print(trows[0].parent.name)
#descendants give everything information inside the tag
print(list(trows[0].descendants))
print(trows[0].contents)
#only give the name of children tag
print(trows[0].children)

#=====GETTING CRYPTO PRICES=====
#prepare dictionary
prices = {}
#to get the information about name and price for only 10 data
for tr in trows[:10]:
    #only get the data from row 2 and 3
    name, price = tr.contents[2:4]
    #get only the string of the name of token without get the tag
    fixed_name = name.p.string
    #get only the string of the price without get the tag
    fixed_price = price.a.string
    #input the data into the dict
    prices[fixed_name] = fixed_price

#print the final data
print(prices)