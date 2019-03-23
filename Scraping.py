import requests
from bs4 import BeautifulSoup
import csv
import re

page = requests.get("https://www.the-numbers.com/market/2018/top-grossing-movies")

#print(page) #Response code contatins the status code

#print(page.status_code) #this also prints the status code, a 200 code means that the page downloaded successfully

#print(page.content) #prints the html content CAUTION: HEAVY!

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify()) #prints the page in a formatted nicely manner

##chlist = list(soup.children) #gives the list of children tags in the page

##chlisttypes = [type(item) for item in list(soup.children)] #gives the object type of the contents

##html = list(soup.children)[2] #selecting the third item on the list, html tag and its children

##chhtml = html.children

tabledata = soup.find_all('tr')

max = len(tabledata) - 2

movie = list(tabledata[2])

movie_num = list(movie)[1].get_text()

movie_name = list(movie)[3].get_text()

movie_reldate = list(movie)[5].get_text()

movie_distr = list(movie)[7].get_text()

movie_genre = list(movie)[9].get_text()

movie_boxoffice = list(movie)[11].get_text()

movie_ticketsold = list(movie)[13].get_text()

#print(movie_num, movie_name, movie_reldate, movie_distr, movie_genre, movie_boxoffice, movie_ticketsold)
csvData = list()
for num in range(1,max) :
    movie = list(tabledata[num])
    movie_num = list(movie)[1].get_text()
    movie_name = list(movie)[3].get_text()
    movie_reldate = list(movie)[5].get_text()
    movie_distr = list(movie)[7].get_text()
    movie_genre = list(movie)[9].get_text()
    movie_boxoffice = list(movie)[11].get_text()
    movie_ticketsold = list(movie)[13].get_text()
    csvData.append([movie_num, movie_name, movie_reldate, movie_distr, movie_genre, movie_boxoffice, movie_ticketsold])
    #print(movie_num, movie_name, movie_reldate, movie_distr, movie_genre, movie_boxoffice, movie_ticketsold)


print(csvData)
with open('moviegross2018.csv', 'w', encoding = "utf-8") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()

##with open('moviegross2018.txt', 'w', encoding = "utf-8") as txtFile:
##    for item in csvData :
##        for inneritem in item :
##            k = re.sub("\[","",inneritem)
##            k = re.sub("\]","",inneritem)
##            txtFile.write("%s;"%k)
##        txtFile.write("\n")
##txtFile.close()
