"""
---------------------
Scrapes book titles, prices, and ratings from books.toscrape.com
 and saves the results to a CSV file.
 
Libraries used:
    requests        -> fetch raw HTML from a page
    BeautifulSoup   -> parse HTML and pull out the data we want
    csv             -> write the extracted data to a .csv file
"""



import csv
import time
import requests
from bs4 import BeautifulSoup

base_url="https://books.toscrape.com/catalogue/page-{}.html"
headers={

    "User-Agent":(
        "Mozilla/5.0(Windows NT 10.0;Win64;x64)"
        "AppleWebKit/537.36(KHTML,like Gecko) Chrome/124 Safari/537.36"
    )
}

ratewords={"One":1,"Two":2,"Three":3,"Four":4,"Five":5}

def get_pagehtml(page_no:int)->str:
    """
    Fetch the raw HTML for a given catalogue page no.
    """
    url= base_url.format(page_no)
    response=requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text

def parse_books(html:str)->list[dict]:

    """Parsen a page's html and return a list of book dicts. """

    soup=BeautifulSoup(html,"html.parser")
    books=[]

    for article in soup.select("article.product_pod"):
        title=article.h3.a["title"].strip()

        price_text=article.select_one("p.price_color").get_text(strip=True)
        price=float(price_text.replace("£","").replace("Â", ""))
        
        availability=article.select_one("p.instock.availability").get_text(strip=True)

        rating_class=article.select_one("p.star-rating")["class"]

        rating_word=[c for c in rating_class if c!="star-rating"][0]
        rating=ratewords.get(rating_word,0)

        books.append(
            {
                "title": title,
                "price_gbp":price,
                "availability":availability,
                "rating_out_of_5":rating,
            }
        )

        return books
    

def scrape_all_pages(max_pages:int=5)-> list[dict]:
    all_books=[]
    for page in range(1,max_pages+1):
        print(f"Scrapping page{page}.....")

        try:
            html=get_pagehtml(page)
        except requests.exceptions.HTTPError:

            print("No more pages found. Stopping.")
            break
        books_on_page=parse_books(html)
        all_books.extend(books_on_page)

        time.sleep(1)

    return all_books


def save_to_csv(books:list[dict],filename:str="books_scrapped.csv")->None:

    """Write the list of books to the CSV file."""

    if not books:
        print("No data to save")
        return
    fieldnames=books[0].keys()
    with open(filename,mode="w",newline="",encoding="utf-8")as f:
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


    print(f"Saved {len(books)} records to {filename}")


    
if __name__ == "__main__":
    scraped_books=scrape_all_pages(max_pages=7)
    save_to_csv(scraped_books,"books_scraped.csv")



