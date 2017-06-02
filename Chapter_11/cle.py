#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

browser = webdriver.Firefox()

email = sys.argv[1] 
text_string = ' '.join(sys.argv[2:])
subject_line = "From cle.py script"

if email != '' and text_string != '':

    browser.get('http://gmail.com')
    email_input_elem = browser.find_element_by_id('identifierId')
    email_input_elem.send_keys('')
    email_next_button = browser.find_element_by_class_name('RveJvd')
    email_next_button.click()
    wait = WebDriverWait(browser, 5)
    pass_input_elem = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    pass_input_elem.send_keys('')
    pass_next_button = wait.until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
    pass_next_button.click()
    compose_button_elem = wait.until(EC.element_to_be_clickable((By.XPATH("//div[@type='button']")))).click()
    
else:
    
    print("Command line format is \"cle email stringoftext\"")
