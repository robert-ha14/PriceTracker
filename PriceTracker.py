from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.ebay.com/itm/Canon-EOS-Rebel-T5-EOS-1200D-18-0MP-Digital-SLR-Camera-Black-Kit-w-EF-S/133233664586?epid=203489846&hash=item1f0558624a:g:Dy8AAOSwk5FdxbzX'

def get_price():
	page = requests.get(url)
	html_contents = page.text

	soup = BeautifulSoup(html_contents, 'html.parser')

	tag = soup.find(id="prcIsum")
	return(tag['content'])

currentPrice = get_price()

while(currentPrice == get_price()):
	currentPrice = get_price()
	print currentPrice
	time.sleep(1)

print "change in price!"