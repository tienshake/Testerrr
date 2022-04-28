from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://fullstack.edu.vn") #step 1
driver.implicitly_wait(6)
#step 2 bam vao dang nhap
driver.find_element(By.CSS_SELECTOR, '#root > div.NavBar_wrapper__4m3K5 > div.NavBar_actions__nSNzo > a').click()
#step 3 Bấm vào button 'Sử dụng email/số điện thoại'
driver.find_element(By.CSS_SELECTOR, '#root > div > div.Login_container__l\+22X > div.Login_content__Clzqv > div.Login_body__t6Xgp > div > div:nth-child(1)').click()
#Step 4: Nhập số điện thoại vào ô nhập số điện thoại
driver.find_element(By.CSS_SELECTOR, '#root > div > div.Login_container__l\+22X > div.Login_content__Clzqv > div.Login_body__t6Xgp > div > div:nth-child(1) > div > div.FormInput_inputWrap__mjtRx > input[type=text]').send_keys('0339255709')
#Step 5: Ấn vào nút gởi mã
driver.find_element(By.CSS_SELECTOR, '#root > div > div.Login_container__l\+22X > div.Login_content__Clzqv > div.Login_body__t6Xgp > div > div:nth-child(2) > div > div.FormInput_inputWrap__mjtRx > div').click()
#Step 6: Nhập mã xác nhận vào ô nhập mã xác nhận
driver.find_element(By.CSS_SELECTOR, '#root > div > div.Login_container__l\+22X > div.Login_content__Clzqv > div.Login_body__t6Xgp > div > div:nth-child(2) > div > div.FormInput_inputWrap__mjtRx > input[type=number]').send_keys('323232')
#step 7 bam vao dang nhap
driver.find_element(By.CSS_SELECTOR, '#root > div > div.Login_container__l\+22X > div.Login_content__Clzqv > div.Login_body__t6Xgp > div > button > div').click()
#sau khi thực hiện xong thì chỉ tắt trình duyệt
# driver.close()