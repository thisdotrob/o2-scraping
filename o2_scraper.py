from country_scraper import CountryScraper

class O2Scraper:
    def __init__(self, country_names):
        self.country_names = country_names

    def get_landline_rates(self):
        country_scrapers = [CountryScraper(name) for name in self.country_names]
        rates = [country_scraper.get_landline_rate() for country_scraper in country_scrapers]
        return rates
