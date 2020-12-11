import sys
import re
import requests
from bs4 import BeautifulSoup


def dataToList(data):
	return [re.sub(r"\s\s+", " ", i.text).strip().rstrip() for i in data]


def getTitle(dom):
	# Clean up the Allrecipes style title
	return dom.title.text.replace(" | Allrecipes", "").replace("Recipe", "").strip()


if __name__ == '__main__':
	if len(sys.argv) == 2:
		url = sys.argv[1]
	else:
		url = "https://www.allrecipes.com/recipe/276771/air-fryer-balsamic-glazed-chicken-wings/"

	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	recipe_title = getTitle(soup)
	ingredient_list = dataToList(soup.find_all(class_="ingredients-item-name"))
	direction_list = dataToList(soup.find_all(class_="instructions-section-item"))

	# AllRecipes.com has advertising included in the first direction div
	direction_list[0] = direction_list[0].replace("Advertisement", "")

	# Print recipe to console
	print("\n", recipe_title)
	print("_" * len(recipe_title))
	print("Ingredients\n")
	for ingredient in ingredient_list:
		print("  * ", ingredient, "\n")

	print("Directions\n")
	for direction in direction_list:
		print("  ", direction, "\n")
