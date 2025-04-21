from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bot.config import CHROMEDRIVER_PATH, SOURCE_USDT_BINANCE ,SOURCE_BINANCE_BTC_USDT

def get_usdt_price_Binance():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(SOURCE_USDT_BINANCE)

    try:
        price_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-cy='input-fiat-amount']"))
        )
        price = f"1 USDT ≈ {price_element.get_attribute('value')} AMD"
    except Exception as e:
        price = f"Error: {e}"
    driver.quit()
    return price

def get_btc_price_Binance():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(CHROMEDRIVER_PATH)

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(SOURCE_BINANCE_BTC_USDT)

    try:
        price_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.lock-ltr.text-subtitle1.font-medium")
            )
        )
        price = price_element.text.strip()
        price = f"1 BTC ≈ {price} USDT"
    except Exception as e:
        price = f"Error: {e}"
    driver.quit()
    return price

