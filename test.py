from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.theverge.com/")
driver.maximize_window()
driver.implicitly_wait(10)
for i in range(1, 39):
    # if i == 4:
    #     continue
    driver.find_element(By.XPATH, f'(//h2[@class="c-entry-box--compact__title"]//a)[{i}]').send_keys(Keys.CONTROL,
                                                                                                     Keys.ENTER)
    driver.implicitly_wait(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(2)
    title = driver.find_element(By.XPATH, '//h1[@class="c-page-title"]').text
    print(i)
    if title == 'The Great Fiction of AI' or title == 'Dungeons & Dragons: Honor Among Thieves looks like a ' \
                                                      'celebrity-filled LARP in first trailer':
        continue
    content = driver.find_element(By.XPATH, '//div[@class="c-entry-content "]').text
    with open('post_img.png', 'wb') as file:
        try:
            img = driver.find_element(By.XPATH, '//picture[@class="c-picture"]/img')
        except NoSuchElementException:
            img = driver.find_element(By.XPATH,
                                      '//div[@class="ytp-cued-thumbnail-overlay"]//div['
                                      '@class="ytp-cued-thumbnail-overlay-image"]')
        file.write(img.screenshot_as_png)
    driver.implicitly_wait(10)
    try:
        driver.find_element(By.XPATH, '//a[@class="c-entry-hero__logo"]').send_keys(Keys.CONTROL, Keys.ENTER)
    except NoSuchElementException:
        driver.find_element(By.XPATH, '//a[@id="chorus-brand"]').send_keys(Keys.CONTROL, Keys.ENTER)
    driver.switch_to.window(driver.window_handles[2])
    driver.implicitly_wait(5)
    driver.get('http://139.59.95.41:8000/addpost')
    if i == 1:
        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('parthshah5642@gmail.com')
        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('123')
        driver.find_element(By.XPATH, '//input[@class="button text-white"]').click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, '//a[@href="/addpost/"]').click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, '//input[@id="title"]').send_keys(title)
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, '//input[@id="img_file"]').send_keys(
        r"C:\Users\parth.shah\Desktop\tests\automation\post_img.png")
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, '//textarea[@id="content"]').send_keys(content)
    driver.find_element(By.XPATH, '//input[@value="Add Post"]').click()
    driver.implicitly_wait(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
