from selenium import webdriver
import math
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


options = Options()
#options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options)

def getIndeedPage(query, page):
    url = 'https://www.indeed.com/jobs?q=' + query + '&start=' + str(page * 10) + '&filter=0'


    print(url)
    driver.get(url)
    with open('data/out-' + query + '-pg' + str(page) + '.html', 'w') as f:
        f.write(driver.page_source)
        return driver.page_source

query = 'rust+developer'
results = int(BeautifulSoup(getIndeedPage(query, 0), 'html.parser').find(
        'div',
        class_='jobsearch-JobCountAndSortPane-jobCount').find('span').text.split(' ')[0].replace(',', ''))
print(str(results) + ' jobs found')
for x in range(math.ceil(results / 15)):
    source = getIndeedPage('rust+developer', x)
    soup = BeautifulSoup(source, 'html.parser')
