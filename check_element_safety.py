from selenium.common.exceptions import NoSuchElementException


def is_element_present(driver):
    try:
        driver.find_element_by_xpath(element)
        return True
    except NoSuchElementException:
        return False

if is_element_present(driver) is True:
  # do something