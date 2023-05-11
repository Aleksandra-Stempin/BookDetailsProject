import requests
import urllib3
import ssl
from lxml.html import fromstring
from urllib3 import PoolManager

class WebScrapingGeneral():

    def _getReguestFromWebScraping(self, url):
        urllib3.disable_warnings()
        try:
            page = requests.get(url=url
                                    , verify=ssl.CERT_NONE)
            return page
        except Exception as e:
            errMsg = "\nerror in get request:\n" + str(e) + "\n"
            print(errMsg)
            raise Exception

    def _formStringFromWebScraping(self, page):
            try:
                pageDet = fromstring(page.text)
                return pageDet
            except Exception as e:
                errMsg = "\nerror in forming string:\n" + str(e) + "\n"
                print(errMsg)
                raise Exception

    def getBookDetFromWebScraping(self, url):
        try:
            page = WebScrapingGeneral._getReguestFromWebScraping(self, url)
            if page != None:
                pageDet = WebScrapingGeneral._formStringFromWebScraping(self, page)
            else:
                pageDet = ""
            return pageDet
        except Exception as e:
            errMsg = "\nerror in getting details from book scraping:\n" + str(e) + "\n"
            print(errMsg)
            raise Exception





