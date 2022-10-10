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
    # international_reg_link = wait.until(EC.element_to_be_clickable(
    #     (By.LINK_TEXT, "International registrations"))).click()

    # while True:
    #     if not driver.find_element(By.LINK_TEXT, "International registrations").is_displayed():
    #         ActionChains(driver).scroll_by_amount(0, 3000).perform()
    #     else:
    #         driver.find_element(By.LINK_TEXT, "International registrations").click()
    #         break

    international_reg_link = driver.find_element(By.LINK_TEXT, "International registrations")
    international_reg_link.click()

    # try:
    #     print("aaaaaaaaaaaaaaa")
    #     international_reg_link = driver.find_element(By.LINK_TEXT, "International registrations")
    #     international_reg_link.click()
    # except ElementClickInterceptedException:
    #     print("bbbbbbbbbbbbbbbb")
    #     ActionChains(driver).scroll_by_amount(0, 3000).perform()
    #     time.sleep(1)
    #     international_reg_link = driver.find_element(By.LINK_TEXT, "International registrations")
    #     international_reg_link.click()
    # except NoSuchElementException:
    #     print("cccccccccccccc")
    #     ActionChains(driver).scroll_by_amount(0, 3000).perform()
    #     time.sleep(1)
    #     international_reg_link = driver.find_element(By.LINK_TEXT, "International registrations")
    #     international_reg_link.click()


    # select Helsinki center
    found_dropdown = wait.until(EC.presence_of_element_located(
        (By.ID, "office2-first-dropdown")))
    found_dropdown.click()
    # found_dropdown = driver.find_element(By.ID, "office2-first-dropdown")
    dropdown = Select(found_dropdown)
    dropdown.select_by_visible_text("Service location in Helsinki")


    # mouse click in empty space to close dropdown
    action = ActionBuilder(driver)
    action.pointer_action.pointer_down(MouseButton.FORWARD)
    action.pointer_action.pointer_up(MouseButton.FORWARD)
    action.perform()

    time.sleep(2)
    # Press button 'Select time'
    select_time_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button [@class='office-button office-button-DVV']"))).click()
    # select_time_button = driver.find_element(By.XPATH, "//button [@class='office-button office-button-DVV']")
    # select_time_button.click()


def check_for_slots():
    """проходить последовательно по каждому tr, проверять есть ли вообще td с атрибутом data-date (он отсутсвует у
    прошедших недель) (первый пропускать - это сегодня),
    и соответсвенно проходить только два tr с атрибутом data-date (дальше уже не интересно)
    Потом в каждом td ныряем в
    div class="fc-daygrid-day-frame fc-scrollgrid-sync-inner"
    div class="fc-daygrid-day-events"
    div class="fc-daygrid-event-harness"
    a class="fc-daygrid-event fc-daygrid-dot-event fc-event fc-event-start fc-event-end fc-event-future"
    div class="new-calendar-daygrid-events"
    и чекаем текст, если он != No times , то мы нашли искомое
    """
    whole_table = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//tbody[@role='presentation']")))
    # whole_table = driver.find_element(By.XPATH, "//tbody[@role='presentation']")
    all_tr_table = whole_table.find_elements(By.TAG_NAME, "tr")
    counter = 0
    for one_tr in all_tr_table:
        # div_in_tr = one_tr.find_element(By.XPATH, "//a[@class='fc-daygrid-event fc-daygrid-dot-event fc-event fc-event-start fc-event-end fc-event-future']")
        # print(div_in_tr.text)
        feedback = False
        if counter > 2:
            # print("No time slots")
            break

        # print(one_tr.text)
        # print()

        if ":" in one_tr.text:
            # print("There is a time slot")
            # TODO Make noise here
            feedback = True
            break

        counter += 1
    return feedback


def make_notification():
    # TODO make noise!!
    driver.get("https://www.google.com/")


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
            # make_notification()
            # TODO call noise function
            break
        time.sleep(3)
