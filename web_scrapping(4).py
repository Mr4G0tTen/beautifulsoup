from bs4 import BeautifulSoup
import requests
import re

#=====GETTING WEBSITE HTML=====
search_term = input("what product do you want to search for? ")
url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"

page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#=====QUERYING MULTIPLE PAGES=====
page_text = doc.find(class_ = "list-tool-pagination-text").strong
print(page_text)
#remove all unwanted symbol
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1]) #:-1 to remove last character
print(pages)

items_found = {}

#=====FINDING PRODUCTS=====
for page in range(1, pages+1):
    url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_ = "item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    #to get the same product result from what we are searching for
    items = div.find_all(text=re.compile(search_term)) #without re.compile, it won't detect different character
    for item in items:
        parent = item.parent
        #to skip an item without a link references
        if parent.name != 'a':
            continue
        link = parent['href']
        #find parent tag of the item
        next_parent = item.find_parent(class_="item-container")

        #find parent by using the name class of the parent and the find function
        try:
            price = next_parent.find(class_="price-current").find("strong").string
            items_found[item] = {"price": int(price.replace(",", "")), "link": link}
        except:
            pass


        #input the data to dict
        items_found[item] = {'price': int(price.replace(",","")), 'link' : link}

#print the dict
print(items_found)


#=====SORTING PRODUCT BY PRICE=====
#make the dict into tuple that have key and value. the value is the containt of dictionary.
#tuple is sorting with parameter from lambda which is sorted by the price
#the function of the key is to make lambda can be sorted
sorted_items = sorted(items_found.items(), key=lambda x : x[1]['price'])

for item in sorted_items:
    #it will print the name of the product
    print(item[0]) # '3080 FTW'
    #it will call the value of price item and print it with $ sign
    print(f"${item[1]['price']}") # 'price' : 2999
    print(item[1]['link']) # 'link' : 'www.'
    print('------------------------------------------------------------------------------')

#example: [('3080 FTW', {'price':2999, 'link': 'www.'})]