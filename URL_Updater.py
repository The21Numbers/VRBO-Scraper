from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver

# region instantiate driver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
# endregion

start_url = \
    'https://www.vrbo.com/search/keywords:pointe-west-galveston-galveston-county-texas-united-states-of-america/page:%d'

for page in range(1, 21):
    driver.get(start_url % page)

    time.sleep(5)

    # region scroll down page (load page)

    # preps action chains
    actions = ActionChains(driver)
    actions.send_keys(' ')

    for i in range(18):
        time.sleep(0.1)
        actions.perform()

    time.sleep(1)

    # endregion

    # TODO Grab all urls and store in file.
    #

collection = driver.find_element_by_class_name('HitCollection')
print(collection.text)
