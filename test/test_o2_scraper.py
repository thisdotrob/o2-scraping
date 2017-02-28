from unittest import TestCase
from o2_scraper import O2Scraper

COUNTRY_NAMES = ["Canada", "Germany"]

class CountryScraperKlass:
    def __init__(self, name):
        pass

    def get_landline_rate(self):
        return "£99"

class ValueErrorRaisingCountryScraperKlass(CountryScraperKlass):
    def get_landline_rate(self):
        raise ValueError

class ScrapeTest(TestCase):
    def test_retrieving_landline_rates(self):
        scraper = O2Scraper(COUNTRY_NAMES, CountryScraperKlass)
        landline_rates = scraper.get_landline_rates()
        self.assertEqual(landline_rates, ["£99", "£99"])

    def test_handling_invalid_country_names(self):
        scraper = O2Scraper(COUNTRY_NAMES, ValueErrorRaisingCountryScraperKlass)
        landline_rates = scraper.get_landline_rates()
        self.assertEqual(landline_rates, ["Invalid name", "Invalid name"])
