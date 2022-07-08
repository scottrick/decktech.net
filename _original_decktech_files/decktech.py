import os
from bs4 import BeautifulSoup
import re
import pandas as pd

os.chdir('d:\\Desktop\\decktech_archives\\decktech\\swccg\\decks\\dark')
# get a list of the files in the current directory
here = os.listdir(os.getcwd())

def preproc(infile):

    try:
    # open the infile for reading
        file = open(infile, 'r')
        fileName = os.path.splitext(infile)[0]

        # convert the contents of the infile to a Beautiful Soup object
        soup = BeautifulSoup(file, 'html.parser')

        # Find deck title
        deck_title = soup.find('font', {'face':'Haettenschweiler, Tahoma, Arial'}).get_text()
        deck_title = deck_title.encode('UTF-8', 'backslashreplace').replace(':', '').replace('!', '').replace('<', '').replace('>', '')
        deck_title = deck_title.replace("'", " ").replace("?", "").replace("!", "").replace("*", "").replace(",", " ").replace(".", " ")
        # Find author
        author_element = soup.find('td', text="Author")
        for c in author_element.parent.select("td:nth-of-type(2)"):
            author = c.text

        #Find date created
        date_element = soup.find('td', text="Date Created")
        for b in date_element.parent.select("td:nth-of-type(2)"):
            date = b.text
            date = pd.to_datetime(date).strftime("%Y-%m-%d")

        #Find description
        description_element = soup.find('td', text="Description")
        for g in description_element.parent.select("td:nth-of-type(2)"):
            description = g.text
            # print description.replace('\r', '').replace('\n', '').replace('!', '')
            description = description.encode('UTF-8', 'backslashreplace').replace('\n', '').replace('*', '').replace('!', '').replace('"', '')

        #Find rating
        ratingElement = soup.find('td', text="Rating")
        rating = ratingElement.parent.find('img')['src']
        rating = re.sub("../images/dd", "", str(rating))
        rating = re.sub("\.GIF", "", rating)
        rating = float(int(rating))/2

        # Find cards
        cardsElement = soup.find('td', text="Cards")
        for a in cardsElement.parent.select("td:nth-of-type(2)"):
            cards = a.find('font').text
            cards = cards.replace('*', '').replace('!', '').replace(':', '').replace('<>', '')

        # Find strategy
        strategyElement = soup.find('td', text="Strategy")
        for m in strategyElement.parent.select("td:nth-of-type(2)"):
            strategy = m.find('font').text
            strategy = strategy.replace(':', '').replace('!', '')

        with open(date + '-' + fileName + '.txt', 'a') as output:
            output.write('---' + '\n')
            output.write('layout: post' + '\n')
            output.write('author: ! ' + author.encode('UTF-8', 'ignore').replace(':', '') + '\n')
            output.write('title: ! ' + '"' + deck_title + '"' + '\n')
            output.write('tags:\n' + '- ' +'Dark' + '\n')
            output.write('date: ' + date + '\n')
            output.write('description: ! ' +'"' + str(description).replace('\r', '') + '"' + '\n')
            output.write('rating: ' + str(rating) + '\n')
            output.write('---' + '\n' + 'Cards: ' + '\n' + '\n' + "'" + cards.encode("UTF-8", 'ignore') + "'" + '\n' + '\n' + 'Strategy: ' + "'" + '\n' + '\n' + strategy.encode("UTF-8", 'ignore') + "'")

    except:
        print "error " + fileName


fileName = 0
for i in here:
    preproc(i)