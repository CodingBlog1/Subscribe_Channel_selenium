from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

urls = ["https://www.youtube.com/@CrazyXYZ","https://www.youtube.com/@JingleToons","https://www.youtube.com/zeenews"]

driver = webdriver.Edge()
for url in urls:
    driver.get(url)
    driver.maximize_window()
   
    WebDriverWait(driver,200).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#subscribe-button > ytd-button-renderer > yt-button-shape > button'))).click()
    # driver.find_element(By.CSS_SELECTOR,').click()
    # time.sleep(5) 

    driver.find_element(By.CSS_SELECTOR,'#button > yt-button-shape > a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys('shoyabmalik7887@gmail.com')
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button').click()
    time.sleep(2)
    WebDriverWait(driver,120).until(EC.presence_of_element_located((By.NAME,'password'))).send_keys("#Malik7887")
    na = driver.find_element(By.NAME,'password')
    na.send_keys("#Malik7887")
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button').click()
    time.sleep(2)
    WebDriverWait(driver,200).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#subscribe-button > ytd-button-renderer > yt-button-shape > button'))).click()


    

    time.sleep(2)
    

    screenshot_filename = f"{url.split('/')[-1]}_subscription.png"
    driver.save_screenshot(screenshot_filename)
    print(f"Screenshot saved as {screenshot_filename}")
    
# close the browser
# driver.quit()

