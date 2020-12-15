import sys
import re
import bs4
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class Scrape:
    """ Base class to be extended and used for other domains

    This class grabs a domain and pulls in the html. 
    It then parses through the html for specific tags
    and determins what to scrape.`
    The scraped object can then be manipulated as needed.
    """

    def __init__(self, url: str) -> None:
        self.url = url
        self.html = requests.get(url).content
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.domain = self.getDomain(url)
        self.title = self.getTitle(self.soup)
        self.ingredients = []
        self.directions = []

    def getTitle(self, dom: bs4.element.ResultSet) -> str:
        """ Removes the domain name from the title as well as 'Recipe if it's there """
        delineators = [" by ", " | ", " - ", " – ", " — "]
        title = dom.title.text
        for delineator in delineators:
            title = title.split(delineator)[0]

        return title.lower().replace("recipe", "").title().strip()

    def dataToList(self, data: bs4.element.ResultSet) -> list:
        """ Takes a ResultSet from BeautifulSoup and turns it into a list of strings """
        return [re.sub(r"\s\s+", " ", i.text).strip().rstrip() for i in data]

    def getDomain(self, url: str) -> str:
        """ Takes the full url and returns just the domain name with no subdomain """
        return '.'.join(urlparse(self.url).netloc.split('.')[1:])
