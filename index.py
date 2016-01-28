from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome()
driver.get("http://www.swagbucks.com/")
driver.maximize_window()
driver.find_element_by_id("sbGlobalNavLoginBtn").click()     # to go to login page

elem1= driver.find_element_by_id("sbxJxRegEmail")
elem1.send_keys("enter your email")
elem2= driver.find_element_by_id("sbxJxRegPswd")
elem2.send_keys("password")
driver.find_element_by_id("loginBtn").click()

#dealing with alert/pop-up
driver.find_element_by_id("swagButtonModalExit").click()


Daily_poll= driver.find_element_by_id("sbMainNavSectionListItemToDoListDailyPoll")

Daily_poll.click()
#submitting the choice
a=[]
a=driver.find_elements_by_class_name("pollCheckbox");
a[1].click()
#vote & earn 1 SB
driver.find_element_by_class_name("todayPoll").click()

#to colse the window

driver.quit()

