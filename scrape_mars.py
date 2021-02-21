#!/usr/bin/env python
# coding: utf-8


from splinter import browser
from bs4 import BeautifulSoup
import pandas as pd
import time


#link for ref 
# https://splinter.readthedocs.io/en/latest/drivers/chrome.html

get_ipython().system('which chromedriver')


def scrape():
    
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    Nasa_News_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


    browser.visit(Nasa_News_url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    #scrape latest news title
    news_title = soup.find_all('div', class_='content_title')
    latest_title = news_title[1].text
    #print(latest_title)


    #scrape latest news article teaser
    news_teaser = soup.find_all('div', class_="article_teaser_body")
    latest_teaser = news_teaser[0].text
    #print(latest_teaser)


    #scrape JPL Mars featured image 
    JPL_Mars_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(JPL_Mars_url)

    #click buttons to load image webpage
    browser.click_link_by_id("full_image")
    time.sleep(3)
    browser.click_link_by_partial_text("more info")


    # make a new soup
    html=browser.html
    soup=BeautifulSoup(html, "html.parser")
    sub_img = soup.find("figure", class_="lede")
    name=sub_img.a["href"]
    featured_image="https://www.jpl.nasa.gov" + name
    #featured_image


    USGS_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(USGS_url)

    html=browser.html
    soup=BeautifulSoup(html, "html.parser")

    hemi_list = []

    hemispheres = soup.find_all("div", class_="item")

    for hemi in hemispheres:
        #for titles
        hemi_div = hemi.find("div", class_="description")
        hemi_title = hemi_div.a.h3.text
        #print(hemi_title)

        #click link for images
        browser.click_link_by_partial_text("Hemisphere Enhanced")
        time.sleep(3)

        # scrape image 
        html=browser.html
        soup_4=BeautifulSoup(html, "html.parser")
        usgs_open = soup_4.find("img", class_="wide-image")
        usgs_src=usgs_open["src"]
        hemi_image_url="https://www.astrogeology.usgs.gov" + usgs_src
        #print(hemi_image)
        hemi_list.append({"title": hemi_title, "img_url": hemi_image_url})
        
    mars_scrape_data = {
        'Latest Headline': latest_title, 
        latest_teaser, 
        'Featured Image': featured_image, 
        hemi_list}

    return mars_scrape_data







