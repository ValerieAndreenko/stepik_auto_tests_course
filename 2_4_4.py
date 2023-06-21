from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    browser.get(link)
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/h5[2]")))
    prise = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/h5[2]").text.split()[0]
    prisegot = int(prise[1:])
    while prisegot > 100:
        prise = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/h5[2]").text.split()[0]
        prisegot = int(prise[1:])
    book_button = browser.find_element(By.CSS_SELECTOR, "#book")
    book_button.click()
    browser.execute_script("window.scrollBy(0, 100);")
    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap + #input_value")
    x = int(x_element.text)
    y = calc(x)
    put_number_in = browser.find_element(By.CSS_SELECTOR, "#answer")
    put_number_in.send_keys(y) 
    submit_button = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit_button.click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(10)
    browser.quit()