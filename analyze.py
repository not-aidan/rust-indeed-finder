import os
from bs4 import BeautifulSoup

def read_file(file_path):
	with open(file_path, 'r') as f:
		return f.read()


def contains_word(string: str, word: str):
    for section in string.split(' '):
        for section in section.split('-'):
            if section.strip('.,?!:"\'') == word:
                return True
    return False

def contains_words(string: str, whitelisted: list[str] = [], blacklisted: list[str] = []):
    for word in whitelisted:
        if contains_word(string, word) == False:
            return False
    for word in blacklisted:
        if contains_word(string, word) == True:
            return False
    return True

def list_jobs(query: str, whitelistWords: list[str], blacklistWords: list[str] = []):
    os.chdir('data/' + query)
    jobs = 0
    # iterate through all file
    for file in os.listdir():
        # Check whether file is in text format or not
        #print(file);
        if file.endswith(".html"):
            soup = BeautifulSoup(read_file(file), 'html.parser')
            for card in soup.find_all("div", class_="job_seen_beacon"):
                htmlTitle = card.find("a", class_="jcs-JobTitle")
                title = htmlTitle.text.lower()
                link = 'https://www.indeed.com' + htmlTitle.get('href')
                is_rust = contains_words(title, whitelistWords, blacklistWords)
                descriptions = []
                ul = card.find("div", class_="job-snippet").ul
                if ul == None:
                    continue
                for description in ul.find_all("li"):
                    description = description.text.lower()
                    descriptions.append(description)
                    is_rust = is_rust or contains_words(description, whitelistWords, blacklistWords) 
                if is_rust:
                    print(title)
                    print(link)
                    for description in descriptions:
                        print(description)
                    print('\n')
                    jobs += 1
    print('found ' + str(jobs) + ' jobs')
    os.chdir('../../')

print('Finding all rust jobs')
blacklist = []
list_jobs('rust+developer', ['rust'], blacklist)
