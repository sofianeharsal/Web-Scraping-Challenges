from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configurer les options pour exécuter Chrome en mode headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Exécuter en mode headless
chrome_options.add_argument("--no-sandbox")  # Option pour des raisons de sécurité
chrome_options.add_argument("--disable-dev-shm-usage")  # Pour éviter les problèmes de mémoire

# Créer un service Chrome
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL de la page à scraper
url = 'https://quotes.toscrape.com/'

# Ouvrir la page
driver.get(url)

# Attendre que le contenu soit chargé
time.sleep(2)  # Ajuste ce délai si nécessaire

# Trouver la cinquième citation
fifth_quote_element = driver.find_elements(By.CSS_SELECTOR, 'div.quote span.text')[4]
fifth_quote = fifth_quote_element.text

# Afficher la cinquième citation
print('Cinquième citation:', fifth_quote)

# Fermer le navigateur
driver.quit()
