from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoAutosuggest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def demo_autosuggest_dropdown(self):
        self.driver.get("https://www.yatra.com/")
        self.driver.maximize_window()

        depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)

        going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        going_to.click()
        going_to.send_keys("New York")

        search_results = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))
        print(len(search_results))
        for result in search_results:
            print(result.text)
            if "New York (JFK)" in result.text:
                result.click()
                break

        origin = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']")))
        origin.click()

        all_dates = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))
        for date in all_dates:
            if date.get_attribute("data-date") == "22/04/2024":
                date.click()
                break

        self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()

    def __del__(self):
        self.driver.quit()

# Instantiate and run the script
dauto = DemoAutosuggest()
dauto.demo_autosuggest_dropdown()
