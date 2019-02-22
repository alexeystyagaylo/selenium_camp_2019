

def is_element_present(driver):
  try:
      driver.find_element_by_xpath(element)
      return True
  except:
      return False

if is_element_present(driver) is True:
  # do something