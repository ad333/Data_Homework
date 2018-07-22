# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import selenium
from selenium import webdriver
import pandas as pd
import time

def scrape():

    # Set up the browser path
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}  
    browser = Browser('chrome', **executable_path, headless=False) 

    mars_data = {}

    # NASA Mars news
    # ---------------
    
    # visit the url
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    time.sleep(2)

    # Extract html from browser, create beautiful soup object and parse with html parser
    html = browser.html
    soup = bs(html, 'html.parser')

    # Extract news title and paragraph
    news_title = soup.find('div', class_ = 'content_title').text
    news_p = soup.find('div', class_ = 'article_teaser_body').text


    # JPL Mars Space Images - Featured Image
    # --------------------------------------

    # visit the url
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    time.sleep(2)

    # Extract html from browser, create beautiful soup object and parse with html parser
    img_html = browser.html
    img_soup = bs(img_html, 'html.parser')

    # extract image path src
    img_path = img_soup.find('img', class_ = 'thumb')
    img_src = img_path['src']

    # full image url
    main_url = 'https://www.jpl.nasa.gov'
    featured_image_url = main_url + img_src


    # Mars Weather
    # ------------

    # visit the url
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    time.sleep(2)

    # Extract html from browser, create beautiful soup object and parse with html parser
    weather_html = browser.html
    weather_soup = bs(weather_html, 'html.parser')

    # Extract text for mars weather
    mars_weather = weather_soup.find('p', class_ = 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text


    # Mars facts
    # ----------

    # visit the url
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    time.sleep(2)

    # read html into pandas dataframe
    facts_table = pd.read_html(facts_url)[0]
    facts_table = facts_table.rename(columns = {0: 'Description', 1: 'Value'})
    facts_table_df = facts_table.set_index(['Description'])

    # convert to dictionary
    facts_dict = facts_table_df.to_dict()  


    # Mars hemispheres
    # ----------------

    # visit the url
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    time.sleep(2)

    # Extract html from browser, create beautiful soup object and parse with html parser
    hemispheres_html = browser.html
    hemispheres_soup = bs(hemispheres_html, 'html.parser')

    # Extract elements containing the url paths
    path = hemispheres_soup.find('div', class_ = 'collapsible results')
    i_path = path.find_all('a')

    # declare empty list to hold dictinaries
    hemisphere_image_urls = []

    # Loop for each hemispheres
    for i in i_path:
        if i.h3:
            # extract title and url
            title = i.h3.text
            url = 'https://astrogeology.usgs.gov/' + i['href']
            
            browser.visit(url)
            time.sleep(2)
            url_html = browser.html
            image_soup = bs(url_html, 'html.parser')
            
            # Extract image url
            image_url = image_soup.find('div', class_ = 'downloads').find('li').a['href']
            
            # Add title and img_url to dictionary
            dict_ = {'title':title, 'img_url':image_url}

            # append dictionary items to the list
            hemisphere_image_urls.append(dict_)

    # Add all data to a single dictionary
    mars_data = { "news_title": news_title,
                  "news_p": news_p,
                  "featured_image_url": featured_image_url,
                  "mars_weather": mars_weather,
                  "facts_dict": facts_dict,
                  "hemisphere_image_urls": hemisphere_image_urls}

    return mars_data