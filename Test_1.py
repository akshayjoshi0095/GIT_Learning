from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time

class Learning:
    #def __init__(self):
        # self.driver=webdriver.Chrome()
        # time.sleep(2)
        # print 'session:{}, url:{}, title:{}'.format(self.driver.session_id,self.driver.command_executor._url,self.driver.title)
        # self.driver.maximize_window()
        # self.driver.get('https://jqueryui.com')
        # self.driver.implicitly_wait(5)

    def drag_drop_1(self):
        self.driver.find_element_by_xpath('//div[@id="sidebar"]//a[text()="Droppable"]').click()
        time.sleep(3)
        action = ActionChains(self.driver)
        self.driver.switch_to.frame(0)
        ele1 = self.driver.find_element_by_xpath('//div[@id="draggable"]')
        ele2 = self.driver.find_element_by_xpath('//div[@id="droppable"]')
        action.drag_and_drop(ele1, ele2).perform()
        print 'drag_drop_1 accomplished'

    def drag_drop_2(self):
        self.driver.find_element_by_xpath('//div[@id="sidebar"]//a[text()="Droppable"]').click()
        self.driver.switch_to.frame(0)
        action=ActionChains(self.driver)
        ele1 = self.driver.find_element_by_xpath('//div[@id="draggable"]')
        ele2 = self.driver.find_element_by_xpath('//div[@id="droppable"]')
        action.click_and_hold(ele1).move_to_element(ele2).release(ele2).perform()
        print 'drag_drop_2 accomplished'

    def right_click(self):
        action=ActionChains(self.driver)
        ele1=self.driver.find_element_by_xpath('//div[@id="sidebar"]//a[text()="Droppable"]')
        action.context_click(ele1).perform()
        print 'right click accomplished'
        self.driver.close()

    def Refresh_Backward_Forward(self):
        self.driver.find_element_by_xpath('//div[@id="sidebar"]//a[text()="Droppable"]').click()
        time.sleep(1)
        self.driver.switch_to.frame(0)
        action = ActionChains(self.driver)
        ele1 = self.driver.find_element_by_xpath('//div[@id="draggable"]')
        ele2 = self.driver.find_element_by_xpath('//div[@id="droppable"]')
        action.click_and_hold(ele1).move_to_element(ele2).release(ele2).perform()

        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)


        self.driver.find_element_by_xpath('//div[@id="sidebar"]//a[text()="Resizable"]').click()
        time.sleep(2)
        self.driver.back()

        self.driver.switch_to.frame(0)
        time.sleep(5)
        action.drag_and_drop(ele1, ele2).perform()
        time.sleep(1)
        self.driver.refresh()

        time.sleep(2)
        self.driver.forward()
        print 'refresh, forward, backward accomplished'

    def Scroll(self):
        ele1 = self.driver.find_element_by_xpath(
            '//body[@class="jquery-ui home page page-id-33 page-template-default page-slug-index single-author singular"]')
        time.sleep(1)
        ele1.send_keys(Keys.END)
        time.sleep(2)
        ele1.send_keys(Keys.HOME)

        print 'scroll up & down accomplished'


    # def implicit_explicit_wait(self):
    #     self.driver=webdriver.Chrome()
    #     time.sleep(2)
    #     print 'session:{}, url:{}, title:{}'.format(self.driver.session_id,self.driver.command_executor._url,self.driver.title)
    #     self.driver.maximize_window()
    #     self.driver.get('https://www.expedia.com')
    #     self.driver.implicitly_wait(1)
    #     time.sleep(10)
    #     ele1=self.driver.find_element_by_xpath('(//input[@class="clear-btn-input gcw-storeable text gcw-origin gcw-required gcw-distinct-locations"])[1]')
    #     print(ele1.is_enabled())
    #     ele1.clear()
    #     ele1.send_keys('Bengaluru, India (BLR-Kempegowda Intl.)')
    #     ele1.send_keys(Keys.TAB)
    #
    #     # if ele1.is_enabled()=='True':
    #     #     ele1.clear()
    #     #     ele1.send_keys('Bengaluru, India (BLR-Kempegowda Intl.)')
    #
    #     ele2=self.driver.find_element_by_xpath('(//input[@class="clear-btn-input gcw-storeable text gcw-destination gcw-required gcw-distinct-locations"])[1]')
    #     if ele2.is_enabled()==True:
    #         ele2.clear()
    #         ele2.send_keys('Delhi, India (DEL-Indira Gandhi Intl.)')
    #         ele2.send_keys(Keys.TAB)
    #
    #     ele3=self.driver.find_element_by_xpath('//input[@id="package-departing-hp-package"]')
    #     if ele3.is_enabled()==True:
    #         ele3.clear()
    #         ele3.send_keys('11/01/2019')
    #         ele3.send_keys(Keys.TAB)
    #
    #     ele4=self.driver.find_element_by_xpath('//input[@id="package-returning-hp-package"]')
    #     if ele4.is_enabled()==True:
    #         ele4.clear()
    #         ele4.send_keys('11/10/2019')
    #         ele4.send_keys(Keys.TAB)
    #         ele4.send_keys(Keys.ENTER)
    #
    #     time.sleep(10)
    #     wait=WebDriverWait(self.driver,10)
    #     ele6=self.driver.find_element_by_xpath('//body[@class="wrap cf l-results  wizard-responsive dated flexible-shopping package-type-fh"]')
    #     ele6.send_keys(Keys.END)
    #     time.sleep(5)
    #     ele6.send_keys(Keys.HOME)
    #     print'scroll done'
    #
    #
    #     wait.until(expected_conditions.element_to_be_clickable('//input[@name="hideRegionId"]'))
    #     self.driver.find_element_by_xpath('//input[@name="hideRegionId"]').click()


#(//button[@class="trigger-utility menu-trigger btn-utility btn-secondary dropdown-toggle theme-standard pin-left menu-arrow gcw-component gcw-traveler-amount-select gcw-component-initialized"])[last()]


obj=Learning()
#obj.drag_drop_1()
#obj.drag_drop_2()
#obj.right_click()
#obj.Refresh_Backward_Forward()
obj.implicit_explicit_wait()




