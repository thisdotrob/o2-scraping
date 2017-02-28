from unittest import TestCase
from scrape import CountryScraper

class ScrapeTest(TestCase):
    def test_retrieving_landline_rate(self):
        canada_scraper = CountryScraper("Canada")
        pakistan_scraper = CountryScraper("Pakistan")
        canada_landline_rate = canada_scraper.get_landline_rate()
        pakistan_landline_rate = pakistan_scraper.get_landline_rate()
        self.assertEqual(canada_landline_rate, "£1.50")
        self.assertEqual(pakistan_landline_rate, "£2.00")
