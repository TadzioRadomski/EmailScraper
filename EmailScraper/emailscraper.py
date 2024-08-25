import re
import requests
from bs4 import BeautifulSoup
from lxml import etree

website_list = open('WebsiteList.txt', 'r')

urls = website_list.read().splitlines()
website_list.close()

email_pattern = re.compile(r'^([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})')
all_emails = []

try:
    email_list = open('EmailList.txt', "x")
except FileExistsError:
    email_list = open('EmailList.txt', 'w+')
    email_list.truncate(0)

session = requests.Session()
for url in urls:
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'lxml')
    emails = soup.find_all(string=email_pattern)

    if emails == []: 
        print(f'No email found at: {url}')
        continue
    
    print(f'{len(emails)} email(s) found at {url}')
    for email in emails:
        print(f'    {email}')
        all_emails.append(email)
        email_list.write(f'{email}\n')

email_list.close()
