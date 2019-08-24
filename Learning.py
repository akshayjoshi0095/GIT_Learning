from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver=webdriver.Chrome(executable_path='path where your chrome driver exist upto the name + extension of file')

driver.close()                  ### close only the focussed browser
driver.quit()                   ### close all the opened in the focussed tab


''' 
>> imp imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait 
	
	
>>  drag_n_drop, forward, bacjword, refresh, click, right_click, scroll
    
>>  Conditional Command     ### always return True/False
    > is_enabled()   
    >is_selected()
    >is_dispalyed()
    
>> self.driver.find_element_by_xpath(xpath)                      ## finding xpath
    self.driver.find_element_by_xpath(xpath).click()             ## click 
    self.driver.find_element_by_xpath(xpath).send_keys(value1)     # input
    self.driver.find_element_by_xpath(xpath).clear()            
    self.driver.find_element_by_xpath(xpath).text                  # to get the text 
    
    
>>Waits
    >self.driver.implicitly_wait(sec)   
    
Implicit Wait: Implicit waits are used to provide a default waiting time (say 30 seconds) between each consecutive test step/command across the
                entire test script. Thus, the subsequent test step would only execute when the 30 seconds have elapsed after executing the previous 
                test step/command.

Explicit Wait: Explicit waits are used to halt the execution till the time a particular condition is met or the maximum time has elapsed. 
                Unlike Implicit waits, explicit waits are applied for a particular instance only.
    
    
	
	
    
'''