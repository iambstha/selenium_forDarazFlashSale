from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
# opt.add_argument('headless')
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)

driver.implicitly_wait(5)
driver.get("https://www.daraz.com.np/")


def askItem():
    askedItem = input("Search item in Daraz Flash Sale: ")
    findComponents(askedItem)

def findComponents(askedItem):
    item = askedItem
    text_box = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[3]/div[2]/div[1]/a")
    text_box.click()
    
    flash_element = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]")
    sale_element = flash_element.find_elements(by=By.CLASS_NAME, value="sale-title")
    # arrFlash = []
    # for i in sale_element:
    #     arrFlash.append(i.text)
    
    for items in sale_element:
        if item in items.text:
            print(items.text) 

askItem()