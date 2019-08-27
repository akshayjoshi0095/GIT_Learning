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
    
    

	
	
Gitbash Cmds

Git is a source code management software
TFS= team foundation server by microsoft
SVN by apache

featues-Tracking of files, Versioning,compare code, Merge branch and compare branch


Github- is webbased central repository hosting services

My git clone url -	https://github.com/akshayjoshi0095/GIT_Learning.git


# To know the git version
	$ git --version
	
# To configure username
	$ git config global --user.name 'Type username'

#To configure useremail
	$ git config global --user.email 'Type email'

# To retrieve configured username
	$ git config user.name

# To retrieve configured useremial
	$ git config user.email
	
# To enter into particular directory
	$ cd D:
	
# To create a foldername
	$ mkdir 'foldername'
	
# To enter into that folder
	$ cd foldername/
	
# To know the current location
	$ pwd
	
# for creating local repository
	$ git init
	
# To check how many files is in untracked status and staged status
	$ git status

# To convert any file from untracked status to statged status
	$ git add filename				#### for making any particular file staged
	$ git add .						#### for making all file staged
	
# To convert all the staged status files to tracked status
	$ git commit -m 'Type any message'

# To know whether our local repository to linked to any remote repository
	$ git remote -v
	## if already linked would be present then this cmd will return fetch and push url

# To linked local repository to any remote repository
	$ git remote add origin 'remote repository url'				### after this cmd give $ git remote -v and check

# To push all the tracked file(changes made into tracked file) in remote repository
	$ git push origin master
	
# To take any project from remote repository into local repository
	$ git clone 'user git clone url'

# To take the latest project into a local repository which is already linked to remote repository from the remote repository
	$ git pull origin master

# To check the no of branch present in the repository
	$ git branch

# To create a new branch
	$ git branch newbranchname

# To enter into newly created branch
	$ git checkout newbranchname

# way to take the content of branch into our machine
	$ git clone 'giturl'		## this cmd will bring only the content of master branch into your local machine
	$ git branch newbranchname	## this cmd will overrides the content brought as part of master branch and chnge the content to 	    the content present in branch
	
# way to merge the new changes made in the local branch
	$ git checkout master
	$ git merge branchname     #### that branchname whose content you want to push into the master branch and update it.
	$ git push -u origin master
	
	
'''
