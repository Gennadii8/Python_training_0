from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException, ElementNotVisibleException, \
    ElementNotSelectableException


class FindElement:
    # def __int__(self):
    #     pass

    def locate_by_id(self, elem_id):
        driver.get("https://www.aviasales.ru")
        # departure_input = driver.find_element(By.ID, 'destination')
        departure_input = driver.find_element(By.ID, elem_id)
        departure_input.send_keys("Helsinki")

    def locate_by_xpath(self, elem_xpath):
        driver.get("https://www.aviasales.ru")
        # departure_input = driver.find_element(By.XPATH, '// *[ @ id = "destination"]')
        # departure_input = driver.find_element(By.XPATH, '//input[@id="destination"]')
        departure_input = driver.find_element(By.XPATH, elem_xpath)
        departure_input.send_keys("Riga")

    def locate_by_link_text(self, elem_link_text):
        driver.get("https://www.aviasales.ru")
        # time.sleep(3)
        # departure_input = driver.find_element(By.LINK_TEXT, elem_link_text)
        # locating by partial link
        departure_input = driver.find_element(By.PARTIAL_LINK_TEXT, elem_link_text)
        # link is invisible because of pop-up, so at first I scroll page to the end
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        departure_input.click()

    def locate_dynamic_element_start(self):
        # finding input "destination"
        driver.get("https://www.aviasales.ru")
        departure_input = driver.find_element(By.XPATH, '//input[starts-with(@id, "destina")]')
        print(departure_input.get_attribute("type"))

    def locate_dynamic_element_contains(self):
        # finding input "destination"
        driver.get("https://www.aviasales.ru")
        departure_input = driver.find_element(By.XPATH, '//input[contains(@id, "stinati")]')
        print(departure_input.get_attribute("type"))

    def locate_parent_element(self):
        """Also possible to find children, descendant, ancestor, siblings and so on
        https://www.scientecheasy.com/2019/08/xpath-axes.html/"""

        driver.get("https://www.aviasales.ru")
        arrival_input_parent = driver.find_element(By.XPATH, '//input[@id="destination"]//parent::div')
        print(arrival_input_parent.get_attribute("class"))


class FindElements:

    def locate_elements_by_name(self, elem_name):
        driver.get("https://www.aviasales.ru")
        # departure_input = driver.find_element(By.ID, 'destination')
        departure_input = driver.find_elements(By.TAG_NAME, elem_name)
        for one_elem in departure_input:
            print(one_elem.text)

        # departure_input.send_keys("Helsinki")


class GetAttributeValue:

    def get_value(self):
        driver.get("https://www.aviasales.ru")
        found_element = driver.find_element(By.ID, 'destination')
        print(found_element.get_attribute("type"))


"""get all attributes of element"""
# all_attributes = driver.execute_script(
#     'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
#     name_of_the_element)
# print(all_attributes)


class ElementEnableChecker:

    def check_accessibility(self):
        driver.get("https://training.openspan.com/login")
        # returns True or False
        found_element_state = driver.find_element(By.ID, 'login_button').is_enabled()
        print(found_element_state)


class ElementVisabilityChecker:

    # in this case element CAN be found in DOM if it's invisible in UI
    # if element appears in DOM after some actions, at first this actions have to be executed and then
    # the availability of the element have to be checked
    # TODO rewrite this function (check hiding_selenium_doesnt_work.py)

    def check_visability_in_DOM(self):
        driver.get("https://www.aviasales.ru")
        # returns True or False
        found_elem_state = driver.find_element(By.XPATH, '//span[contains(text(),"Москва - Стамбул")]').is_displayed()
        print(found_elem_state)
        # Waiting 3 seconds for popup to appear
        cookies_popup = WebDriverWait(driver, timeout=3).until(
            lambda d: d.find_element(By.XPATH, "// div[ @class ='y2gjNiIS0o1RA_5Ebnkw']"))
        # time.sleep(1.5)
        # cookies_popup = driver.find_element(By.XPATH, "// div[ @class ='y2gjNiIS0o1RA_5Ebnkw']")
        cookies_accept_button = cookies_popup.find_element(By.TAG_NAME, "button")
        cookies_accept_button.click()
        time.sleep(1.5)
        uplevel_element = driver.find_element(By.XPATH, "//label[@for='directions_1']")
        uplevel_element.click()
        time.sleep(1.5)
        found_elem_state = driver.find_element(By.XPATH, '//span[contains(text(),"Москва - Стамбул")]').is_displayed()
        print(found_elem_state)


