# Projet de Web Scraping

Ce projet consiste à réaliser différents challenges de web scraping sur les sites [Books to Scrape](https://books.toscrape.com/) et [Quotes to Scrape](http://quotes.toscrape.com/). Le but est de collecter des informations à partir de plusieurs pages web et d'implémenter des fonctions permettant de répondre aux différentes questions ci-dessous.

## Défis

### 1. Nombre de livres et prix moyen par catégorie sur [Books to Scrape](https://books.toscrape.com/)

- Objectif : Scraper les données du site web pour obtenir le nombre de livres et le prix moyen de chaque catégorie.
- URL : `https://books.toscrape.com/`
- Méthode : Extraction des catégories de livres, puis collecte du nombre de livres et des prix dans chaque catégorie.

### 2. Authentification et scraping de [Quotes to Scrape](http://quotes.toscrape.com/login)

- Objectif : S'authentifier sur le site, puis effectuer le scraping après identification.
- URL : `http://quotes.toscrape.com/login`
- Méthode : Utilisation des informations d'identification pour se connecter et accéder au contenu sécurisé.

### 3. Nombre de pages sur [Quotes to Scrape](https://quotes.toscrape.com/)

- Objectif : Trouver combien de pages sont présentes sur le site.
- URL : `https://quotes.toscrape.com/`
- Méthode : Scraper les informations de pagination pour compter le nombre total de pages.

### 4. Nombre de citations sur [Quotes to Scrape - Infinite Scroll](http://quotes.toscrape.com/scroll)

- Objectif : Compter le nombre total de citations visibles via l'URL qui utilise le chargement dynamique.
- URL : `http://quotes.toscrape.com/scroll`
- Méthode : Gestion du chargement dynamique pour accéder à toutes les citations.

### 5. Première citation sur la page 10 de [Quotes to Scrape](https://quotes.toscrape.com/js/page/10/)

- Objectif : Récupérer la première citation présente sur cette page spécifique.
- URL : `https://quotes.toscrape.com/js/page/10/`
- Méthode : Accéder directement à la page et scraper la première citation affichée.

### 6. Cinquième citation sur la page 5 de [Quotes to Scrape](http://quotes.toscrape.com/js-delayed/page/5/)

- Objectif : Récupérer la cinquième citation sur la page mentionnée.
- URL : `http://quotes.toscrape.com/js-delayed/page/5/`
- Méthode : Gestion du délai de chargement pour accéder aux citations après le rendu complet de la page.

### 7. Tag le plus répétitif sur [Quotes to Scrape - Tableful](http://quotes.toscrape.com/tableful/)

- Objectif : Identifier le tag qui apparaît le plus souvent sur cette page.
- URL : `http://quotes.toscrape.com/tableful/`
- Méthode : Scraper tous les tags disponibles et analyser leur fréquence d'apparition.

### 8. Citation d'Albert Einstein sur la musique via [Quotes to Scrape - Filter](http://quotes.toscrape.com/filter.aspx)

- Objectif : Trouver la seule citation d'Albert Einstein qui mentionne la musique.
- URL : `http://quotes.toscrape.com/filter.aspx`
- Méthode : Utiliser le formulaire pour filtrer les résultats et récupérer la citation recherchée.

### 9. Temps estimé pour scraper le site [Quotes to Scrape - Random](http://quotes.toscrape.com/random)

- Objectif : Estimer le temps nécessaire pour scraper l'intégralité du contenu de ce site web aléatoire.
- URL : `http://quotes.toscrape.com/random`
- Méthode : Calculer un temps approximatif en fonction du nombre de pages et de citations à récupérer.

## Technologies utilisées

- Python
- Bibliothèques : `BeautifulSoup`, `requests`, `Selenium` (pour la gestion des contenus dynamiques et authentification)
- Gestion des données : `Pandas`

