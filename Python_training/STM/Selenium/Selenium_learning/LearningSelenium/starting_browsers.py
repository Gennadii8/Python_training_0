"""Without Options"""
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# driver.get("https:\\google.com")

#
# """With Options Chrome"""
# # below method with options
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# # options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.maximize_window()
#
# driver.get("https:\\google.com")
# print(driver.title)
# # driver.implicitly_wait(5)
# # driver.close()
#
# """With Options Mozilla"""
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.options import Options
#
# options = Options()
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
# driver.maximize_window()
#
# driver.get("https:\\google.com")
# print(driver.title)
# # driver.implicitly_wait(5)
# # driver.close()


# """With Options Edge"""
# from selenium import webdriver
# from selenium.webdriver.edge import service
#
# edgeOption = webdriver.EdgeOptions()
# edgeOption.use_chromium = True
# edgeOption.add_argument("start-maximized")
# edgeOption.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
# s = service.Service(r'C:\BrowserDrivers\msedgedriver.exe')
# driver = webdriver.Edge(service=s, options=edgeOption)
# driver.get("https:\\google.com")


"""With Options Internet Explorer
it redirect to Edge - google opens there"""
from selenium import webdriver
from selenium.webdriver.ie import service

ieOption = webdriver.IeOptions()
ieOption.use_chromium = True
ieOption.add_argument("start-maximized")
ieOption.binary_location = r"C:\Program Files (x86)\Internet Explorer\iexplore.exe"
s = service.Service(r'C:\BrowserDrivers\IEDriverServer.exe')
driver = webdriver.Ie(service=s, options=ieOption)
driver.get(r"https:\\google.com")



"""Old method with executable_path"""
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path="C:\\BrowserDrivers\\chromedriver.exe")
#
# driver.get("https:\\google.com")



