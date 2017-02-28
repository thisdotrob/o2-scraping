from selenium import webdriver

def get_title():
    driver = webdriver.Chrome()
    driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")
    title = driver.title
    driver.quit()
    return title