class CheckRadioWorker:

    def use_checkbox(self):
        driver.get("https://www.sugarcrm.com/uk/request-demo/")
        found_checkbox = driver.find_element(By.ID, 'interest_market_c0')
        if not found_checkbox.is_selected():
            found_checkbox.click()

    def use_radiobutton(self):
        driver.get("https://www.sugarcrm.com/uk/request-demo/")
        found_radiobutton_1 = WebDriverWait(driver, timeout=5).until(
            lambda d: d.find_element(By.ID, "doi0"))
        # found_radiobutton_1 = driver.find_element(By.ID, 'doi0')
        found_radiobutton_1.click()
        time.sleep(2)
        found_radiobutton_2 = driver.find_element(By.ID, 'doi1')
        if not found_radiobutton_2.is_selected():
            found_radiobutton_2.click()


class DropDownSelector:

    def one_line_selector(self):
        driver.get("https://www.salesforce.com/uk/form/signup/freetrial-sales-pe/?d=70130000000EqoP")
        cookies_popup = WebDriverWait(driver, timeout=3).until(
            lambda d: d.find_element(By.ID, "onetrust-banner-sdk"))
        cookies_accept_button = cookies_popup.find_element(By.TAG_NAME, "button")
        cookies_accept_button.click()
        found_dropdown = driver.find_element(By.NAME, "CompanyEmployees")
        dropdown = Select(found_dropdown)
        dropdown.select_by_index(3)
        # dropdown.select_by_value("50")
        # dropdown.select_by_visible_text("21 - 99 employees")

    def few_lines_selector(self):
        """It's a shit, but DOM is modifying, and it's hard to work with input"""
        driver.get("https://mdbootstrap.com/docs/standard/extended/multiselect/")
        found_dropdown = driver.find_element(By.XPATH,
                                             "//input[@class='form-control select-input placeholder-active active']")
        time.sleep(1)
        found_dropdown.click()
        dropdown_list = driver.find_element(By.XPATH, "//div[@class='select-options-list']")
        non_selected_options = dropdown_list.find_elements(By.CLASS_NAME, "select-option selected")
        selected_options = dropdown_list.find_elements(By.CLASS_NAME, "select-option")
        all_options = non_selected_options + selected_options
        # needful_options = ["One", "Two", "Seven"]
        needful_options = ["Two", "Seven"]
        for one_elem in all_options:
            selected_attr = one_elem.get_attribute("aria-selected")
            if selected_attr == "false" and one_elem.text in needful_options:
                # print(one_elem.text)
                # print("need to click")
                one_elem.click()

            elif selected_attr == "true" and one_elem.text in needful_options:
                # print(one_elem.text)
                # print("already selected")
                pass

            elif selected_attr == "true" and one_elem.text not in needful_options:
                # print(one_elem.text)
                # print("need to unselect")
                one_elem.click()

    def display_all_suggestions(self):
        driver.get("https://www.aviasales.ru/")
        departure_input = driver.find_element(By.XPATH, "//input[@id='origin']")
        departure_input.click()
        # time.sleep(1)
        departure_input.send_keys("Riga")

        destination_input = driver.find_element(By.XPATH, "//input[@id='destination']")
        destination_input.click()
        time.sleep(1)
        destination_input.send_keys("New")
        suggested_list = driver.find_element(By.XPATH, "//div[@data-test-id='autocomplete-dropdown']")
        all_children_of_list = suggested_list.find_elements(By.XPATH, ".//*")
        for one_elem in all_children_of_list:
            all_attributes = driver.execute_script(
                'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
                one_elem)
            # print(all_attributes)
            if all_attributes.get("class"):
                # print("прошло")
                if all_attributes["class"] == "autocomplete__suggestion-info":
                    # print("Прошло на второй уровень")
                    print(all_attributes["title"])

    def choose_one_suggestion(self):
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

    def choose_one_suggestion_hadle_exeption(self):
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

        # new_deli_option = wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, "//descendant::div[@class='autocomplete__suggestion-info' and @title='Дели, Индия']")))
        # new_deli_option.click()


