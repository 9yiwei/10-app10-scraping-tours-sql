import os
import requests
import selectorlib
import smtplib, ssl

URL = "https://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape the page source from url"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def store(extracted):
    try:
        with open('data.txt', 'a') as file:
            file.write(extracted + '\n')
    except:
        with open('data.txt', 'w') as file:
            file.write(extracted + '\n')


def read():
    try:
        with open('data.txt', 'r') as file:
            return file.read()
    except:
        with open('data.txt', 'w') as file:
            pass


scraped = scrape(URL)
extracted = extract(scraped)
content = read()

print(extracted)

if extracted != "No upcoming tours":
    if extracted not in content:
        store(extracted)

