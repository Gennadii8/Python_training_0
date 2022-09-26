import os

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
# # free-proxy library
# from fp.fp import FreeProxy
# # fake-useragent library
# from fake_useragent import UserAgent

# options = Options()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.maximize_window()

try:

    import sys
    import os

    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    from fp.fp import FreeProxy
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver import Chrome
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    import time
    print('all module are loaded ')

except Exception as e:

    print("Error ->>>: {} ".format(e))


class Spoofer:

    # def __init__(self, country_id=['US'], rand=True, anonym=True):
    def __init__(self):
        # self.country_id = country_id
        # self.rand = rand
        # self.anonym = anonym
        self.userAgent = self.get()

    def get(self):
        ua = UserAgent()
        # proxy = FreeProxy(country_id=self.country_id, rand=self.rand, anonym=self.anonym).get()
        # ip = proxy.split("://")[1]
        return ua.random


class DriverOptions:

    def __init__(self):

        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        # self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--incognito")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("disable-infobars")

        self.helperSpoofer = Spoofer()

        self.options.add_argument('user-agent={}'.format(self.helperSpoofer.userAgent))
        # self.options.add_argument('--proxy-server=%s' % self.helperSpoofer.ip)


class WebDriver(DriverOptions):

    def __init__(self, path=''):
        DriverOptions.__init__(self)
        self.driver_instance = self.get_driver()

    def get_driver(self):

        print("""
        UserAgent: {}
        """.format(self.helperSpoofer.userAgent))

        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True

        # path = os.path.join(os.getcwd(), '../windowsDriver/chromedriver.exe')

        # driver = webdriver.Chrome(executable_path=path, options=self.options)
        # options = Options()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })

        return driver


def main():

    driver = WebDriver()
    driverinstance = driver.driver_instance
    # driverinstance.get("https://www.expressvpn.com/what-is-my-ip")

    driverinstance.get("https://www.ozon.ru/category/gornye-velosipedy-31943/")
    # time.sleep(1.5)
    # change_address_button = driver.find_element(By.XPATH, "//div[@class='cq3 ui-c']//button[@type='button']")
    change_address_button = WebDriverWait(driverinstance, timeout=3).until(
        lambda d: d.find_element(By.XPATH, "//div[@class='cq5 ui-c']//button[@type='button']"))
    change_address_button.click()
    driverinstance.delete_cookie("AREA_ID")
    driverinstance.add_cookie({"name": "AREA_ID", "value": "5911"})
    # driver.set_window_size(1024, 768)
    time.sleep(3)
    driverinstance.refresh()


    time.sleep(5)
    print("done")


if __name__ == "__main__":
    main()




# class CheckBoxWorker:
#
#     # big case for opening OZON, changing country and region and then working with checkboxes
#     def use_checkbox(self):
#         driver.get("https://www.ozon.ru/category/gornye-velosipedy-31943/")
#         # time.sleep(1.5)
#         # change_address_button = driver.find_element(By.XPATH, "//div[@class='cq3 ui-c']//button[@type='button']")
#         change_address_button = WebDriverWait(driver, timeout=3).until(
#             lambda d: d.find_element(By.XPATH, "//div[@class='cq3 ui-c']//button[@type='button']"))
#         change_address_button.click()
#         driver.delete_cookie("AREA_ID")
#         driver.add_cookie({"name": "AREA_ID", "value": "5911"})
#         # driver.set_window_size(1024, 768)
#         time.sleep(3)
#         driver.refresh()


        # time.sleep(1.5)
        # current_country = driver.find_element(By.XPATH, "// span[ @class ='ui-c3 ui-e6'] // span[1]")
        # current_country.click()

