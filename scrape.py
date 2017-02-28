from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from elements import ElementIds

ENTRY_PAGE_URL = "http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk"
TIMEOUT_SECS = 5

def get_landline_rate(country):
    driver = webdriver.Chrome()
    driver.implicitly_wait(TIMEOUT_SECS)
    driver.get(ENTRY_PAGE_URL)
    country_input = driver.find_element_by_id(ElementIds.COUNTRY_INPUT)
    country_input.send_keys(country + Keys.RETURN)
    pay_monthly_button = driver.find_element_by_id(ElementIds.PAY_MONTHLY_BUTTON)
    pay_monthly_button.click()
    call_rates_table = driver.find_element_by_id(ElementIds.CALL_RATES_TABLE)
    landline_rate_row = call_rates_table.find_elements_by_tag_name("tr")[0]
    landline_rate = landline_rate_row.find_elements_by_tag_name("td")[1].text

    driver.close()

    return landline_rate
