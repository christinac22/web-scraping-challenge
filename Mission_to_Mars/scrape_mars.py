#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# ## NASA Mars News

# In[2]:


# Referenced Day 2 Ins-Splinter
# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit Nasa news url
url = 'https://redplanetscience.com/'
browser.visit(url)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[5]:


news_title = soup.find('div', class_='content_title')


# In[6]:


news_p = soup.find('div', class_='article_teaser_body')


# In[7]:


print(news_title.text)
print('------')
print(news_p.text)


# In[8]:


browser.quit()


# ## JPL Mars Space Images - Featured Image

# In[9]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[10]:


url = 'https://spaceimages-mars.com/'
browser.visit(url)


# In[11]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[12]:


# Referenced: https://www.geeksforgeeks.org/image-scraping-with-python/
for item in soup.find_all('img', class_='thumbimg'):
    print(url + requests.utils.quote(item['src']))


# In[13]:


browser.quit()


# ## Mars Facts

# In[14]:


url = 'https://galaxyfacts-mars.com/'


# In[15]:


# Use Pandas to scrape tabular data from url
tables = pd.read_html(url)


# In[16]:


type(tables)


# In[17]:


tables[0]


# In[18]:


#Display df
# Referenced: https://stackoverflow.com/questions/61736164/how-can-i-set-second-row-as-a-name-of-columns-in-dataframe
mars_diagram_df = tables[0]
mars_diagram_df.columns = mars_diagram_df.iloc[0]
mars_diagram_df = mars_diagram_df.iloc[1:].reset_index(drop=True)
mars_diagram_df.set_index("Mars - Earth Comparison", inplace=True)
mars_diagram_df


# In[19]:


tables[1]


# In[20]:


#Display df
mars_planet_profile_df = tables[1]

# Rename df/set_index
mars_planet_profile_df.columns = ["Description" , "Information"]
mars_planet_profile_df.set_index("Description", inplace=True)

mars_planet_profile_df


# ## Mars Hemispheres

# In[21]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[22]:


url = 'https://marshemispheres.com/'
browser.visit(url)


# In[23]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[24]:


# image urls
for item in soup.find_all('img', class_='thumb'):
    img = url + item['src']
    print(img)


# In[25]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": {img}},
    {"title": "Cerberus Hemisphere", "img_url": {img}},
    {"title": "Schiaparelli Hemisphere", "img_url": {img}},
    {"title": "Syrtis Major Hemisphere", "img_url": {img}}
]


# In[26]:


hemisphere_image_urls


# In[27]:


browser.quit()


# In[ ]:




