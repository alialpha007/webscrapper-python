# Import Libraries
import csv
from isort import file
import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup

# Cleaning the Terminal
print("\033c")


url = "https://www.amazon.com/2022-Apple-MacBook-Laptop-chip/dp/B0B3C57XLR/ref=sr_1_2?crid=3286H5YIQUCWE&keywords=macbook&qid=1665582528&qu=eyJxc2MiOiI2LjQ2IiwicXNhIjoiNi42MSIsInFzcCI6IjYuMjYifQ%3D%3D&sprefix=macbook%2Caps%2C445&sr=8-2"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

page = requests.get(url, headers=headers)
soup1 = BeautifulSoup(page.content, 'html.parser')
# soup2 = BeautifulSoup(soup1.prettify())
title = soup1.find(id='productTitle').text.strip()
price = soup1.find('span', {"class": "a-offscreen"}).text.strip()
# print("Product Name: ", title)
# print("Product Price: ", price)
# print(type(title))
# print(type(price))

date = datetime.date.today()

header = ['Title', 'Price', 'Date']
data = [title, price, date]
with open('AmazonWebScrapper.csv', 'w', newline='', encoding='UTF') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

dataFile = pd.read_csv(
    '/Users/muhammadali/Documents/University/Introduction to Data Science/Lab/AmazonWebScrapper.csv')
print(dataFile)
