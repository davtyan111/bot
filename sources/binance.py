from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bot.config import SOURCE_USDT_BINANCE, SOURCE_BINANCE_BTC_USDT


def get_usdt_price_Binance():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install()) 
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(SOURCE_USDT_BINANCE)

    try:
        price_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-cy='input-fiat-amount']"))
        )
        price = price_element.get_attribute("value")

        if not price:
            print("USDT: Price element is empty, refreshing...")
            driver.refresh()
            price_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-cy='input-fiat-amount']"))
            )
            price = price_element.get_attribute("value")
            print("USDT: Price element found after refresh.")

        return f"1 USDT ≈ {price} AMD"

    except Exception as e:
        return f"Error: {e}"
    finally:
        driver.quit()


def get_btc_price_Binance():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(SOURCE_BINANCE_BTC_USDT)  # ✅ Use the variable for consistency

    try:
        price_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.lock-ltr.text-subtitle1.font-medium")
            )
        )
        price = price_element.text.strip()
        return f"1 BTC ≈ {price} USDT"
    except Exception as e:
        return f"Error: {e}"
    finally:
        driver.quit()
