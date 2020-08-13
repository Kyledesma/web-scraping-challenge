#Import Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import time
import pandas as pd
from splinter.exceptions import ElementDoesNotExist




def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'C:\\DS Bootcamp\\gt-inc-data-pt-05-2020-u-c\\chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)



def scrape():
    browser = init_browser()

    #Creating dictionaries
    mars_data = {}



    #Visting Website
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    
    #Creating a soup object from the html
    soup = BeautifulSoup(response.text, 'lxml')

    #Add news_pp to MongoDB
    results = soup.find_all('div', class_='list_text')

    # Retrieve the thread title
    title = result.find('div', class_='content_title')


    # Extract the title text
    news_title = title.a.text



    #Extract the paragraph text
    news_p = result.find('div', class_='article_teaser_body').text


    #Inserting into MongoDB
    mars_data['news_title'] = news_title
    mars_data['news_paragraph'] = news_p

    browser.quit()
    return mars_data