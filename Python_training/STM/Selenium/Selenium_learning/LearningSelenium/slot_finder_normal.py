import time

from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def start_search():
    driver.get("https://isl.ajanvaraus.fi/frontend/?lang=en")

    # transfer to international registration page
    time.sleep(1)
    ActionChains(driver).scroll_by_amount(0, 3000).perform()
    time.sleep(1)
    ActionChains(driver).scroll_by_amount(0, 3000).perform()

    international_reg_link = driver.find_element(By.LINK_TEXT, "International registrations")
    international_reg_link.click()

    # select Helsinki center
    found_dropdown = wait.until(EC.presence_of_element_located(
        (By.ID, "office2-first-dropdown")))
    found_dropdown.click()
    dropdown = Select(found_dropdown)
    dropdown.select_by_visible_text("Service location in Helsinki")

    # mouse click in empty space to close dropdown
    action = ActionBuilder(driver)
    action.pointer_action.pointer_down(MouseButton.FORWARD)
    action.pointer_action.pointer_up(MouseButton.FORWARD)
    action.perform()

    # Press button 'Select time'
    select_time_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button [@class='office-button office-button-DVV']"))).click()


def check_for_slots():
    """
    find all "a" tags that contain info about time slot (or slots) of all future (and today) days
    then in a loop, look for slots in next N days from today (including today)
    """

    time.sleep(1)
    path = "//a[starts-with(@class, 'fc-daygrid-event')]//child::div[starts-with(@class, 'new-calendar-daygrid-event')]"
    enabled_days = driver.find_elements(By.XPATH, path)

    number_of_days_of_interest = 7
    days_counter = 0
    feedback = False
    for one_a in enabled_days:
        if days_counter >= number_of_days_of_interest:
            print("No available days")
            break
        # print(one_a.text)
        if one_a.text != "No times":
            # print("!!!!!!!!!!!!!!!!!!!!!!!!")
            feedback = True
            break
        days_counter += 1
    return feedback


if __name__ == "__main__":
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
    driver.maximize_window()

    # start_search()
    # check_for_slots()

    while True:
        start_search()
        slots_search_result = check_for_slots()
        if slots_search_result:
            print("There is a time slot")
            # make_noise()
            # TODO call noise function
            break
        time.sleep(3)