class ScreenShooter:

    def make_screenshot(self):
        """Makes screenshot of special element and big screenshot
        they open from IDE, but doesn't open from windows explorer """
        driver.get("https://www.aviasales.ru/")
        example_button = driver.find_element(By.XPATH, "// div[ @class ='avia-form__submit']")
        example_button.screenshot("button_screenshot.png")

        # driver.get_screenshot_as_file(r"C:\\Users\\GennadiiMatveev\\Desktop\\Training\\Python_training\\STM\\Selenium\\Selenium_learning\\LearningSelenium.png")
        driver.save_screenshot("test_screenshot_1.png")


class WindowsHandler:

    def operate_windows(self):
        driver.get("https://www.aviasales.ru/")
        facebook_link = driver.find_element(By.XPATH, "// a[ @ title = 'Авиасейлс в Facebook']")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        facebook_link.click()
        parent_handler = driver.current_window_handle
        all_handlers = driver.window_handles
        # print(all_handlers)
        time.sleep(2)
        for handler in all_handlers:
            if handler != parent_handler:
                driver.switch_to.window(handler)
                time.sleep(2)
                driver.close()
        time.sleep(2)
        driver.switch_to.window(parent_handler)
        driver.close()


class IFramesHandler:

    """Always need to switch to frame and to child frame if needed"""

    def dive_into_child_iframe(self):
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        time.sleep(1)
        cookies_button = driver.find_element(By.XPATH, "// div [@id = 'accept-choices']")
        cookies_button.click()

        big_iframe = driver.find_element(By.XPATH, "// iframe [@id='iframeResult']")
        driver.switch_to.frame(big_iframe)

        driver.switch_to.frame(0)
        time.sleep(2)

        cookies_button_frame = driver.find_element(By.XPATH, "// *[ @ id = 'accept-choices']")
        cookies_button_frame.click()

        first_frame_button = driver.find_element(By.ID, "w3loginbtn")
        first_frame_button.click()


class AlertHandler:

    def change_website_code(self):
        """It can be an interesting case of changing div with all it's children,
        but it seems like the every child have to be separately changed"""
        code_field = driver.find_element(By.XPATH, "//div[@class='CodeMirror-code']")
        text_code = code_field.text
        print(text_code)
        driver.execute_script("arguments[0].textContent='Hello'", code_field)
        print()
        print(code_field.text)
        run_button = driver.find_element(By.XPATH, "//button[@id='runbtn']")
        run_button.click()
        print()
        print(code_field.text)

        # <!DOCTYPE html>
        # <html>
        # <body>
        #
        # <h1>The Window Object</h1>
        # <h2>The alert() Method</h2>
        #
        # <p id="demo">Click the button to display an alert box.</p>
        #
        # <button onclick="myFunction()">Try it</button>
        #
        # <script>
        # function myFunction() {
        #  var txt;
        #  var person = prompt ("Please enter your name", "Vasya");
        #  if (person == null || person == ""){
        #  txt = "User cancelled the prompt.";
        #  } else {
        #    txt = "Hello" + person + "! How are you today?";
        #  }
        #   document.getElementById("demo").innerHTML = txt;
        # }
        # </script>
        #
        # </body>
        # </html>

    def work_with_alert(self):
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
        time.sleep(1)
        cookies_button = driver.find_element(By.XPATH, "// div [@id = 'accept-choices']")
        cookies_button.click()
        # self.change_website_code()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        try_button = driver.find_element(By.TAG_NAME, "button")
        try_button.click()
        # driver.switch_to.alert.accept()
        Alert(driver).accept()
        """Also available alert.dismiss, alert.send_keys and alert.text to show text of alert
        Can be used driver.switch_to.alert.accept() or Alert(driver).accept()"""


