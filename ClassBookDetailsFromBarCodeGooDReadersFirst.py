import os.path
import time

from selenium.common.exceptions import TimeoutException
import ClassFileHandling
import ClassGetBookDetails
import ClassWebScrapingGoodReaders
import ClassReadBarCode
import ClassSearchGoodReaders
import ClassWebScrapingGoodReaders
import self
import ClassPingMe as ping
import ClassPingMeWithSimpleaudio as pmsa
from ClassWebScrapingLC import WebScrapingLC
import ClassWebScrapingLC

class BookDetailsFromBarCodeGooDReadersFirst():
    e=""
    def GetBookDet(self, bookDetFilesDir, barcodeImgDir, bookDetFileName, headlessMode = False):
        deleteFile = True
        # creating objects of imported classes
        fh = ClassFileHandling.CreateWriteReadCloseFiles(filesOutDir=bookDetFilesDir, fileName=bookDetFileName)
        rb = ClassReadBarCode.ReadBarcode(barcodeDir=barcodeImgDir)
        bd = ClassGetBookDetails.GetBookDetailsByIsbn(outDir=bookDetFilesDir)
        ws = ClassWebScrapingLC.WebScrapingLC()
        wsgr = ClassWebScrapingGoodReaders.WebScrapingGoodReaders()
        p = ping.PingMe()
        psa = pmsa.PingMeWithSimpleaudio()
        def _ValidateArg():
            """validates class arguments"""
            errMsg = ""
            bookDetIsDir = False
            imgDirIsDir = False
            if os.path.isdir(bookDetFilesDir):
                bookDetIsDir = True
            else:
                errMsg = errMsg + "Directory %s is not a valid directory path\n"%str(bookDetFilesDir)

            if os.path.isdir(barcodeImgDir):
                imgDirIsDir = True
            else:
                errMsg = errMsg + "Directory %s is not a valid directory path\n"%str(barcodeImgDir)

            if bookDetIsDir and imgDirIsDir:
                return True
            else:
                errMsg = errMsg.strip()
                print(errMsg)
                return False


        if _ValidateArg():
            try:
                fh.CreateFile()
                # creating dictionary with ISBN numbers and image's names
                isbnDic = rb.ReadFromBarcode()
                isbnList = list(isbnDic.keys())
                isbnNoList = []
                # list of ISBN numbers that haven't been found in Good Readers page and will be searched for in lubimy
                # czytac
                LC_isbnNoList = []
                # list of ISBN numbers that haven't been found in Good Readers page and lubimy czytac page
                NotFound_isbnNoList = []
                lubimyCzytacCount = 0
                goodReadersCount = 0
                for isbnNo in isbnList:
                    if bd.IsBook(isbnNo):
                        isbnNoList.append(isbnNo)
                    else:
                        errText = "%s is not a valid book ISBN." % isbnNo
                        print(errText)
                startCount = len(isbnNoList)
                if startCount > 0:
                    print("Good readers start")
                    # good readers loop
                    for isbnNo in isbnNoList:
                        imgText = "\nImage: %s isbn: %s" % (isbnDic.get(isbnNo), isbnNo)
                        print(imgText)
                        # time.sleep(5)
                        try:
                            attemptNo = 0
                            bookDet = ";;;;;;;;"
                            while (bookDet == ";;;;;;;;" and attemptNo < 2):
                                print("Attempt {} isbn {}".format(str(attemptNo+1),isbnNo))
                                attemptNo = attemptNo + 1
                                bookDet = wsgr.GetBookDataFromWebScrapingGR(isbnNo)
                            if len(bookDet)>20:
                                fh.WriteToFile(bookDet)
                                deleteFile = False
                            else:
                                LC_isbnNoList.append(isbnNo)
                        except Exception as e:
                            LC_isbnNoList.append(isbnNo)
                            errStr = "Error in BookDetailsFromBarCodeGooDReadersFirst good readers loop\n{}".format(str(e))
                            print(errStr)
                            continue
                    goodReadersCount = startCount - len(LC_isbnNoList)

                # lubimy czytać loop
                    LC_isbnNoList = list(dict.fromkeys(LC_isbnNoList))
                    if len(LC_isbnNoList)>0:
                        # isbnNoListSucces = isbnNoListLC
                        print("\nLubimy czytac start")
                        bd.OpenDriver(headlessMode)
                        bd.OpenGooglePage()
                        bd.AgreeGoogleCookies()
                        for isbnNo in LC_isbnNoList:
                            try:
                                imgText = "\nImage: %s isbn: %s" % (isbnDic.get(isbnNo),isbnNo)
                                print(imgText)
                                bd.ClearSearch()
                                if bd.InputSearch(isbnNo):
                                    bookLink = bd.ReturnLink()
                                    # print(bookLink)
                                    if len(bookLink)>5:
                                        bookDet = ws.GetBookDataFromWebScraping(bookLink)
                                        if len(bookDet)>=20:
                                            fh.WriteToFile(bookDet)
                                            deleteFile = False
                                        else:
                                            NotFound_isbnNoList.append(isbnNo)
                                else:
                                    NotFound_isbnNoList.append(isbnNo)

                            except:
                                NotFound_isbnNoList.append(isbnNo)
                                errStr = "Error in BookDetailsFromBarCodeGooDReadersFirst lubimy czytac loop\n{}".format(str(e))
                                print(errStr)
                                continue
                        # print("lubimy czytac isbnNoList\n", len(isbnNoList), "\n", isbnNoList)
                        NotFound_isbnNoList = list(dict.fromkeys(NotFound_isbnNoList))
                        lubimyCzytacCount = len(LC_isbnNoList)-len(NotFound_isbnNoList)
                        fh.CloseFile()
                        if deleteFile:
                            fh.DeleteFile()
                        try:
                            bd.CloseDriver()
                        except:
                            pass

                    successGR = goodReadersCount
                    succesLC = lubimyCzytacCount
                    succesTotal = succesLC + successGR
                    notFound = startCount - succesTotal
                    succesTotalPercent = (succesTotal/startCount) * 100
                    succesTotalPercent = round(succesTotalPercent, 2)
                    failTotalPercent = (notFound/startCount) * 100
                    failTotalPercent = round(failTotalPercent, 2)
                    resumeTxt = """
summary

total book count: {}
found by good readers: {}
found by lubimy czytać: {}
total found: {}
percent found: {}%
not found: {}
percent not found: {}%
                    """.format(startCount, successGR, succesLC, succesTotal, succesTotalPercent, notFound, failTotalPercent)
                    print(resumeTxt)
                    if len(NotFound_isbnNoList)>0:
                        notFoundTxt = "\nNot found:\n"
                        for isbnNo in NotFound_isbnNoList:
                            notFoundTxt = notFoundTxt + "image: {} isbn: {}\n".format(isbnDic.get(isbnNo),isbnNo)
                        print(notFoundTxt)
                else:
                    fh.CloseFile()
                    try:
                        fh.DeleteFile()
                    except:
                        pass


                # p.SuccessNotyfication()
                if len(resumeTxt)>5:
                    psa.succesNotification()
                else:
                    raise Exception
            except Exception as err:
                errMsg = "Issue in BookDetailsFromBarCodeGooDReadersFirst:\n{}".format(str(err))
                print(errMsg)
                try:
                    bd.CloseDriver()
                except:
                    pass
                try:
                    fh.CloseFile()
                except:
                    pass
                if deleteFile:
                    fh.DeleteFile()
                # p.FailNotyfication()
                psa.failNotification()



