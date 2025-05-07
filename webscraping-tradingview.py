from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'https://www.webull.com/quote/us/gainers'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

stock_data = soup.findAll("div", class_= 'table-cell')

#print(stock_data[3].text)

counter = 1
for x in range(5):
    name = stock_data[counter].text
    name = name.find('p', class_='txt')
    print(name)
    input()
    change = float(stock_data[counter+2].text.strip('+').strip('%')/100)
    last_price = float(stock_data[counter+3].text)
    prev_price = round(last_price / (1+change),2)


    print(f'Company name: {name}')
    print(f'Change: {change}')
    print(f'Price: {last_price}')
    print(f'Previous Price: {prev_price}')    

    counter += 11


		







