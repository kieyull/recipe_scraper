"""
1. Take input
2. check that the url wasn't already scraped
2. determine domain
3. check if domain is in list of domains with specific rules
4. scrape site with specific rules || use generic rules (wordpress plugins, etc)
5. clean results
6. insert into database
"""
import sys
import lib.scraper as scraper
from peewee import *

mysql_db = MySQLDatabase('recipes', user='app', password='password',
                         host='localhost', port=3306)

# ingredient_list = dataToList(soup.find_all(class_="ingredients-item-name"))
# direction_list = dataToList(soup.find_all(class_="instructions-section-item"))

# # AllRecipes.com has advertising included in the first direction div
# direction_list[0] = direction_list[0].replace("Advertisement", "")

# Url examples
urls = [
    'https://www.thechunkychef.com/epic-dry-rubbed-baked-chicken-wings/',  # WP
    'https://www.allrecipes.com/recipe/276771/air-fryer-balsamic-glazed-chicken-wings/',
    'https://www.foodnetwork.com/recipes/ellie-krieger/greek-style-stuffed-peppers-recipe-1946946',
    'https://www.yummly.com/recipe/Crawfish-Etouffee-2670864',
    'https://www.epicurious.com/recipes/food/views/honey-mustard-sheet-pan-chicken-dinner-with-potatoes-and-greens',
    'https://tasty.co/recipe/spicy-cheesy-sausage-dip',
    'https://www.delish.com/holiday-recipes/christmas/a30222189/peppermint-bark-trifle-recipe/',
    'https://www.theguccha.com/bang-bang-cauliflower/',
    'https://www.skinnytaste.com/caramelized-onion-empanadas-chilean-pequenes/',
    'https://www.sproutedkitchen.com/home/2009/11/12/grape-salsa-on-goat-cheese-crostini.html',
]

if __name__ == '__main__':
    """
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        url = "https://www.allrecipes.com/recipe/276771/air-fryer-balsamic-glazed-chicken-wings/"
    """

    for url in urls:
        recipe_data = scraper.Scrape(url)
