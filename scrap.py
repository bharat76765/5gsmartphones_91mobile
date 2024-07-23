import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException

# Initialize the WebDriver
s = Service("C:/Users/babab/Downloads/edgedriver_win64 (1)/msedgedriver.exe")
driver = webdriver.Edge(service=s)

try:
    driver.get("https://www.google.co.in/")
    time.sleep(2)

    search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search.send_keys("https://www.91mobiles.com/5g-mobile-price-list-in-india")
    time.sleep(2)
    search.send_keys(Keys.ENTER)

    select91 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
    time.sleep(2)
    select91.click()
    time.sleep(2)


    driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/2)")
    time.sleep(2)
    html = []
    html.append(driver.page_source)
    selectnext = driver.find_element(By.XPATH, '//*[@id="finder_pagination"]/div/div[2]/span')
    selectnext.click()
    time.sleep(2)

    for i in range(10):
        try:
            driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/2)")
            time.sleep(3)  # Allow time for scrolling
            html.append(driver.page_source)
            sam = driver.find_element(By.XPATH, '//*[@id="finder_pagination"]/div/div[4]/span')
            sam.click()
            time.sleep(3)  # Allow time for page to load
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            print(f"Error navigating to page {i + 2}: {e}")
            break

    html5g = "".join(html)
    with open("5gphone2.html", 'w', encoding='utf-8') as f:
        f.write(html5g)

finally:
    driver.quit()
