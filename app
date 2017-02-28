#!/usr/bin/python

import sys
from o2_scraper import O2Scraper

def main():
    country_names = sys.argv[1:]
    scraper = O2Scraper(country_names)
    for country_name, rate in zip(country_names, scraper.get_landline_rates()):
        print(f"{country_name}: {rate}")

if __name__ == '__main__':
    main()
