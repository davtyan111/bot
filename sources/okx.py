from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from bot.config import CHROMEDRIVER_PATH, SOURCE_USDT_OKX

def fetch_okx_price():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(CHROMEDRIVER_PATH)

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(SOURCE_USDT_OKX)

    try:
        price_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'index_priceHint')]"))
        )
        price = price_element.text
    except Exception as e:
        price = f"Error: {e}"
    driver.quit()
    return price


