import requests, lxml, urllib.parse, sys
from bs4 import BeautifulSoup

# Adding User-agent (default user-agent from requests library is 'python-requests')
# https://github.com/psf/requests/blob/589c4547338b592b1fb77c65663d8aa6fbb7e38b/requests/utils.py#L808-L814
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

# Search query
params = {'q': 'phone buy'}

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
  #response = requests.get("data:image/png;base64,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")
  #file = open("sample_image.png", "wb")
  #file.write(response.content)
  #file.close()

#Rupees symbol encoding to UTF-8
  #sin =  soup.findAll('div',class_='e10twf T4OwTb')
  #print(sin)


