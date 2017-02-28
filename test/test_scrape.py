from unittest import TestCase
from scrape import get_title

class ScrapeTest(TestCase):
    def test_retrieving_entry_page_title(self):
        title = get_title()
        self.assertEqual(title, "O2 | International | International Caller Bolt On")
