import requests
from bs4 import BeautifulSoup

# URL de base du site
base_url = 'http://quotes.toscrape.com/page/'

def get_total_pages():
    # Commence par la première page
    page_num = 1
    while True:
        url = f"{base_url}{page_num}/"
        response = requests.get(url)
        
        # Si on arrive sur une page qui n'existe pas, on s'arrête
        if response.status_code != 200:
            break
        
        # Analyse la page avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Cherche l'élément indiquant que la page est vide (si nécessaire)
        if not soup.find_all("div", class_="quote"):
            break

        page_num += 1
    
    # Le numéro de page en cours est la première page inexistante, donc on retourne page_num - 1
    return page_num - 1

total_pages = get_total_pages()
print(f"Nombre total de pages : {total_pages}")
