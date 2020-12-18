import requests
import bs4
import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import re

url='https://www.sanfoundry.com/computer-network-questions-answers/'


file=open('ask.dat','w+')

def gt(tu):
    ans=requests.get(tu)
    soup=bs4.BeautifulSoup(ans.text,'lxml')

    pos=soup.select('p:nth-of-type(n+2), [itemprop=\'text\'] div.collapseomatic_content')

    str1=''
    str2=''
    for i in pos:
        if i.text.find('View Answer')!=-1:
            print(i.text,file=file)
            print('$$$$',file=file)
        elif i.text.find('Answer: ')!=-1:
            print(i.text,file=file)
            print('####',file=file)

    



ans=requests.get(url)
t0=bs4.BeautifulSoup(ans.text,'lxml')
t=t0.select('td a')

# t=driver.find_elements_by_css_selector('td a')

for i in t:
    gt(i.get('href'))
    


# table_rows = t.find_elements_by_tag_name('tr')
# print(table_rows)



# ls=soup.find_all('a',href=re.compile('javascript:__doPostBack'))


# print(ans.text)