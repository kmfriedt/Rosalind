from bs4 import BeautifulSoup
import urllib.request
import os
import re
"""
You should run this script from the project root.
Because I'm lazy, this script won't create the appropriate folders for you.
Therefore, ensure that you have the following filestructure:
$ROOT 
-- website
   -- problems

(The required filestructure may change if the website is updated)
"""


list_view = urllib.request.urlopen('http://rosalind.info/problems/list-view/').read()
list_view_soup = BeautifulSoup(list_view, "html.parser")

fname = 'website/index.html'
f = open(fname, 'w+')

r = BeautifulSoup(re.sub('/problems/(.*)/', './problems/\\1.html', list_view_soup.prettify()), "html.parser")
f.write(r.prettify())

accessible_problems = list_view_soup.find_all("a", class_="accessible")
inaccessible_problems = list_view_soup.find_all("a", class_="not-accessible")

problem_links = [p["href"] for p in inaccessible_problems + accessible_problems] # they look like /problems/<problem_name>

problems = []
for link in problem_links:
    source = BeautifulSoup(urllib.request.urlopen(f'http://rosalind.info{link}').read(), "html.parser")
    problems.append({ "link": link, "source": source })

for p in problems:
    fname = p["link"].split('/')[2] + '.html'
    f = open(f'website/problems/{fname}', 'w+')
    f.write(p["source"].prettify())
    f.close()

