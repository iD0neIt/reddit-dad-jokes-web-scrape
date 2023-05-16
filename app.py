import time
import datetime
import calendar
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from page.jokes_page import JokesPage

# configure chrome browser
options = webdriver.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('--log-level=3')
chrome = webdriver.Chrome(
    options=options, 
    service=ChromeService(
        ChromeDriverManager().install()
    )
)

# open web page
chrome.get('https://www.reddit.com/r/dadjokes/')

# create the JokesPage object 
page = JokesPage(chrome)

# get the initial number of jokes
initial_number_of_jokes = len(page.jokes)

# determine the number of days in current year
current_year = datetime.date.today().year
number_of_days_in_current_year = 366 if calendar.isleap(current_year) else 365

jokes = []

# keep scrolling down and add the jokes to the jokes list 
start = 0
while len(jokes) < number_of_days_in_current_year:
    for joke in page.jokes[start:]:
        joke_string = f'{joke.start}\n{joke.punchline.rstrip()}'
        if joke.punchline:
            if len(jokes) == number_of_days_in_current_year:
                break
            print(joke_string)
            jokes.append(joke_string)
    
    start = initial_number_of_jokes

    chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    jokes_found = len(page.jokes)
    initial_number_of_jokes = jokes_found

# close browser
chrome.quit()

# write the jokes to a txt file
file = 'reddit-dad-jokes.txt'
with open(file, 'w', encoding='utf-8') as fp:
    title = 'REDDIT DAD JOKES'
    fp.write(f'{title.center(140)}')
    fp.write('\n')
    fp.write('\n')
    for index, joke in enumerate(jokes):
        fp.write(f'\n[{index + 1}]\n')
        fp.write(f'{joke}\n')
