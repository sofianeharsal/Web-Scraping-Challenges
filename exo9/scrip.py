import requests
from bs4 import BeautifulSoup
import time

# URL de base
base_url = "http://quotes.toscrape.com"

# Fonction pour scraper une page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.select('div.quote')
    return quotes

# Nombre total de pages
total_pages = 10

# Mesurer le temps moyen pour scraper une page
start_time = time.time()
scrape_page(f"{base_url}/page/1/")
end_time = time.time()
average_time_per_page = end_time - start_time

# Calculer le temps total estimé
total_time = total_pages * average_time_per_page

print(f"Nombre total de pages: {total_pages}")
print(f"Temps moyen pour scraper une page: {average_time_per_page:.2f} secondes")
print(f"Temps total estimé pour scraper tout le site: {total_time:.2f} secondes")
