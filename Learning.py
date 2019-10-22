from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import WebDriverWait


import time


driver=webdriver.Chrome(executable_path='path where your chrome driver exist upto the name + extension of file')

driver.close()                  ### close only the focussed tab only if only one tab is open in the window than window will get closed
driver.quit()                   ### close the focussed window


''' 
>> imp imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait 
	
	
>>Actions func (from selenium.webdriver.common.action_chains import ActionChains)

    >>Drag n drop
        >action=ActionChains(self.driver)
        >action.drag_and_drop(ele1,ele2).perform()
    
    >>Drag n drop
        >action=ActionChains(self.driver)
        >action.click_and_hold(ele1).move_to_element(ele2).release(ele2).perform()
        
    >>Rightclick
        >action=ActionChains(self.driver)
        >action.context_click(ele1).perform()
    
    >>Doubleclick
        >action=ActionChains(self.driver)
        >action.double_click(ele1).perform()
   
        
>>Navigate function
    
    >forward
        >self.driver.forward()
    
    >back
        >self.driver.back()
    
    >Refresh
        >self.driver.refresh()
        
    >scroll
        >ele1.send_keys(Keys.END)
        >time.sleep(2)
        >ele1.send_keys(Keys.HOME)
            
    >scroll
        >self.driver.execute_script(javascript)
        
        
    
>>  Conditional Command     ### always return True/False  but while using them in automation we have to give condition like this  
    > is_enabled()              e.g element1.is_enabled()!='True' or element1.is_enabled()=='True'
    >is_selected()
    >is_dispalyed()
    
>> self.driver.find_element_by_xpath(xpath)                      ## finding xpath
    self.driver.find_element_by_xpath(xpath).click()             ## click 
    self.driver.find_element_by_xpath(xpath).send_keys(value1)     # input
    self.driver.find_element_by_xpath(xpath).clear()            
    self.driver.find_element_by_xpath(xpath).text                  # to get the text 
    
    
>>Waits    
    >from selenium.webdriver.support.ui import WebDriverWait
    >from selenium.webdriver.support import expected_conditions
    >from selenium.webdriver.common.by import By
    
Implicit Wait: Implicit waits are used to provide a default waiting time (say 30 seconds) between each consecutive test step/command across the
                entire test script. Thus, the subsequent test step would only execute when the 30 seconds have elapsed after executing the previous 
                test step/command.
    >>self.driver.implicitly_wait(sec)
    
    
Explicit Wait: Explicit waits are used to halt the execution till the time a particular condition is met or the maximum time has elapsed. 
                Unlike Implicit waits, explicit waits are applied for a particular instance only.
    >>wait=WebDriverWait(self.driver,10)
      wait.until(expected_conditions.element_to_be_clickable((By.XPATH,next)))
 
 
>>Select Function (from selenium.webdriver.support.ui import Select)  
    drp=Select(ele2)
    drp.select_by_visible_text('text')
    drp.select_by_index(give no. as per the html)
    drp.select_by_value('value as per html')

    l=drp.options
    print 'no of option in dropdown', len(l)
    for i in l:
        print i.text
    
    
>> Way to handle alert window
    >self.driver.switch_to_alert().accept()             ### it will close the pop-up by clicking on ok
    >self.driver.switch_to_alert().dismiss()            ### it will close the pop-up by clicking on cancle
    
    
>>Way to switch b/t different tabs open in a single window:
    >self.driver.current_window_handle                  ### retun the handle of currently focussed window
    >handles=self.driver.window_handles                 ### a list containing all the window handles will get created
    >self.driver.switch_to_window(handle[n])            ### it will switch the focus into the nth window
    

>> frames/iframes Way to switch between them
    >the concept to toggeling b/t frames is to switch to the req frame, perform task and then again come back to the main page and then move to the 
    another frame and perform your task
    >we can switch to any frame present on the page by it name, id , index_no.
    
    >Way to switch to any frame
        >self.driver.switch_to_frame('name of frame')
        >self.driver.switch_to_frame('id')
        >self.driver.switch_to_frame(index_no)
       
    >Way to come back from any frame to the main page
        >self.driver.switch_to.default_content()        ### it always points to the main page so no need to pass any xpath/id
    
	

	
	
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
	>> after this cmd local files in the pc will get updated with the latest files of master/any other branchname as u defined >>not your current branch in git repository
	>> now u need to introduce your change and push this data to the current branch by $ git push origin current_branch_name and then merge this branch with the master
	
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

# way to delete branch 
>> for deleting we have to be on our master branch
	
	git branch -d branch_name
	git branch -D branch_name
	
The -d option stands for --delete, which would delete the local branch, only if you have already pushed and merged it with your remote branches.
The -D option stands for --delete --force, which deletes the branch regardless of its push and merge status, so be careful using this one!


## way to update any local branch with the master branch
	> checkout to that branch
	> $ git pull
	> $ git merge master/any other branchname
		>> after this cmd local files in the pc will get updated with the latest files of master/any other branchname as u defined >>not your current branch in git repository
		>> now u need to introduce your change and push this data to the current branch by $ git push origin current_branch_name and then merge this branch with the master
	
	
## way to revert the last commit

$ git reset --soft HEAD~1
	Reset will rewind your current HEAD branch to the specified revision. In our example above, we'd like to return to the one before the current revision - effectively making our last commit undone.

Note the --soft flag: this makes sure that the changes in undone revisions are preserved. After running the command, you'll find the changes as uncommitted local modifications in your working copy.

If you don't want to keep these changes, simply use the --hard flag. Be sure to only do this when you're sure you don't need these changes anymore.
>>$ git reset --hard HEAD~1	
	


Imp Cmds

1-Cmd for parallel execution :
    we have to go upto that location where all the robotfile exist and open cmd
    
    >pabot --processes n --report_generation_location *.robot
        eg. pabot --processes 2 --outputdir D:\TRY\Multi_Threading\ *.robot
    NOTE:- This cmd will run all the robot file present at the loaction parallely and generate report.html, log.html, output.xml at the defined outputdir

    >pabot --processes n --report_generation_location\Result *.robot
        eg. pabot --processes 2 --outputdir D:\TRY\Multi_Threading\Result *.robot
    NOTE:- This cmd will run all the robot file present at the loaction parallely and generate report.html, log.html, output.xml 
           + suite specific folder, inside Result folder which will get create automatically at the defined location.
    
    > n stand for no of file u want to execute parallel
    > this cmd is only applicable for the execution of robot files.

	
2- Cmd 

pytest-html
>Cmd to generate html reports of unittestframework 

Note:- Give all path with double backslash

1-pytest -v -s filename_with_location_which_u_want_to_run    
    >>> this will show passed and failed over cmd only means no report would get generate
            
2-pytest -v -s --html=report.html --self-contained-html filename_with_location_which_u_want_to_run   
    >> this will show passed and failed over cmd as well as a report will get generate at the default current_directory location, 
        as we haven't defined report generation location of our choice
    
pytest -v -s --html=reportfile_name_with_location.html --self-contained-html filename_with_location_which_u_want_to_run
    >> this will show passed and failed over cmd as well as a report will get generate at the default location, 
	>> .\ represents current directory


	
## understanding resolving merging conflicts
'''
