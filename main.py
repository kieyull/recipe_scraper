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
import scraper.scraper as scraper

if __name__ == '__main__':
	if len(sys.argv) == 2:
		url = sys.argv[1]
	else:
		url = "https://www.allrecipes.com/recipe/276771/air-fryer-balsamic-glazed-chicken-wings/"
	
	recipe_data = scraper.Scraper(url)
