from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver

# region instantiate driver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
# endregion

start_url = \
    'https://www.vrbo.com/search/keywords:pointe-west-galveston-galveston-county-texas-united-states-of-america/page:1/'
driver.get(start_url)

# region scroll down page (load page)

# preps action chains
actions = ActionChains(driver)
actions.send_keys(' ')

for i in range(25):
    time.sleep(0.1)
    actions.perform()

time.sleep(1)

# TODO FIX
for listing in driver.find_elements_by_xpath("//div[@class='Hit media-flex media-flex--left media-flex--xs']"):
    listing_el = listing.find_element_by_xpath("//a[@href]")
    print(listing_el.get_attribute('innerHTML'))

driver.quit()
