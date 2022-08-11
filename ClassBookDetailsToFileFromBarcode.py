from selenium.common.exceptions import TimeoutException
import ClassFileHandling
import ClassGetBookDetails
import ClassReadBarCode
import self
import ClassPingMe as ping

class BookDetailsToFileFromBarcode():

    def GetBookDet(self, bookDetFilesDir, barcodeImgDir, bookDetFileName):
        try:
            # creating objects of imported classes
            fh = ClassFileHandling.CreateWriteReadCloseFiles(filesOutDir=bookDetFilesDir, fileName=bookDetFileName)
            rb = ClassReadBarCode.ReadBarcode(barcodeDir=barcodeImgDir)
            bd = ClassGetBookDetails.GetBookDetailsByIsbn()
            p = ping.PingMe()
            fh.CreateFile()
            print("bd.OpenDriver out start")
            bd.OpenDriver()
            print("bd.OpenDriver out end()")
            isbnDic = rb.ReadFromBarcode()
            isbnNoList = isbnDic.keys()
            bd.OpenGooglePage()
            bd.AgreeGoogleCookies()
            for isbnNo in isbnNoList:
                try:
                    imgText = "\nImage: %s" % (isbnDic.get(isbnNo))
                    print(imgText)
                    bookDetails = ""
                    if bd.IsBook(isbn=isbnNo):
                        if bd.InputSearch(isbnNo=isbnNo):
                            print("bd.GoToLink start out")
                            try:
                                print("link")
                                bd.GoToLink()
                                print("bd.GoToLink end out")
                            except Exception as e:
                                print("bd.GoToLink end out not ok\n%s"%(str(e)))

                            print("bd.ClosePopUps() start out")
                            try:
                                bd.ClosePopUps()
                            except Exception as e:
                                print("bd.ClosePopUps()\n%s"%(str(e)))
                                pass
                            print("bd.ClosePopUps() end out\n")
                            bookDetails = bd.GetBooksDetails()
                            fh.WriteToFile(bookDetails)
                    else:
                        errText = "%s is not a valid book ISBN."%isbnNo
                        print(errText)
                    bd.OpenGooglePage()
                except (TimeoutException, Exception) as ee:
                    eeStr = "Something went wrong TimeoutException\n%s" % (str(ee))
                    print(eeStr)
                    bd.OpenGooglePage()
                    continue

            bd.CloseDriver()
            fh.CloseFile()
            # raise ArithmeticError
            p.SuccessNotyfication()
        except Exception as e:
            try:
                fh.CloseFile()
            except:
                pass
            errText = "Something went wrong\n%s"%(str(e))
            print(errText)
            p.FailNotyfication()






# ping.PingMe.SuccessNotyfication(self)
# ping.PingMe.FailNotyfication(self)