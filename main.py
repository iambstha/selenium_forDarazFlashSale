from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.daraz.com.np/")


def test_eight_components():


    text_box = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[3]/div[2]/div[1]/a")
    text_box.click();

    flash_element = driver.find_element(by=By.XPATH, value="/h tml/body/div[3]/div[2]");
    sale_element = flash_element.find_elements(by=By.CLASS_NAME, value="sale-title");
    for i in sale_element:
        print(i.text)

    driver.quit()

test_eight_components()
