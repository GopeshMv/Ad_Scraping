import requests, lxml, urllib.parse, sys
from bs4 import BeautifulSoup


headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}

# Search query
params = {'q': '//Any type of advertisements that needs to be extracted'}

# Getting HTML response
html = requests.get(f'https://www.google.com/search?q=',
                    headers=headers,
                    params=params).text

# Getting HTML code from BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

# Looking for container that has all necessary data findAll() or find_all()
for container in soup.findAll('div', class_='RnJeZd top pla-unit-title'):
  # Scraping title
  title = container.text

  # Creating beginning of the link to join afterwards
  startOfLink = 'https://www.googleadservices.com/pagead'
  # Scraping end of the link to join afterwards
  endOfLink = container.find('a')['href']
  # Combining (joining) relative and absolute URL's (adding begining and end link)
  ad_link = urllib.parse.urljoin(startOfLink, endOfLink)


  # Printing each title and link on a new line
  print(f'{title}\n{ad_link}\n')

#images = soup.findAll('img', attrs={"id":"platop0"})


for image in soup.findAll('img', attrs={"id":"platop0"}):
  i = image['src']
  print(f'source : {i}')
 

#Rupees symbol encoding to UTF-8
  #sin =  soup.findAll('div',class_='e10twf T4OwTb')
  #print(sin)