class MouseHandler:

    def show_hidden_menu(self):
        driver.get("https://github.com/")
        hidden_point = driver.find_element(By.XPATH, "//div[normalize-space()='GitHub Sponsors']")
        achains = ActionChains(driver)
        menu_hider = driver.find_element(By.XPATH, "//button[normalize-space()='Open Source']")
        achains.move_to_element(menu_hider).perform()
        time.sleep(2)
        hidden_point.click()

    def make_right_and_double_click(self):
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        time.sleep(1)
        achains = ActionChains(driver)

        iframe = driver.find_element(By.XPATH, "//*[@id='gdpr-consent-notice']")
        driver.switch_to.frame(iframe)
        cookies_button = driver.find_element(By.XPATH, "//button [@id='save']")
        cookies_button.click()

        right_click_button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        achains.context_click(right_click_button).perform()
        copy_elem = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
        copy_elem.click()
        Alert(driver).accept()

        double_click_button = driver.find_element(By.XPATH,
                                                  "//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(double_click_button).perform()
        Alert(driver).accept()


class SliderHandler:

    def handle_bad_slider(self):
        """Here value is changed by DOM and input; not by slider"""
        # driver.get("https://www.gigantti.fi/kodinkoneet/pyykinpesu-ja-kuivaus")
        #
        # achains = ActionChains(driver)
        # achains.move_by_offset(15, 15).perform()
        # time.sleep(1)
        # cookies_button = driver.find_element(By.XPATH, "//button [@class= 'coi-banner__accept']")
        # cookies_button.click()

        driver.get("https://kauppa.dna.fi/laitteet/puhelimet")
        time.sleep(1)
        cookies_button = driver.find_element(By.XPATH, "//button [@id= 'onetrust-accept-btn-handler']")
        cookies_button.click()

        # 1st - change value of slider in DOM
        min_price_slider = driver.find_element(By.XPATH, "//input [@ data-testid= 'price-slider-range-input-min']")
        value_of_min = min_price_slider.get_attribute("value")
        print(value_of_min)
        # driver.execute_script("arguments[0].setAttribute(value,arguments[1])", price_slider, 50000)
        driver.execute_script("arguments[0].value = 50000;", min_price_slider)
        print(min_price_slider.get_attribute("value"))

        # 2nd - clean and them write new price in input
        # min_price_field = driver.find_element(By.XPATH, "//input[@id='product-list-slide-input-min']")
        # min_price_field.clear()
        # time.sleep(1)
        # min_price_field.send_keys(128)

    def handle_slider(self):
        """This function doesn't work because on DNA website slider point are not accessible from DOM,
        but in general it should work when the dot can be used"""

        driver.get("https://kauppa.dna.fi/laitteet/puhelimet")
        time.sleep(1)
        cookies_button = driver.find_element(By.XPATH, "//button [@id= 'onetrust-accept-btn-handler']")
        cookies_button.click()

        min_price_slider = driver.find_element(By.XPATH, "//input [@ data-testid= 'price-slider-range-input-min']")

        # 1st method -
        ActionChains(driver).drag_and_drop_by_offset(min_price_slider, 100, 0).perform()

        # 2nd method - click (hold) - move - release (stop holding)
        ActionChains(driver).click_and_hold(min_price_slider).pause(1).move_by_offset(100, 0).release().perform()

        # 3rd method - added a move_to_element to better clarify with which element action is happen
        ActionChains(driver).move_to_element(min_price_slider).click_and_hold(min_price_slider).move_by_offset(100, 0)\
            .release().perform()


class DragAndDropper:

    def drag_and_drop(self):
        driver.get("https://jqueryui.com/droppable/")
        frame = driver.find_element(By.XPATH, "// iframe [@ class = 'demo-frame']")
        driver.switch_to.frame(frame)

        draggable_elem = driver.find_element(By.ID, "draggable")
        droppable_elem = driver.find_element(By.ID, "droppable")

        """Drag and drop from one element to another"""
        # ActionChains(driver).drag_and_drop(draggable_elem, droppable_elem).perform()

        """Drag and drop one element to coordinates - don't go to special coordinates, it moves
        on such amount of x and y from the current location from draggable element"""
        ActionChains(driver).drag_and_drop_by_offset(draggable_elem, 138, 50).perform()


class WaitsOperator:
    """
    Implicit wait - for whole system. После его написания, в КАЖДОЙ строке ниже все действия будут пытаться выполниться
    в течении какого-то заданного времени и только потом падать в ошибку, если что-то не так. Задаётся только время
    ожидания, без конткретного результата, то есть если все строки ниже успешно выполняются раньше отведённого
    времени - ожидание снимается

    Explicit wait - for special element. Есть чёткое условие выполнения, либо падает в ошибку через определённое время

    Fluent wait - possible to specify poll frequency and maximum time. Also can ignored_exceptions can be set.
    По факту это Explicit wait, но есть ещё уставноска частоты обновления и игнорирование каких-то исключений
    """
    
    def implicit_wait_handler(self):
        driver.get("https://www.aviasales.ru/")
        driver.implicitly_wait(5)
        search_button = driver.find_element(By.XPATH, "// div[ @class ='avia-form__submit']")
        # fake_element = driver.find_element(By.XPATH, "// div[ @class ='fake']")
        calendar_input_0 = driver.find_element(By.XPATH, "//div[@class='trip-duration__input-wrapper --departure']")

    def explicit_wait_handler(self):
        driver.get("https://www.aviasales.ru/")
        wait = WebDriverWait(driver, 10)

        destination_input = driver.find_element(By.XPATH, "//input[@id='destination']")
        destination_input.click()
        destination_input.send_keys("New")

        destination_suggestions = destination_input.find_element(
            By.XPATH, '//input[@id="destination"]//following::div[@class="autocomplete__dropdown"]')
        # print(destination_suggestions)
        all_suggestions = wait.until(
            EC.presence_of_element_located((By.XPATH, '//descendant::div[@class="autocomplete__suggestion-info"]'))).\
            find_elements(By.XPATH, '//descendant::div[@class="autocomplete__suggestion-info"]')
        # выражение выше заменяет выражение ниже
        # time.sleep(1)
        # all_suggestions = destination_suggestions.find_elements(
        #     By.XPATH, '//descendant::div[@class="autocomplete__suggestion-info"]')

        for one_elem in all_suggestions:
            print(one_elem.tag_name)
            print(one_elem.get_attribute("title"))

    def fluent_wait_handler(self):
        driver.get("https://www.aviasales.ru/")
        wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

        destination_input = driver.find_element(By.XPATH, "//input[@id='destination']")
        destination_input.click()
        destination_input.send_keys("New")

        destination_suggestions = destination_input.find_element(By.XPATH, '//input[@id="destination"]//following::div[@class="autocomplete__dropdown"]')
        all_suggestions = wait.until(
            EC.presence_of_element_located((By.XPATH, '//descendant::div[@class="autocomplete__suggestion-info"]'))). \
            find_elements(By.XPATH, '//descendant::div[@class="autocomplete__suggestion-info"]')

        # выражение выше заменяет выражение ниже
        # time.sleep(1)
        # all_suggestions = destination_suggestions.find_elements(
        #     By.XPATH, '//descendant::div[@class="autocomplete__suggestion-info"]')

        for one_elem in all_suggestions:
            print(one_elem.tag_name)
            print(one_elem.get_attribute("title"))






if __name__ == "__main__":
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    finder_1 = FindElement()
    finder_2 = FindElements()
    finder_3 = GetAttributeValue()
    finder_4 = ElementEnableChecker()
    finder_5 = ElementVisabilityChecker()
    finder_6 = CheckRadioWorker()
    finder_7 = DropDownSelector()
    finder_8 = ScreenShooter()
    finder_9 = WindowsHandler()
    finder_10 = IFramesHandler()
    finder_11 = AlertHandler()
    finder_12 = MouseHandler()
    finder_13 = SliderHandler()
    finder_14 = DragAndDropper()
    finder_15 = WaitsOperator()

    # finder_1.locate_by_id('destination')
    # finder_1.locate_dynamic_element_start()
    # finder_1.locate_dynamic_element_contains()
    # finder_1.locate_parent_element()
    # finder_1.locate_by_xpath('//input[@id="destination"]')
    # finder_1.locate_by_link_text('О н')
    # finder_2.locate_elements_by_name('a')
    # finder_3.get_value()
    # finder_4.check_accessibility()
    # finder_5.check_visability_in_DOM()
    # finder_6.use_checkbox()
    # finder_6.use_radiobutton()
    # finder_7.one_line_selector()
    # finder_7.few_lines_selector()
    # finder_7.display_all_suggestions()
    # finder_7.choose_one_suggestion()
    finder_7.choose_one_suggestion_hadle_exeption()
    # finder_8.make_screenshot()
    # finder_9.operate_windows()
    # finder_10.dive_into_child_iframe()
    # finder_11.work_with_alert()
    # finder_12.show_hidden_menu()
    # finder_12.make_right_and_double_click()
    # finder_13.handle_slider()
    # finder_14.drag_and_drop()
    # finder_15.implicit_wait_handler()
    # finder_15.explicit_wait_handler()
    # finder_15.fluent_wait_handler()
