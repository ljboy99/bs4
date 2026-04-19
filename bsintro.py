import requests
from bs4 import BeautifulSoup 

#give the requests library a user agent to describe itself as for the website. 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
#define a url for requests lib to navigate to
url = 'https://beautiful-soup-4.readthedocs.io/en/latest/'
#have the requests library send a HTTP get request to the URL
response = requests.get(url, headers=headers)

#if-else statement based on URL response
if response.status_code == 200:
    #pass the context as text into a variable
    html_content = response.text

else: 
    #if URL response is a failure, notify console
    print(f"failed: {response.status_code}")

#BS will use pythons built in parser to parse the content.
soup = BeautifulSoup(html_content, 'html.parser')
#increase readibility with .prettify()
#print(soup.prettify())


#paragraphs = soup.find_all('p')
#for p in paragraphs:
#    print(p.get_text())

#title = soup.find('h1').get_text()

#button = soup.find('button', class_='primary')
#sidebar = soup.find('div', id='sidebar')


def get_links():
    #grab all <a> tags, commonly used for hyperlinks.
    links = soup.find_all('a')
    for link in links:
        #grab all of the tags that are 'href' / hyperlinks
        href = link['href']
        #convert links to text.
        text = link.get_text()
        #if the text 'name' appears in text. print it and it's corresponding hyperlink.
        if 'name' in text:
            print(f'{text} -> {href}')

def get_images():
    images = soup.find_all('img')
    for img in images:
        src = img['src']
        alt = img.get('alt', 'no alt text')

get_links()
#get_images()