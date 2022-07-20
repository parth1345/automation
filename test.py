from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.theverge.com/")
driver.maximize_window()
driver.implicitly_wait(10)
for i in range(2, 5):
    driver.find_element(By.XPATH, f'(//h2[@class="c-entry-box--compact__title"]//a)[{i}]').send_keys(Keys.CONTROL,
                                                                                                     Keys.ENTER)
    driver.implicitly_wait(10)
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(10)
    title = driver.find_element(By.XPATH, '//h1[@class="c-page-title"]').text
    content = driver.find_element(By.XPATH, '//div[@class="c-entry-content "]').text
    img = driver.find_element(By.XPATH, '//picture[@class="c-picture"]/img')
    src = img.get_attribute('src')
    print(src)
    time.sleep(50)
    print(content)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
