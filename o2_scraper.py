from country_scraper import CountryScraper

class O2Scraper:
    def __init__(self, country_names, CountryScraperKlass=CountryScraper):
        self.country_names = country_names
        self.CountryScraper = CountryScraperKlass

    def get_landline_rates(self):
        country_scrapers = [self.CountryScraper(name) for name in self.country_names]
        rates = [self._get_rate_if_valid(country_scraper) for country_scraper in country_scrapers]
        return rates

    def _get_rate_if_valid(self, country_scraper):
        try:
            return country_scraper.get_landline_rate()
        except ValueError as ex:
            return "Invalid name"
