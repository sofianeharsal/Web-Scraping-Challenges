import requests
from bs4 import BeautifulSoup

# Fonction pour scraper une page et trouver les citations
def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            if author == "Albert Einstein" and "music" in tags:
                text = quote.find('span', class_='text').text
                print(f"Citation: {text}")
        return soup
    else:
        print("La requête a échoué avec le statut:", response.status_code)
        return None

# URL de la première page
base_url = "https://quotes.toscrape.com"
page_url = "/page/1/"

# Scraper les pages jusqu'à ce qu'il n'y ait plus de pages suivantes
while page_url:
    soup = scrape_page(base_url + page_url)
    next_button = soup.find('li', class_='next')
    page_url = next_button.find('a')['href'] if next_button else None
