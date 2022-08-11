import os
import time
from telnetlib import EC

import self
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class GetBookDetailsByIsbn():
    # import selenium
    import selenium.webdriver as wb
    import selenium.webdriver.chrome.service as ser
    from selenium.webdriver.chrome.service import Service as ser
    import re
    from ClassConstanntDataGoogle import ConstanntDataGoogle as cdg
    from ClassConstanntDataLubimyCzytac import ConstanntDataLubimyCzytac as cdlc
    # import webdriver_manager.chrome as wm
    # import selenium.webdriver.support.expected_conditions as EC
    # import selenium.webdriver.support.wait as wait
    import datetime
    from webdriver_manager.chrome import ChromeDriverManager as cdm
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    def __init__(self, outDir):
        self.outDir = outDir
        pass

    def OpenDriver(self, headlessMode=False):
        """opens (and installs latest version of) driver"""
        global driver
        global action
        global wait
        ChromeDriverPath = "C:/Program Files/Google/Chrome/Application/chromedriver.exe"
        s = self.ser(self.cdm().install())
        # s = self.ser()
        o = self.wb.ChromeOptions()
        o.add_argument("--incognito")
        o.add_argument("--disable-extensions")
        o.add_argument("--disable-gpu")
        o.add_argument('disable-notifications')
        o.add_argument('disable-infobars')
        # headless mode
        if headlessMode:
            o.add_argument("headless")
            o.headless = True
        driver = self.wb.Chrome(options=o, service=s)
        # driver = webdriver.Chrome(ChromeDriverPath)
        driver.maximize_window()
        action = self.wb.ActionChains(driver)
        driver.implicitly_wait(10)
        # wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
        #                      ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        # driver.set_page_load_timeout(30)
        # driver.implicitly_wait(30)

    def CloseDriver(self):
        """closes driver"""
        driver.close()

    def _CloseException(self, Exception):
        GetBookDetailsByIsbn.CloseDriver(self)
        # GetBookDetailsByIsbn.CloseFile(self)

    def _CreateScreenshotName(self):
        """creating screenshot name in format screenshot_[currentDataTime]"""
        currTime = self.datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        fullDirName = r"%s\screenshots"%(self.outDir)
        try:
            os.mkdir(fullDirName)
        except:
            pass
        # scName = fullDirName + "//screenshot_" + currTime + ".png"
        scName = r"{}\screenshot_{}.png".format(fullDirName,currTime)
        return scName

    def CreateScreenshot(self):
        """creating full page screenshot and saving in folder screenshots"""
        scName = GetBookDetailsByIsbn._CreateScreenshotName(self)
        s = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
        driver.set_window_size(s("Width"), s("Height"))
        driver.find_element(self.By.TAG_NAME, 'body').screenshot(scName)

    def OpenGooglePage(self):
        """opening page with ISBN search"""
        # googleUrl = "https:google.com"
        driver.get(self.cdg.googleUrl)


    def AgreeGoogleCookies(self):
        """accept google cookies"""
        # butID = "L2AGLb"
        driver.find_element(self.By.ID, self.cdg.googleAcceptCookiesButtonID).click()

    def IsBook(self, isbn):
        """checks if isbn is a book"""
        book_isbn = str(isbn)
        if len(book_isbn) == 10:
            return True
        elif len(book_isbn) == 13 and book_isbn.startswith("978"):
            return True
        else:
            return False

    def InputSearch(self, isbnNo):
        """search by given isbn in lubimy czytać page using advanced google search"""
        # advance search input
        searchInputText = self.cdg.googleSearchInputText % (isbnNo)
        searchInput = driver.find_element(self.By.NAME, self.cdg.googleSearchName)
        searchInput.send_keys(searchInputText)
        searchInput.send_keys(self.Keys.ENTER)
        # checks if book can be found, checking message, that is is not found
        try:
            driver.find_element(self.By.XPATH, self.cdg.googleNotFoundXpath)
            notFoundText = self.cdg.googleNotFoundText % (isbnNo)
            print(notFoundText)
            return False
        except:
            return True

    def ClearSearch(self):
        """clears google search input"""
        try:
            searchInput = driver.find_element(self.By.NAME, self.cdg.googleSearchName)
            searchInput.clear()
        except Exception as e:
            errMsg = 'ClearSearch failed,\n%s'%(str(e))
            print(errMsg)

    def GoToLink(self):
        """goes to lubimy czytać book page"""
        print("GoToLink in start")
        try:
            time.sleep(2)
            driver.find_element(self.By.XPATH, self.cdg.googleLinkXpath).click()
            time.sleep(2)

            print("GoToLink in ok")
        except Exception as e:
            print("GoToLink in not ok,\n%s"%(str(e)))
            raise TimeoutException
            # raise self.CloseException
        print("GoToLink in end")

    def ReturnLink(self):
        """goes to lubimy czytać book page"""
        try:
            # time.sleep(2)
            # bookLinkXpath = "//div[@class='yuRUbf']/a"
            bookLink = driver.find_element(self.By.XPATH, self.cdg.googleBookLinkXpath).get_attribute("href")
            # print("bookLink", bookLink)
            return bookLink

        except Exception as e:
            print("ReturnLink in not ok,\n%s"%(str(e)))
            return ""
            pass
            # raise self.CloseException
        print("ReturnLink in end")

    def ClosePopUps(self):
        """closes popups on lubimy czytać page"""
        # cookies popup
        # print("ClosePopUps in start")
        try:
            # cokkiesOkBututID = "onetrust-accept-btn-handler"
            cokkiesOkButut = driver.find_element(self.By.ID, self.cdlc.LC_cokkiesOkBututID)
            action.move_to_element(cokkiesOkButut).click().perform()
            # print("cokkiesOkButut ok")
        except:
            pass

        # zoom pop up
        try:
            zoomOkBut = driver.find_element(self.By.XPATH, self.cdlc.LC_zoomOkButXpath)
            action.move_to_element(zoomOkBut).click().perform()
            # print("zoomOkBut ok")
        except:
            pass

        # newsletter pop up
        try:
            # newsletterCloseButXpath = '//a[@class="footer__fixed__close js-footer-fixed-close-btn pl-3 pb-3"]'
            newsletterCloseBut = driver.find_element(self.By.XPATH, self.cdlc.LC_newsletterCloseButXpath)
            action.move_to_element(newsletterCloseBut).click().perform()
            # print("newsletterCloseBut ok")
        except:
            pass
        # print("ClosePopUps in done")

    def GetBooksDetails(self):
        """gets book's details and saves them to created file and prints on the screen"""
        detButFound = False
        bdf = ";;;;;;;;"
        author = "no author"
        authorToFile = ""
        title = "no title"
        titleToFile = ""
        series = "no series"
        seriesToFile = ""
        bookOfSeries = "-"
        bookOfSeriesToFile = ""
        publisher = "no publisher"
        publisherToFile = ""
        originalTitle = "no original title"
        originalTitleToFile = ""
        publishDate = "no publish date"
        publishDateToFile = ""
        language = "no language"
        languageToFile = ""
        isbn = "no isbn"
        isbnToFile = ""
        # driver.execute_script("scroll(0,-150)")
        try:
            # details button
            # print("details button start")
            try:
                detailsBut = self.WebDriverWait(driver, 10). \
                    until(self.EC.element_to_be_clickable((self.By.XPATH, self.cdlc.LC_detailsButXpath)))
                action.move_to_element(detailsBut).click().perform()
                detButFound = True
            except:
                print(self.cdlc.LC_DetButtNotFound)
            # print("details button end")

            # author
            # expands authors list if book has many authors
            try:
                # print("manyAuthor start")
                manyAuthorsButton = self.WebDriverWait(driver, 5). \
                    until(self.EC.element_to_be_clickable((self.By.XPATH, self.cdlc.LC_manyAuthorsXpath)))
                action.move_to_element(manyAuthorsButton).click().perform()
                # print("manyAuthorsButton found")
            except:
                pass
            # print("manyAuthor end")
            # generating authors list (most cases 1 element list)
            try:
                autohorListStr = ""
                authorsList = driver.find_elements(self.By.XPATH, self.cdlc.LC_authorNameXpath)
                for authorName in authorsList:
                    autohorListStr = autohorListStr + ", " + authorName.text
                    # removes extra commas and spaces
                    autohorListStr = autohorListStr.rstrip(",").lstrip(",").strip(" ")
                author = autohorListStr
                authorToFile = author
            except:
                print("no author", author)
                pass
            # print("author", author)

            # title
            try:
                title = driver.find_element(self.By.XPATH, self.cdlc.LC_bookTitleXpath).text
                titleToFile = title
            except:
                print("no title", title)
                pass


            # series
            regExp = ". \(tom +[0-9]\)"
            try:
                series = driver.find_element(self.By.XPATH, self.cdlc.LC_seriesXpath).text
                seriesToFile = series
            except:
                pass
            regexList = self.re.findall(self.cdlc.LC_regExp, series)
            regexListLen = len(regexList)
            if regexListLen == 1:
                # book in series
                seriesList = series.split("(tom ")
                seriesName = seriesList[0]
                bookOfSeries = seriesList[1]
                bookOfSeries = bookOfSeries.strip(")")
                series = seriesToFile = seriesName
                bookOfSeriesToFile = bookOfSeries

            # publisher
            try:
                publisher = driver.find_element(self.By.XPATH, self.cdlc.LC_publisherNameXpath).text
                publisherToFile = publisher
            except:
                print("no publisher", publisher)
                pass


            # genre
            try:
                genre = driver.find_element(self.By.XPATH, self.cdlc.LC_genreXpath).text
                genreToFile = genre
            except:
                print("no genre", genre)
                pass


            if detButFound:
                # original title
                try:
                    originalTitle = driver.find_element(self.By.XPATH, self.cdlc.LC_originalTitleXpath).text
                    originalTitleToFile = originalTitle
                except:
                    originalTitle = title
                    originalTitleToFile = titleToFile
                # print("originalTitle",  originalTitle)

                # publish date
                try:
                    publishDate = driver.find_element(self.By.XPATH, self.cdlc.LC_publishDateXpath).text
                    publishDateToFile = publishDate
                except:
                    print("no publishDate", publishDate)
                    pass


                # language
                try:
                    language = driver.find_element(self.By.XPATH, self.cdlc.LC_languageXpath).text
                    languageToFile = language
                except:
                    print("no language", language)
                    pass

                # ISBN
                try:
                    isbn = driver.find_element(self.By.XPATH, self.cdlc.LC_isbnXpath).text
                    isbnToFile = isbn
                except:
                    print("no isbn", isbn)
                    pass

            # book details str
            bookDetails = '''author: %s
    title: %s
    original title: %s
    series: %s
    book of series: %s
    publisher: %s
    genre: %s
    publish date: %s
    language: %s
    ISBN: %s
        ''' % (author, title, originalTitle, series, bookOfSeries, publisher, genre, publishDate, language, isbn)
            print(bookDetails)

            # book details in form to file
            bdf = "%s;%s;%s;%s;%s;%s;%s;%s;%s" % (authorToFile, titleToFile, originalTitleToFile, seriesToFile,
                                                  bookOfSeriesToFile, genreToFile, publisherToFile, languageToFile,
                                                  isbnToFile)
            return bdf
        except:
            bdf = ";;;;;;;;"
            return bdf



