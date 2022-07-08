import os
from bs4 import BeautifulSoup
import re
import pandas as pd
from slugify import slugify

os.chdir('d:\\Desktop\\treports')
# get a list of the files in the current directory
here = os.listdir(os.getcwd())

def preproc(infile):

    try:
    # open the infile for reading
        file = open(infile, 'r')
        fileName = os.path.splitext(infile)[0]

        # convert the contents of the infile to a Beautiful Soup object
        soup = BeautifulSoup(file, 'html.parser')
        # soup = soup.findAll('table')
        report = soup.find('table', {'border': '0', 'cellpadding': '0', 'cellspacing': '0', 'vspace': '0', 'hspace': '0', 'width': '100%'})
        report_title = report.find('font').text
        print report_title



        # # Find deck title
        # for item in soup:
        #     report_title = item.findAll('tr')
        #     report_title = report_title.find('font', {'bgcolor': "#000000"}).get_text()
        #     print report_title
        # report_title = report_title.encode('UTF-8', 'backslashreplace').replace(':', '').replace('!', '').replace('<', '').replace('>', '')
        # report_title = report_title.replace("'", " ").replace("?", "").replace("!", "").replace("*", "").replace(",", " ").replace(".", " ")
        # # print report_title
        # # Find author
        # author_element = soup.findAll('font', {'class': 'h2font'})
        # author =  author_element[1].find('a').text
        # date = author_element[2].text.replace('Date Submitted: ', '')
        #
        # report = soup.select('blockquote')
        # # print report
        #
        # print report
        # with open(pd.to_datetime(date).strftime("%Y-%m-%d") + '-' + slugify(report_title) + fileName + '.txt', 'a') as output:
        #     output.write('---' + '\n')
        #     output.write('layout: tr' + '\n')
        #     output.write('author: ! ' + author.encode('UTF-8').replace(':', '') + '\n')
        #     output.write('title: ! ' + slugify(report_title) + '\n')
        #     output.write('tags:\n' + '- ' +'Tournament_Report' + '\n')
        #     output.write('date: ' + pd.to_datetime(date).strftime("%Y-%m-%d") + '\n')
        #     output.write('---' + '\n' + str(report[0]))

    except:
        print "error " + fileName


fileName = 0
# for i in here:
#     print i
#     preproc(i)

preproc(here[1])