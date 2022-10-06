from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from selenium.common.exceptions import StaleElementReferenceException


def choose_one_suggestion():
    """find all suggestions that are hidden, and it's impossible to find them im DOM
    and also click on one of them. It works, but clicking issue a mistake"""
    driver.get("https://www.aviasales.ru/")

    destination_input = driver.find_element(By.XPATH, "//input[@id='destination']")
    destination_input.click()
    time.sleep(1)
    destination_input.send_keys("New")

    destination_suggestions = destination_input.find_element(
        By.XPATH, '//input[@id="destination"]//following::div[@class="autocomplete__dropdown"]')
    # print(destination_suggestions)
    time.sleep(1)
    all_suggestions = destination_suggestions.find_elements(
        By.XPATH, '//descendant::div[@class="autocomplete__suggestion-info"]')
    for one_elem in all_suggestions:
        # print(one_elem.tag_name)
        # print(one_elem.get_attribute("title"))
        if one_elem.get_attribute("title") == "Дели, Индия":
            # needful_suggestion = destination_suggestions.find_element(
            #     By.XPATH, '//descendant::div[@class="autocomplete__suggestion-info" and @title="Дели, Индия"]')
            # needful_suggestion.click()
            one_elem.click()


def choose_one_suggestion_hadle_exeption():
    """find all suggestions that are hidden, and it's impossible to find them im DOM
    and also click on one of them. Ignores StaleElementReferenceException by fluent wait"""
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                         ignored_exceptions=[StaleElementReferenceException])
    driver.get("https://www.aviasales.ru/")

    destination_input = driver.find_element(By.XPATH, "//input[@id='destination']")
    destination_input.click()
    time.sleep(1)
    destination_input.send_keys("New")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//descendant::div[@class='autocomplete__suggestion-info' and @title='Дели, Индия']"))).click()


if __name__ == "__main__":
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    # choose_one_suggestion()
    choose_one_suggestion_hadle_exeption()
    time.sleep(2)
    driver.quit()
