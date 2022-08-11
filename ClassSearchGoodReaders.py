import time

from self import self
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ClassGetBookDetails import GetBookDetailsByIsbn as bd
from webdriver_manager.chrome import ChromeDriverManager as cdm
from ClassConstanntDataGoodReaders import ConstanntDataGoodReaders as cdgr
from ClassConstanntDataGoogle import ConstanntDataGoogle as cdg
import selenium.webdriver as wb
import selenium.webdriver.chrome.service as ser
from selenium.webdriver.chrome.service import Service as ser
class SearchGoodReaders():


    def OpenDriver(self):
        global driver
        s = ser(cdm().install())
        o = wb.ChromeOptions()
        driver = wb.Chrome(options=o, service=s)

    def ReturnBookLinkGR(self, isbnNo):
        # googleSearchForGoodReaders = "https://www.google.com/search?q=goodreads.com"
        driver.get(cdg.googleSearchForGoodReaders)
        time.sleep(3)
        input = driver.find_element(By.XPATH, cdg.gooleInputSearchInGoodReaders)
        input.send_keys(isbnNo)
        input.send_keys(Keys.ENTER)
        bookUrl = driver.current_url
        print(bookUrl)
        return bookUrl



# sgd = SearchGoodReaders()
# sgd.OpenDriver()
# sgd.ReturnBookLinkGR("9788380082113")