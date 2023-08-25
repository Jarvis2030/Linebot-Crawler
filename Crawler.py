from selenium.webdriver.common.by import By
from selenium import webdriver
import selenium
from time import sleep
from bs4 import BeautifulSoup

#Define the webdriver
driver = webdriver.Safari()

#Get the specific 
driver.get('https://www.openrice.com/zh/hongkong')

#fetch the search bar, input the target
search = driver.find_element(By.CLASS_NAME, "quick-search-input-field")
search.click()
search.send_keys("荃灣")
sleep(2)
button = driver.find_element(By.CLASS_NAME, "quick-search-button")
button.click()

sleep(3)
#Use beatifulSoup return the details of the result page
soup = BeautifulSoup(driver.page_source, 'html.parser')
cards = soup.select('li.sr1-listing-content-cell', limit=10)[3:]
content = []
for card in cards:
    title = card.find(
        'h2',{'class':'title-name'}).getText()
    #print(title)
    address = card.find(
        'div',{'class':'icon-info address'}).getText()
    #print(address)
    price = card.find(
        'div',{'class':'icon-info-food-price'}).getText()
    #print(price)
    type = card.find(
        'div',{'class':'icon-info-food-name'}).getText()
    #print(type)
    print(card)
    good = card.select_one(
        'div.emoticon-container.smile-face.pois-restaurant-list-cell-content-right-info-rating-happy').getText()
    #print(good)
    bad = card.select_one(
        'div.emoticon-container.sad-face.pois-restaurant-list-cell-content-right-info-rating-happy').getText()
    #print(bad)
    
    content += f"{title} \n Good vs bad: {good}/{bad} \n {price} \n {address} \n\n"

#print(content)

while(True):
    pass


