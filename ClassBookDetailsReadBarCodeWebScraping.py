from selenium.common.exceptions import TimeoutException
import ClassFileHandling
import ClassGetBookDetails
import ClassWebScrapingGoodReaders
import ClassReadBarCode
import ClassSearchGoodReaders
import ClassWebScrapingGoodReaders
import self
import ClassPingMe as ping
import ClassPingMeWithSimpleaudio as pingSA
from ClassWebScraping import WebScraping
import ClassWebScraping

class BookDetailsReadBarCodeWebScraping():
    def GetBookDet(self, bookDetFilesDir, barcodeImgDir, bookDetFileName, headlessMode = False):
        deleteFile = True
        try:
            # creating objects of imported classes
            fh = ClassFileHandling.CreateWriteReadCloseFiles(filesOutDir=bookDetFilesDir, fileName=bookDetFileName)
            rb = ClassReadBarCode.ReadBarcode(barcodeDir=barcodeImgDir)
            bd = ClassGetBookDetails.GetBookDetailsByIsbn(outDir=bookDetFilesDir)
            ws = ClassWebScraping.WebScraping()
            wsgr = ClassWebScrapingGoodReaders.WebScrapingGoodReaders()
            # p = ping.PingMe()
            psa = pingSA.PingMeWithSimpleaudio()

            fh.CreateFile()
            bd.OpenDriver(headlessMode)
            # creating dictionary with ISBN numbers and image's names
            isbnDic = rb.ReadFromBarcode()
            isbnNoList = isbnDic.keys()

            # selenium
            bd.OpenGooglePage()
            bd.AgreeGoogleCookies()
            for isbnNo in isbnNoList:
                try:
                    imgText = "\nImage: %s" % (isbnDic.get(isbnNo))
                    print(imgText)
                    bookDetails = ""
                    if bd.IsBook(isbn=isbnNo):
                        if bd.InputSearch(isbnNo=isbnNo):
                            print("lubimy czytać")
                            bookLink = bd.ReturnLink()
                            # lxml
                            bookDet = ws.GetBookDataFromWebScraping(bookLink)
                            fh.WriteToFile(bookDet)
                            deleteFile = False
                        else:
                            print("Próba good readers")
                            bookDet = wsgr.GetBookDataFromWebScrapingGR(isbnNo)
                            if bookDet == ";;;;;;;;":
                                bookDet = wsgr.GetBookDataFromWebScrapingGR(isbnNo)
                            if bookDet != ";;;;;;;;":
                                fh.WriteToFile(bookDet)
                                deleteFile = False

                    else:
                        errText = "%s is not a valid book ISBN." % isbnNo
                        print(errText)
                    # clearing google search field
                    bd.ClearSearch()
                except:
                    continue
            fh.CloseFile()
            if deleteFile:
                fh.DeleteFile()
            bd.CloseDriver()
            # p.SuccessNotyfication()
            psa.succesNotification()
            # fh.DeleteEmptyFile()
        except Exception as e:
            bd.CreateScreenshot()
            fh.CloseFile()
            if deleteFile:
                fh.DeleteFile()
            bd.CloseDriver()
            eStr = "Error in BookDetailsReadBarCodeWebScraping\nSomething went wrong\n%s" % (str(e))
            print(eStr)
            # p.FailNotyfication()
            psa.failNotification()



