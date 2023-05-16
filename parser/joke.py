from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from locator.joke_locator import JokeLocator


class JokeParser:
    '''
    Class that extracts the start and punchline of a joke.
    '''
    def __init__(self, parent):
        self.parent = parent

    @property
    def start(self):
        '''
        Returns the start of a joke.
        '''
        locator = JokeLocator.JOKE_START_LOCATOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def punchline(self):
        '''
        Returns the punchline of a joke.
        '''
        locator = JokeLocator.JOKE_PUNCHLINE_LOCATOR
        try:
            punchline = self.parent.find_elements(By.CSS_SELECTOR, locator)
        except NoSuchElementException:
            return None
        else:
            return '\n'.join(line.text for line in punchline) 
  