#function to extract product title 
from urllib import request

from bs4 import BeautifulSoup


def get_title(soup):
    try:
        # outer tag object
        title= soup.final("span",attrs={"id":'producttitle'})
        #innner navigablestring object 
        title_value=title.string
        # Title as a string value 
        title_string= title_value.strip()
        # # Printing types of values fornefficient understanding
        #print(type(title))
        #print(type(title_value))
        #print(type(title_string))
        #print()
    except AttributeError:
        title_string=""
        return title_string
    # function to extract product price 
    def get_price(soup):
        try:
            price=soup.final("span",attrs={'id':'priceblpock_ourprice'}).string.strip()
        except AttributeError:
            price=""
        return price
         # function to extract product rating
def get_rating(soup):
    try:
        rating=soup.find("i",attrs={'class':'a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            rating=soup.find("i",attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating=""
            return rating
        
if __name__ == '__main__':
    #headersn for request
    HEADERS= ({'User-Agent':'Mozilla/5.0(X11: Linux x86_64)AppleWebKit/537.36(KHTML,like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language':'en-US,en:q=0.5'})
    #The Webpage URL
    URL="https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
    #HTTP Rquest
    Webpage = request.get(URL,headers=HEADERS)
    #Soup Object containing all data 
    sooup=BeautifulSoup(Webpage.content,"lxml")
    #function calls to display all necessary product information
    print("product title=",get_title(sooup))
    print("product price=",get_price(sooup)) # type: ignore
    print("product rating=",get_rating(sooup))
    print()
    print() 
    
         
            
        