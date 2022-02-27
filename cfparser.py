#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup
from cf.util import *
from cf.classes import *

import textwrap
import pydoc
import sys

from pylatexenc.latex2text import LatexNodes2Text

def prob_stat(num, ind):
    url = "https://codeforces.com/problemset/problem/"+str(num)+"/"+str(ind)
    # print(url)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    pstate = soup.find('div', attrs={'class':'problem-statement'})
    header = pstate('div', attrs={'class':'header'})
    title = header[0]('div', attrs={'class':'title'})[0].get_text()
    time_limit = header[0]('div', attrs={'class':'time-limit'})[0].get_text()[19:]
    mem_limit = header[0]('div', attrs={'class':'memory-limit'})[0].get_text()[21:]

    statement = pstate('div')[10](['p', 'li'])
    state = []
    for s in statement:
        state.append(s.get_text().replace('$$$', ''))

    input_spec = pstate('div', {'class':'input-specification'})[0](['p', 'li'])
    input_s = []
    for s in input_spec:
        input_s.append(s.get_text().replace('$$$', ''))
    output_spec = pstate('div', {'class':'output-specification'})[0](['p', 'li'])
    output_s = []
    for s in output_spec:
        output_s.append(s.get_text().replace('$$$', ''))

    sample_test = pstate('div', {'class':'sample-test'})[0]
    sample_test_i = sample_test('div', {'class':'input'})
    sample_test_o = sample_test('div', {'class':'output'})
    sti = []
    sto = []
    for s in sample_test_i:
        sti.append(s.get_text().replace('Input',''))
    for s in sample_test_o:
        sto.append(s.get_text().replace('Output',''))

    tab = '    '

    paged = '\n'
    paged += get_colored(tab+title, "blue")+"\n"
    paged += get_colored(tab+"Time: ",'blue')+get_colored(time_limit, color='magenta')+"\n"
    paged += get_colored(tab+"Memory: ",'blue')+get_colored(mem_limit, color='magenta')+"\n\n\n"

    paged += get_colored(tab+"Problem Statement:\n", 'blue')+"\n"
    for s in state:
        paged += get_colored(tab+"".join(textwrap.wrap(s, 150))+"\n")+"\n"

    paged += get_colored(tab+"Input:\n", 'blue')+"\n"
    for s in input_s:
        paged += get_colored(tab+"".join(textwrap.wrap(s, 150))+"\n")+"\n"

    paged += get_colored(tab+"Output:\n", 'blue')+"\n"
    for s in output_s:
        paged += get_colored(tab+"\n\t".join(textwrap.wrap(s, 150))+"\n")+"\n"

    for i in range(len(sti)):
        paged += get_colored(tab+"Sample Input "+str(i)+":", 'blue')+"\n"
        paged += get_colored(tab+sti[i].replace('\n', '\n\t '), 'cyan')+"\n"
        paged += get_colored(tab+"Sample Output "+str(i)+":", 'blue')+"\n"
        paged += get_colored(tab+sto[i].replace('\n', '\n\t '), 'green')+"\n"

    # print(paged)

    print(LatexNodes2Text().latex_to_text(paged))

    # pydoc.pager(paged)



prob_stat(sys.argv[1], sys.argv[2])
