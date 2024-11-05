
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
from session import add_series

base_url = 'https://www.awafim.tv/browse?q=&type=series&genre%5B%5D=Action&genre%5B%5D=Adventure&genre%5B%5D=Comedy&genre%5B%5D=Crime&genre%5B%5D=Thriller&genre%5B%5D=War&genre%5B%5D=Western'
def scrape_page(page_number):
    url = base_url + str(page_number)
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_number}")
        return False  
    
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article', {'class': 'titles-one'})
    if not articles:
        print(f"No more articles found on page {page_number}")
        return False

    for data in articles:
        try:
            head = data.find('h3', {'class': 'to-h3'})
            f_head = head.text.strip() if head else 'N/A'
            
            date = data.find('div', {'class': 'toi-year'})
            f_date = date.text.strip() if date else 'N/A'
            
            season = data.find('div', {'class': 'toi-run'})
            f_season = season.text.strip() if season else 'N/A'
            
            link_tag = data.find('a')
            link = urljoin(base_url, link_tag['href']) if link_tag else 'N/A'
            
            country = 'N/A'  
            
            image = data.find('img', {'class': 'to-thumb'})
            f_image = image.get('src') if image else 'N/A'
            
            rating = data.find('span', {'class': 'stars-list'})
            f_rating = rating.get('title') if rating else 'N/A'
            
            add_series(f_head, f_date, f_season, link, country, f_image, f_rating)
            
            print(f"Title: {f_head}\nDate: {f_date}\nSeason: {f_season}\nLink: {link}\nImage: {f_image}\nRating: {f_rating}\n")
        except Exception as e:
            print(f"An error occurred while processing an article on page {page_number}: {e}")

    return True 

def main():
    page_number = 1
    while scrape_page(page_number):
        print(f"Scraped page {page_number}")
        page_number += 1
        time.sleep(1)  

if __name__ == "__main__":
    main()
