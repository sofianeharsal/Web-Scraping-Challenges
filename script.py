import requests
from bs4 import BeautifulSoup

# URL de login et URL de la page des citations
login_url = 'http://quotes.toscrape.com/login'
quotes_url = 'http://quotes.toscrape.com/'

# Création d'une session pour maintenir les cookies
session = requests.Session()

# Étape 1: Charger la page de login pour obtenir le token CSRF
response = session.get(login_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extraire le token CSRF (caché dans un champ input)
csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

# Étape 2: Soumettre le formulaire de login avec les informations d'identification
login_data = {
    'csrf_token': csrf_token,
    'username': 'votre_nom_utilisateur',  # Remplacez par votre nom d'utilisateur
    'password': 'votre_mot_de_passe'  # Remplacez par votre mot de passe
}

# Soumettre le formulaire
session.post(login_url, data=login_data)

# Étape 3: Accéder à la page des citations après authentification
response = session.get(quotes_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Scraper les citations
quotes = soup.find_all('span', class_='text')

# Afficher les citations
for quote in quotes:
    print(quote.text)
