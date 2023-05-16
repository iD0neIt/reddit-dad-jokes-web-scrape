from selenium.webdriver.common.by import By

from locator.jokes_page_locator import JokesLocator
from parser.joke import JokeParser


class JokesPage:
    '''
    Class that returns a list of JokeParser objects for each joke on the page.
    '''
    def __init__(self, browser):
        self.browser = browser
    
    @property
    def jokes(self):
        '''
        Returns a list of JokeParser objects for each joke on the page.
        '''
        return [
            JokeParser(element)
            for element in self.browser.find_elements(
                By.CSS_SELECTOR, JokesLocator.JOKES
            )
        ]
    