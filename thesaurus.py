# from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests


def getSynonyms(word, numResults):
    data = requests.get("https://www.thesaurus.com/browse/" + word.lower())
    soup = BeautifulSoup(data.text, 'html.parser')
    div = soup.find('ul', {'class' : 'css-1lc0dpe et6tpn80'})
    counter = 0
    for li in div.find_all('li'):
        if(counter>=int(numResults)):
            break
        else:
            counter += 1
            print(li.text)
    print()
    print("Finished")

inputWord = input("What word do you want to synonomize?  ")
numOfResults = input("How many Synonyms do you want?  ")
getSynonyms(inputWord, numOfResults)
# ThesaurusBot("happy")
