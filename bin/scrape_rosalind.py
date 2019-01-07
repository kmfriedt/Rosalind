from bs4 import BeautifulSoup
import urllib
import os
import re

list_view = urllib.urlopen('http://rosalind.info/problems/list-view/').read()
list_view_soup = BeautifulSoup(list_view)

fname = 'index.html'
f = open(fname, 'w+')

r = BeautifulSoup(re.sub('/problems/(.*)/', './problems/\\1.html', list_view_soup.prettify()))
f.write(r.prettify().encode("utf-8"))

accessible_problems = list_view_soup.find_all("a", class_="accessible")
inaccessible_problems = list_view_soup.find_all("a", class_="not-accessible")

problem_links = [p["href"] for p in inaccessible_problems + accessible_problems] # they look like /problems/<problem_name>

problems = []
for link in problem_links:
    problems.append({ "link": link, "source": BeautifulSoup(urllib.urlopen('http://rosalind.info' + link).read()) })

for p in problems:
    fname = p["link"].split('/')[2] + '.html'
    f = open('problems/' + fname, 'w+')
    f.write(p["source"].prettify().encode("utf-8"))
    f.close()

