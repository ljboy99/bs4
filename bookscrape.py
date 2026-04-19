import requests 
from bs4 import BeautifulSoup
import csv
import time

#initial code by CLAUDE AI
#annotations and edits made for my own learning purposes

page = 1; book_data = []; books_scraped = 1

if __name__ == "__main__":

    #This will repeat the following lines until page is greater than 50
    while page <= 50:
        print(f'Scraping page: {page}')
        #define the URL we are going to have requests navigate to
        url = f'https://books.toscrape.com/catalogue/page-{page}.html'
        #define the response of the URL get request
        response = requests.get(url)
        #parse contents of the URL get request
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        #print(url)
        for book in books:
            title = book.find('h3').find('a')['title']
            #pull the price info and strip the whitespace from both sides
            price = book.find('p', class_='price_color').get_text()#.strip()
            availability = book.find('p', class_='instock availability').get_text()
            rating_class = book.find('p', class_='star-rating')['class']
            rating = rating_class[-1]

            #add the data we pulled from the site to the book_data dict
            book_data.append({
                'title': title,
                'price': price.strip(),
                #strip the whitespace from both sides of the availability when adding to the dict
                'availability': availability.strip(),
                'rating': rating
            })

            print(f"{title} added")
            #print(books_scraped)
            #I wanted to pace the scraping more
            #time.sleep(0.05)
            books_scraped += 1
            #every time we scrape 20 books, we will navigate to the next page
            if books_scraped % 20 == 0:
                #navigate to next page by adding to page count in the URL
                page += 1

    #open books.csv to write to the file
    with open('books.csv', 'w', newline='', encoding='utf-8') as f:
        #define header fieldnames for the csv
        writer = csv.DictWriter(f, fieldnames=['title', 'price', 'availability', 'rating'])
        #write defined headers to the CSV header row
        writer.writeheader()
        #write the data we scraped to the csv to the defined columnsz
        writer.writerows(book_data)

    print(f"\nScraped {len(book_data)} books --> books.csv")