import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'daily_ebook_downloads'}
chrome_options.add_experimental_option('prefs', prefs)

class download_ebooks:
 
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def get_weekly_nyt_list(self):
        self.driver.get('PASTE NYT LIST HERE')
        sleep(5)
        book_number = 1
        new_line = '\n'
        with open('weekly_book_download.txt', "w") as f:
            while book_number <11:
                book_name = self.driver.find_element_by_xpath(f'/html/body/div/div[2]/main/div[3]/div[1]/section/ol/li{[book_number]}/article/div/a/h3').text
                book_writer = self.driver.find_element_by_xpath(f'/html/body/div/div[2]/main/div[3]/div[1]/section/ol/li{[book_number]}/article/div/a/p[2]').text
                book_info = (f"{book_name} {book_writer}").lower()
                print(book_info)
                f.write(book_info + new_line)
                book_number += 1
            else:
                f.close()
        
    def login(self):
        self.driver.get('https://singlelogin.app/?redirectUrl=b-ok.cc')
        sleep(5)
        user_sign_in = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div/div[1]/form/div[1]/input')
        user_sign_in.send_keys('PASTE USERNAME HERE')
        password = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div/div[1]/form/div[2]/input')
        password.send_keys('PASTE PASSWORD HERE')
        sign_in = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div/div[1]/form/button')
        sign_in.click()
        print('signed in')
        sleep(10)

    def download_ebooks(self):
        new_line = '\n'
        with open('weekly_book_download.txt', "r") as f:
            lines = f.read().splitlines()
            line_number = 0
            while line_number < 11:
                print(lines[line_number])
                bookname = lines[line_number]
                self.driver.get(f'https://b-ok.cc/s/?q={bookname}&languages%5B%5D=english&extensions%5B%5D=epub')
                sleep(10)
                got_to_book_download = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3/a')
                got_to_book_download.click()
                sleep(5)
                download_book = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/div[1]/div[1]/div/a')
                download_book.click()
                print(f'downloading {bookname}')
                sleep(30)
                print(f'downloaded {bookname}')
                line_number += 1
            else:
                pass
        
    def rename_books(self):
        for file in os.listdir('daily_ebook_downloads'):
            if " (z-lib.org)" in file:
                original = os.path.join('daily_ebook_downloads', file)
                renamed = os.path.join('daily_ebook_downloads', file.replace(" (z-lib.org)", ""))
                os.rename(original, renamed)



    def book_download_tracker(self):
        path="daily_ebook_downloads"  
        dirList=os.listdir(path)
        with open("downloaded_master_list.txt", "a+") as f:
            for filename in dirList:
                print (filename)
                clean_filename = filename + '\n'
                f.write(clean_filename)



def do_requests():
        bot = download_ebooks()
        bot.get_weekly_nyt_list()
        bot.login()
        bot.download_ebooks()
        bot.rename_books()
        bot.book_download_tracker()

do_requests()