# first attempt at web scraper for DSSG - 1/7/2016
# using BS4 and requests
# guide 1: http://journalistsresource.org/tip-sheets/research/python-scrape-website-data-criminal-justice
# guide 2: http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python

import requests
from bs4 import BeautifulSoup
import time

url_scraped = 'http://www.jobaps.com/sf/default.asp#JobListing'

r = requests.get(url_scraped)
# print(r.text)

soup = BeautifulSoup(r.text)
# OR (r.content) ? (r.text) may not always work [what is parsing]
# print(len(soup.select('#JobListing tr')[2:]))


sfgov_job_listings = []

for list_item in soup.select("#JobListing tr")[2:]:
    # print(list_item['class'])
        # in HTML, # is table, . is list

    # if list_item['class'] == ['ColumnHeader']:
    #     # print(list_item)
    #     continue

    if list_item['class'] == ['RowHeader']:
        continue

    # print(list_item)

    list_cells = list(list_item.children)

    # print(list(list_item.children)[1])
    # print(list(list_item.children)[2])
    # print(list(list_item.children)[3])

    job_title = list(list_cells[1].children)[0].text
    dept = list_cells[3].string
# not .text

    print(job_title)
    print(dept)

    # dept = list(list_item.children)[2]

#    list_cells = list_item.findAll('td')
# # maybe wrong here? not sure what the soup.select pulls, but html here is odd/even, almost like overlaying structure is tr
# # maybe use table_id instead? table_id is 'JobListing'
#
#     if len(list_cells) > 0:
#         relative_link_to_sfgov_joblinks = list_cells[0].find('a')['href']
#         absolute_link_to_sfgov_joblinks = url_to_scrape + relative_link_to_sfgov_joblinks
#         sfgov_job_listings.append(absolute_link_to_sfgov_joblinks)
#
# sfgov_jobs = []
#
# for sfgov_vidslinks[:10]:
#     # don't understand the [:10]:...
#     r = requests.get(sfgov_vidslinks)
#     soup = BeautifulSoup(r.text)
#
#     sfgov_details = {}






