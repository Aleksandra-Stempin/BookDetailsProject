import requests
import self
import re
from lxml.html import fromstring
from ClassConstanntDataGoogle import ConstanntDataGoogle as cdg
from ClassConstanntDataLubimyCzytac import ConstanntDataLubimyCzytac as cdlc
class WebScraping():
    global bookDet
    def _getReguest(self, bookUrl):
        try:
            print("book url", bookUrl)
            bookPage = requests.get(url=bookUrl, params=None)
        except Exception as e:
            errMsg= "\nerror in get request:\n"+str(e)+"\n"
            print(errMsg)
            raise Exception





    def GetBookDataFromWebScraping (self, bookUrl):
        bookAttribute = ""
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

        print("book url", bookUrl)
        bookPage = WebScraping._getReguest(self, bookUrl)

        print("bookPage")
        bookDet = fromstring(bookPage.text)
        print(" bookDet",  bookDet)

        def _getBookAttribute(xpath):
            bookAttribute = bookDet.xpath("{}//text()".format(xpath))[0]
            bookAttribute = str(bookAttribute).strip()
            print(bookAttribute)
            return bookAttribute

        # author
        try:
            authorsList = bookDet.xpath("{}//text()".format(cdlc.LC_authorNameXpath))
            for authorEl in authorsList:
                author = author + ", " + str(authorEl).strip()
            author = author.replace("no author", "")
            author = author.strip(",").strip()
            authorToFile = author
        except:
            pass
        print("author", author)

        # title
        try:
            title = _getBookAttribute(cdlc.LC_bookTitleXpath)
            titleToFile = title
        except:
            pass
        print("title", title)

        # original title
        try:
            originalTitle = _getBookAttribute(cdlc.LC_originalTitleXpath)
            originalTitleToFile = originalTitle
        except:
            originalTitle = title
            originalTitleToFile = titleToFile
        print(" originalTitle",  originalTitle )

        # series and book in series
        try:
            series = _getBookAttribute(cdlc.LC_seriesXpath)
            isSeries = cdlc.LC_seriesPattern in series
            regexList = re.findall(cdlc.LC_regExp, series)

            regexListLen = len(regexList)
            # if regexListLen == 1:
            if isSeries:
                # book in series
                seriesList = series.split("(tom ")
                seriesName = seriesList[0].strip()
                bookOfSeries = seriesList[1].strip()
                bookOfSeries = bookOfSeries.strip(")").strip()
                series = seriesToFile = seriesName
                bookOfSeriesToFile = bookOfSeries
        except:
            pass

        # publisher
        try:
            publisher = _getBookAttribute(cdlc.LC_publisherNameXpath)
            publisherToFile = publisher
        except:
            pass

        # genre
        try:
            genre =_getBookAttribute(cdlc.LC_genreXpath)
            genreToFile = genre
        except:
            pass

        # publish date
        try:
            publishDate = _getBookAttribute(cdlc.LC_publishDateXpath)
            publishDateToFile = publishDate
        except:
            pass

        # language
        try:
            language = _getBookAttribute(cdlc.LC_languageXpath)
            languageToFile = language
        except:
            pass

        #isbn
        try:
            isbn = _getBookAttribute(cdlc.LC_isbnXpath)
            isbnToFile = isbn
        except:
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

