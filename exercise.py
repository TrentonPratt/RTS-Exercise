from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_bar = driver.find_element_by_name("q") #Inspected search bar element to determine name was "q"
search_bar.send_keys("RTS Labs")
search_bar.send_keys(Keys.RETURN)

result = driver.find_element_by_tag_name('h3') #first search result assumed to be first h3 element on page
result.click()


