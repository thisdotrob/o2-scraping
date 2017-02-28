# o2 scraping

Python application for scraping call costs from http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk

## Installation

This project requires chromedriver to be installed:
```shell
$ brew install chromedriver
```

This project uses [pipenv](http://docs.pipenv.org/en/latest/), enter the following in your terminal to install dependencies and run the application:
```shell
$ pipenv install
$ pipenv shell
$ python app "Canada" "Germany" "Iceland" "Pakistan" "Singapore" "South Africa"
```

To run the tests, use:
```shell
$ python -m unittest -v
```
