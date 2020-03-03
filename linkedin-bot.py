from selenium import webdriver
from time import sleep
from info import username, password, job

class LinkedInBot():
    def __init__(self):
        
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.linkedin.com/')

        sleep(3)

        email_btn = self.driver.find_element_by_xpath('/html/body/nav/section[2]/form/div[1]/div[1]/input')
        email_btn.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('/html/body/nav/section[2]/form/div[1]/div[2]/input')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('/html/body/nav/section[2]/form/div[2]/button')
        login_btn.click()
    
    def getToJobListings(self):
        job_btn = self.driver.find_element_by_xpath('//*[@id="jobs-tab-icon"]')
        job_btn.click()
        sleep(3)

        job_title_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[3]/div/div/section/div[2]/div[1]/div/div[2]/div/div/input')
        job_title_btn.send_keys(job)

        search_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[3]/div/div/section/div[2]/div[1]/div/button')
        search_btn.click()

    def setFilter(self):
        feature_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[3]/section[1]/header/div/div/div[3]/div/div/ul/li[2]/form/button/span')
        feature_btn.click()
        sleep(1)

        easy_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[3]/section[1]/header/div/div/div[3]/div/div/ul/li[2]/form/div/fieldset/div/ul/li[2]/label')
        easy_btn.click()
        sleep(1)

        apply_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[3]/section[1]/header/div/div/div[3]/div/div/ul/li[2]/form/div/fieldset/div/div/div/button[2]/span')
        apply_btn.click()
    
    def handlePopup(self):
        try: #default one
            follow_cancel_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[1]/label')
            follow_cancel_btn.click()

            submit_app_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[3]/button/span')
            submit_app_btn.click()
            sleep(1)

            exit_out_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button')
            exit_out_btn.click()

        except Exception: #if longer version
            try:
                next_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button/span')
                next_btn.click()

                another_next_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button[2]/span')
                another_next_btn.click()

            except Exception:
                next_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button/span')
                next_btn.click()

                while True:
                    try:
                        another_next_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button[2]/span')
                        another_next_btn.click()
                    except Exception:
                        another_next_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button[2]/span')
                        another_next_btn.click()               


    def clickApply(self):
        for i in range (1, 26): #this is for if the number of jobs on each page is 25; if not, adjust the second number to number of postings on page + 1
            sleep(2)
            pref = '/html/body/div[5]/div[4]/div[3]/section[1]/div[2]/div/div/div[1]/div[2]/div/ul/li['
            suff = ']/div/artdeco-entity-lockup/artdeco-entity-lockup-content/h3/a'
            j = str(i + 1)
            xpath = pref + j + suff
            next_job_btn = self.driver.find_element_by_xpath(xpath)
            
            try: #default, everything works great
                print("default")
                easy_app_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[3]/section[1]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[3]/div/button/span')
                easy_app_btn.click()

                self.handlePopup()
                sleep(1)

                next_job_btn.click()
                sleep(2)
            
            except Exception:
                print('already applied exception')
                next_job_btn.click()
                sleep(2)                 

    def autoApply(self):
        while True:
            sleep(1)
            self.clickApply()

bot = LinkedInBot()
bot.login()
bot.getToJobListings()
sleep(3)
bot.setFilter()
sleep(2)
bot.autoApply()
