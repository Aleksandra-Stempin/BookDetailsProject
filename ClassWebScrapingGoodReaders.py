import time

from ClassConstanntDataGoodReaders import ConstanntDataGoodReaders as cdgr
import requests
import self
import re
from lxml.html import fromstring
import re

class WebScrapingGoodReaders():
    global bookDet
    global tryNo
    tryNo = 0
    def _ConverDate(self, dateGR):
        dateList = str(dateGR).split(" ")
        monthDictionary = {
            "January": "01",
            "February": "02",
            "March": "03",
            "April": "04",
            "May": "05",
            "June": "06",
            "July": "07",
            "August": "08",
            "September": "09",
            "October": "10",
            "November": "11",
            "December": "12"}
        mm = dateList[0]
        monthNo = monthDictionary.get(mm)
        dd = dateList[1]
        ddNo =re.findall("\d+", dd)[0]
        if len(str(ddNo)) == 1:
            ddNo = "0%s"%(ddNo)
        yy = dateList[2]

        date = "{}-{}-{}".format(yy,monthNo, ddNo)
        # print(date)
        return date

    def GetBookDataFromWebScrapingGR (self, isbnNo):
        global tryNo
        bookAttribute = ""
        bdf = ";;;;;;;;"
        bookFound = True
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
        genre = "no genre"
        genreToFile = ""
        originalTitle = "no original title"
        originalTitleToFile = ""
        publishDate = "no publish date"
        publishDateToFile = ""
        language = "no language"
        languageToFile = ""
        isbn = "no isbn"
        isbnToFile = ""
        try:
            def _getBookAttribute(xpath):
                bookAttribute = bookDet.xpath("{}//text()".format(xpath))[0]
                bookAttribute = str(bookAttribute).strip()
                return bookAttribute

            # getting request to book page on good readers
            bookUrl = cdgr.GR_bookUrl % (isbnNo)
            # print(bookUrl)
            time.sleep(2)
            bookPage = requests.get(bookUrl)
            bookDet = fromstring(bookPage.text)

            # checking no results element
            try:
                noRestlts = _getBookAttribute(cdgr.GR_noResultsXpath)
                if noRestlts == "No results.":
                    bookFound = False
            except:
                pass
            # print("book found", bookFound)
            if bookFound:
                # author
                try:
                    authorsList = bookDet.xpath("{}//text()".format(cdgr.GR_authorXpath))
                    authorsListStr = str(authorsList).replace("[","").replace("]","").replace("'","").replace(", (", "(")
                    authorsListStr = authorsListStr.replace("(Goodreads Author)", "")
                    authorsListList = authorsListStr.split(",")
                    authorListFinal = []
                    for authorEl in authorsListList:
                        authorEl = authorEl.strip()
                        if authorEl.count("(")==0:
                            authorListFinal.append(authorEl)
                    author = str(authorListFinal).strip("'").strip("[").strip("]").replace("'", "")
                    authorToFile = author
                except Exception as e:
                    pass

                # title
                try:
                    title = _getBookAttribute(cdgr.GR_titleXpath)
                    titleToFile = title
                except:
                    pass

                # original title
                try:
                    originalTitle = _getBookAttribute(cdgr.GR_originalTitleXpath)
                    originalTitleToFile = originalTitle
                except:
                    originalTitle = title
                    originalTitleToFile = titleToFile


                # series and book of series
                try:
                    seriesAndBookOfSeries = _getBookAttribute(cdgr.GR_seriesXpath).strip("(, )")
                    if seriesAndBookOfSeries.count("#") == 1:
                        seriesAndBookOfSeriesList = seriesAndBookOfSeries.split("#")
                        series = seriesAndBookOfSeriesList[0].strip()
                        seriesToFile = series
                        bookOfSeries = seriesAndBookOfSeriesList[1].strip()
                        bookOfSeriesToFile = bookOfSeries
                except:
                    pass

                # publisher Name And Publish Date
                try:
                    publisherNameAndPublishDate = _getBookAttribute(cdgr.GR_publisherNameAndPublishDateXpath)
                    publisherNameAndPublishDateList = publisherNameAndPublishDate.split("\n")
                    publisher = publisherNameAndPublishDateList[2].replace("by", "").strip()
                    publisherToFile = publisher
                    publishDateGR = publisherNameAndPublishDateList[1].strip()
                    publishDate = WebScrapingGoodReaders._ConverDate(publishDateGR)
                    publisherToFile = publishDate
                except:
                    pass

                # genre
                try:
                    genreList = bookDet.xpath("{}//text()".format(cdgr.GR_gerneXpath))
                    if len(genreList)>=3:
                        genreList = genreList[0:3]
                    myGenre = ""
                    for g in genreList:
                        myGenre = myGenre + ", " + g
                    myGenre = myGenre.strip(",").strip()
                    genre = myGenre
                    genreToFile = genre
                except:
                    pass

                # language
                try:
                    language = _getBookAttribute(cdgr.GR_languageXpath)
                    languageToFile = language
                except:
                    pass

                # isbn
                try:
                    isbn = _getBookAttribute(cdgr.GR_isbnXpath)
                    isbnToFile = isbnToFile
                except:
                    isbn = isbnNo
                    isbnToFile = isbnNo

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
                    ''' % (
                author, title, originalTitle, series, bookOfSeries, publisher, genre, publishDate, language, isbn)

                # print(bookDetails)
                if title != "no title":
                    print(bookDetails)
                    # book details in form to file
                    bdf = "%s;%s;%s;%s;%s;%s;%s;%s;%s" % (authorToFile, titleToFile, originalTitleToFile, seriesToFile,
                                                          bookOfSeriesToFile, genreToFile, publisherToFile, languageToFile,
                                                          isbnNo)
                else:
                    bdf = ";;;;;;;;"
                    print("Nothing was found for book ISBN: {}".format(isbnNo))

            else:
                notFoundMsg = "Book with ISBN: %s has not been found in Good Readers"%(isbnNo)
                print(notFoundMsg)
                bdf = ";;;;;;;;"
            # print(bdf)
            return bdf
        except Exception as e:
            print("Error in GetBookDataFromWebScrapingGR for {}\n{}".format(isbnNo, str(e)))
            bdf = ";;;;;;;;"
            return  bdf





# harryUrl = r"https://www.goodreads.com/book/show/30972270-harry-potter-i-kamie-filozoficzny"
# harryISBN = "9788380082113"
# WebScrapingGoodReaders.GetBookDataFromWebScrapingGR(self, harryISBN)


