# Python requests module has several built in methods to make HTTP requests to sepcified URL 
import requests
# The Beautiful soup library provides simple methods and pythonic phrases for guiding searching and changing a parse tree 
from bs4 import BeautifulSoup
import pandas as pf
import time 

# create a function to scrape ebay for current arcade machine prices 
# creating a list to store data 
data = []
current_page = 1
proceed = True

while(proceed):
    print("Currently scraping page: "+str(current_page))
    url = "https://books.toscrape.com/catalogue/page-"+str(current_page)+".html"

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser") 
    # This accounts for the last page of the book list 
    if soup.title.text == "404 Not Found" :
        proceed = False
    else:

        #use html tag that contails all of the books 
        # the books are stores in a li list tag include the class link 
        # use Beautiful soup library find_all function 
        all_books = soup.find_all("li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")
        #find_all returns a list element we can use a for loop to parse this data 
        for book in all_books :
            item = {}
        
            # create disctionary keys for the following information 
            # title of the book , link of the product, and the price 
            #.find finds the first image tag use .attrs it is extremely useful here in terms of finding the first occurance of the attribute 
            item['Title'] = book.find("img").attrs["alt"]
            item['Link'] = book.find("a").attrs["href"]
            #use string parsing tool to extract all of the characters after the third 
            #use .text to get the text part of the tag
            item['Price'] = book.find("p", class_ = "price_color").text[2:]
            #for finding the status of the product use the strip tool to delete any unintended whitespace 
            item['Stock'] = book.find("p", class_="instock availability").text.strip()

            #input the specific data correlated to the book into the master list of book attribute data titled data 

            data.append(item)

            print(item['Stock'])


    
    current_page +=1

# Here we will use the panda library to insert the data into the excel sheet 
df = pf.DataFrame(data)
df.to_excel("books.xlsx")
