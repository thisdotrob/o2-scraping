from unittest import TestCase
from o2_scraper import O2Scraper

COUNTRY_NAMES = ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]

class ScrapeTest(TestCase):
    def test_retrieving_landline_rates(self):
        scraper = O2Scraper(COUNTRY_NAMES)
        landline_rates = scraper.get_landline_rates()
        self.assertEqual(landline_rates, ["£1.50", "£1.50", "£1.50", "£2.00", "£1.50", "£1.50"])
