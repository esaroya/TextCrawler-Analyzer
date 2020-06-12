# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:06:58 2020

@author: eishe
"""

import requests
import csv
import time
from bs4 import BeautifulSoup
import preprocessor

"""
    CREATE CRAWLER CLASS.
    
    NEEDED FUNCTIONS:
        Write_data: after you get all the data you want from reddit, isolate the data
                    that you need for your analysis and save to another text file.
                    
                    @PARAMS @fields which fields you want pr
                
    
"""


def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)

def open_html(path):
    with open(path, 'rb') as f:
        return f.read()
    

#if __name__ == "__main__":
def crawl_reddit():  #params: list of subreddit links, with codes for what data you want
    url = "https://old.reddit.com/r/datascience/"
    
    headers = {'User-Agent':'Mozilla/5.0'}
    
    page = requests.get(url, headers=headers)
    
    
    soup = BeautifulSoup(page.text, 'html.parser')
    soup.prettify()
    
    attrs = {'class':'thing', 'data-domain':'self.datascience' }
    
    counter = 1
    while (counter <= 100):
        for post in soup.find_all("div", attrs=attrs):
            title = post.find('p', class_='title').text
            author = post.find('a', class_='author').text
            comments = post.find('a', class_='comments')
            numcomments = comments.text.split()[0]
            likes = post.find("div", attrs={"class": "score unvoted"}).text
            if "comment" in numcomments:
                numcomments = 0
            if "•" in likes:
                likes = "none"
            
            #print("\nTitle: " + title + "\nAuthor: " + author + "\nComments: " + str(comments) + "\nLikes: " + likes + "\n")
            link = comments.attrs['href']
            time.sleep(.5)        
            linkPage = requests.get(link, headers = headers)
            commentSoup = BeautifulSoup(linkPage.text, 'html.parser')
            commentSoup.prettify()
            try:
                expando = commentSoup.find("div", class_='expando')
                text = expando.find("div", class_='md').text
            except:
                text = "empty"
            
            process = preprocessor.preprocessor(text)
            process.processText()
            processedText = ' '.join(process.wordTokens)
    
            post_line = [counter, title, author, numcomments, likes, text, processedText]
            ##print(post_line)
            with open('output.csv', 'a', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter='|')
                writer.writerow(post_line)
            counter+=1
        
        next_button = soup.find("span", class_="next-button")
        next_page_link = next_button.find("a").attrs['href']
        time.sleep(3)
        page = requests.get(next_page_link, headers = headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        
       
   
def getPostTitle():

def getLikes():
    
def Postlikes():

def getTopNcomments(): #where N is less than 101    
        
def getPostSummary():
    
def downloadimage():

def findclosestsubreddits():
    
def findstringmentions():
    
def AppendColumnAndSave():
    

           
