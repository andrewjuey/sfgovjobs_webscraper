# 1/16/2016
# using BS4, requests
# general guide: http://journalistsresource.org/tip-sheets/research/python-scrape-website-data-criminal-justice

import requests
from bs4 import BeautifulSoup


def get_crawled_data():
    data = []

    # Load HTML into memory
    url_scraped = 'http://www.jobaps.com/sf/default.asp#JobListing'
    html = requests.get(url_scraped)

    # Convert HTML into tree
    tree = BeautifulSoup(html.text)

    # Find job listings
    # TODO: Document the HTML structure you are extracting
    table = tree.select("#JobListing tr")
    # skip first two rows
    rows = table[2:]
    for row in rows:
        # Skip section headers
        if row['class'] == ['RowHeader']:
            continue

        # Get cells of data in each job row
        cells = list(row.children)

        job_title_cell = cells[1]
        job_title_cell_text_sections = list(job_title_cell.children)
        job_title = job_title_cell_text_sections[0].text
        job_code = job_title_cell_text_sections[2].text

        dept = str(cells[3].string)

        salary_ranges_text = str(cells[5].string).strip()
        salary_ranges = salary_ranges_text.split('; ')
        for salary_range_text in salary_ranges:
            if salary_range_text[-5:] == '/year':
                salary_range = salary_range_text[:-5]
                print(salary_range)

        data.append({
            'title': job_title,
            'dept': dept,
            'salary': salary_range
        })

    return data


def get_analysis(data):
    analysis = {}

    analysis['num_total'] = len(data)
    analysis['salary_avg'] = None

    depts = {}
    for job in data:
        if not job['dept'] in depts:
            depts[job['dept']] = 1
        else:
            depts[job['dept']] += 1
    analysis['num_by_dept'] = depts

    return analysis


def main():
    data = get_crawled_data()
    print(data)
    analysis = get_analysis(data)
    print(analysis)


if __name__ == '__main__':
    main()
