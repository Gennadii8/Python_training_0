import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import winsound
from playsound import playsound


def start_search():

    # choose residence permit as a category
    category_dropdown_0 = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@placeholder='Valitse palvelukategoria']")))
    time.sleep(1)
    category_dropdown_0.click()
    residence_permit_selector = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Oleskelulupa']")))
    residence_permit_selector.click()

    # choose family as a service
    category_dropdown_1 = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@placeholder='Valitse palvelu']")))
    time.sleep(1)
    category_dropdown_1.click()
    family_selector = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='2. Perhe (ensimmäinen ja jatkolupa)']")))
    family_selector.click()

    # choose Helsinki as a service
    category_dropdown_2 = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@data-placeholder='Valitse toimipiste']")))
    time.sleep(1)
    category_dropdown_2.click()
    city_selector = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Helsinki : Malmin palvelupiste']")))
    city_selector.click()

    # click search button
    search_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@class='btn btn-primary btn-block hidden-xs ladda-button']")))
    search_button.click()


def check_for_slots():

    # go to the current week
    upcoming_slots_link = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//a[@class='week-indicatorsLink indicatorFirst']")))
    upcoming_slots_link.click()

    # check slots - play sound, if they are presented
    time.sleep(2)
    driver.implicitly_wait(2)
    available_slots = driver.find_elements(By.XPATH, "//a[@class='btn btn-primary tip tt1 ng-binding']")
    return available_slots


def make_noise():
    # TODO сделать это уже на моём компе
    winsound.Beep(440, 5000)
    # playsound('audio.mp3')


if __name__ == "__main__":
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
    driver.maximize_window()
    driver.get("https://migri.vihta.com/public/migri/#/reservation")

    while True:
        start_search()
        slots_search_result = check_for_slots()
        if slots_search_result:
            print("Слоты есть")
            make_noise()
            break
        time.sleep(300)
