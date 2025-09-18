import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://localhost:8000/dz.html")

time.sleep(10)

frame1 = driver.find_element(By.ID, "frame1")
driver.switch_to.frame(frame1)
time.sleep(10)
input1 = driver.find_element(By.ID, "input1")
input1.send_keys("Secret")
time.sleep(10)
button1 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
button1.click()
time.sleep(10)

alert = Alert(driver)
alert_text = alert.text
if alert_text == "Верифікація пройшла успішно!":
    print("Успішно пройшли верифікацію в фреймі 1")
else:
    print("Помилка верифікації в фреймі 1")

alert.accept()
time.sleep(10)
driver.switch_to.default_content()

frame2 = driver.find_element(By.ID, "frame2")
driver.switch_to.frame(frame2)
time.sleep(10)
input2 = driver.find_element(By.ID, "input2")
input2.send_keys("Frame2_Secret")
time.sleep(10)
button2 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
button2.click()
time.sleep(10)
alert = Alert(driver)
alert_text = alert.text
if alert_text == "Верифікація пройшла успішно!":
    print("Успішно пройшли верифікацію в фреймі 2")
else:
    print("Помилка верифікації в фреймі 2")

alert.accept()
time.sleep(10)
driver.quit()




