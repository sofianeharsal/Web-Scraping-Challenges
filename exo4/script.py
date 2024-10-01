from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialisation du navigateur (mode visible pour voir le déroulement)
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Désactiver temporairement le mode headless pour tester
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Ouvrir le site web
url = "http://quotes.toscrape.com/scroll"
driver.get(url)

# Attendre que la première citation soit visible
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))

# Scroller pour charger plus de citations
SCROLL_PAUSE_TIME = 0.5  # Pause entre les scrolls
quote_count = 0

while True:
    # Extraire les citations déjà chargées
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    quotes = soup.find_all('div', class_='quote')  # S'assurer que c'est bien la classe 'quote'
    
    # Vérifier si de nouvelles citations ont été chargées
    new_quote_count = len(quotes)
    if new_quote_count == quote_count:
        break  # Si aucune nouvelle citation n'est chargée, on arrête
    quote_count = new_quote_count
    
    # Scroller jusqu'en bas de la page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Attendre que de nouvelles citations soient chargées
    time.sleep(SCROLL_PAUSE_TIME)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))

# Fermer le navigateur
driver.quit()

# Afficher le résultat
print(f"Nombre total de citations : {quote_count}")
