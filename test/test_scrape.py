from unittest import TestCase
from scrape import get_title, get_landline_rate

class ScrapeTest(TestCase):
    def test_retrieving_entry_page_title(self):
        title = get_title()
        self.assertEqual(title, "O2 | International | International Caller Bolt On")

    def test_retrieving_landline_rate(self):
        canada_landline_rate = get_landline_rate("Canada")
        pakistan_landline_rate = get_landline_rate("Pakistan")
        self.assertEqual(canada_landline_rate, "£1.50")
        self.assertEqual(pakistan_landline_rate, "£2.00")
