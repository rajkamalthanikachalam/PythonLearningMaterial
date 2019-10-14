from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  #for firefox only

# For Chrome, no need of desired capabilities initialization
driver = webdriver.Chrome("C://Automation//Python//drivers//chromedriver.exe")

# For firefox, desired capabilities must be initialized
# Uncomment below line to execute in Firefox
# caps = DesiredCapabilities.FIREFOX
# caps["marionette"] = True
# caps["binary"] = "C://Program Files (x86)//Mozilla Firefox//Firefox.exe"
# driver = webdriver.Firefox(capabilities=caps, executable_path="C://Automation//Python//drivers//geckodriver.exe")

driver.get("https://www.google.com/")
title = driver.title
assert "Google" in title

print(title)
driver.quit()
