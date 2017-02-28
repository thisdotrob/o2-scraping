from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from elements import ElementIds

ENTRY_PAGE_URL = "http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk"
INVALID_COUNTRY_MSG = "Please enter a valid country name"
TIMEOUT_SECS = 10

class CountryScraper:
    def __init__(self, country):
        self.country = country

    def get_landline_rate(self):
        self._initialise_driver()
        self._visit_entry_page()
        self._select_country()
        self._select_pay_monthly()
        rate = self._extract_landline_rate_from_table()
        self._close_driver()
        return rate

    def _initialise_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(TIMEOUT_SECS)

    def _visit_entry_page(self):
        self.driver.get(ENTRY_PAGE_URL)

    def _select_country(self):
        country_input = self.driver.find_element_by_id(ElementIds.COUNTRY_INPUT)
        country_input.send_keys(self.country + Keys.RETURN)
        displayed_text = country_input.get_attribute('value')
        if displayed_text == INVALID_COUNTRY_MSG:
            raise ValueError

    def _select_pay_monthly(self):
        pay_monthly_button = self.driver.find_element_by_id(ElementIds.PAY_MONTHLY_BUTTON)
        pay_monthly_button.click()

    def _extract_landline_rate_from_table(self):
        call_rates_table = self.driver.find_element_by_id(ElementIds.CALL_RATES_TABLE)
        landline_rate_row = call_rates_table.find_elements_by_tag_name("tr")[0]
        landline_rate_cell = landline_rate_row.find_elements_by_tag_name("td")[1]
        return landline_rate_cell.text

    def _close_driver(self):
        self.driver.close()
