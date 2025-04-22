from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bot.config import SOURCE_USDT_FASTEX_USDT, SOURCE_FASTEX_BTC_USDT


def fetch_fastex_price_usdt():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(SOURCE_USDT_FASTEX_USDT)

    try:
        price_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[starts-with(@class, 'MarketPrice_wrapper__price')]")
            )
        )
        price_text = price_element.text.strip()

        if not price_text:
            print("USDT: Price element is empty, refreshing...")
            driver.refresh()
            price_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p[starts-with(@class, 'MarketPrice_wrapper__price')]")
                )
            )
            price_text = price_element.text.strip()
            print("USDT: Price element found after refresh.")

        return f"1 USDT ≈ {price_text} AMD"

    except Exception as e:
        return f"Error: {e}"
    finally:
        driver.quit()


def fetch_fastex_price_BTC():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(SOURCE_FASTEX_BTC_USDT)

    try:
        price_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[starts-with(@class, 'MarketPrice_wrapper__price')]")
            )
        )
        price_text = price_element.text.strip()

        if not price_text:
            print("BTC: Price element is empty, refreshing...")
            driver.refresh()
            price_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p[starts-with(@class, 'MarketPrice_wrapper__price')]")
                )
            )
            price_text = price_element.text.strip()
            print("BTC: Price element found after refresh.")

        return f"1 BTC ≈ {price_text} USDT"

    except Exception as e:
        return f"Error: {e}"
    finally:
        driver.quit()
