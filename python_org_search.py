from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.use_chromium = True

driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe", options=options)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()