from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


#step 1 vào google
driver.get("https://www.google.com")

driver.title # => "Google"

driver.implicitly_wait(0.5)

search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")

#step 2: nhập dữ liệu vào ô
search_box.send_keys("Selenium")

#step 3: bấm vào button tìm kiếm
search_button.click()

driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"

driver.quit()