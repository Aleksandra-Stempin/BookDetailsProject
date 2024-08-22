class ConstanntDataGoogle():
    # google
    googleUrl = "https:google.com"
    googleAcceptCookiesButtonID = "L2AGLb"
    googleSearchName = "q"
    googleSearchInputText = r"isbn %s site:lubimyczytac.pl"
    # googleSearchInputText = "//h3[text()[contains(.,'Książka w')]]/.."
    googleNotFoundXpath = "//div[@class='card-section']/ul/li"
    googleNotFoundText = "Nie znaleziono książki z ISBN %s w serwisie lubimy czytać."
    googleLinkXpath = "//h3[@class='LC20lb MBeuO DKV0Md']"
    googleBookLinkXpath = "//div[@class='yuRUbf']/a"
    googleBookLinkXpath = "//h3[text()[contains(.,'Książka w')]]/.."

    googleSearchForGoodReaders = "https://www.google.com/search?q=goodreads.com"
    gooleInputSearchInGoodReaders = '//input[@jsname = "YPqjbf"]'
    googleMagnifierXpath = "//div[@class='iblpc']"

    # # lubimy czytać
    # LC_cokkiesOkBututID = "onetrust-accept-btn-handler"
    # LC_zoomOkButXpath = '//a[@class="btn btn-primary mb-0 mt-1 js-close-zoom-btn"]'
    # LC_newsletterCloseButXpath = '//a[@class="footer__fixed__close js-footer-fixed-close-btn pl-3 pb-3"]'
    # LC_detailsButXpath = "//button[@data-target='#book-details']"
    # LC_DetButtNotFound = "Couldn't find details button"
    # LC_manyAuthorsXpath = "//a[@class='btn-collapse-authors js-btn-collapse-authors collapsed']"
    # LC_authorNameXpath = "//a[@class='link-name d-inline-block']"
    # LC_bookTitleXpath = "//h1[@class='book__title']"
    # LC_originalTitleXpath = "//dt[contains(text(), 'Tytuł oryginału')]/following-sibling::dd"
    # LC_publisherNameXpath = "//span[contains(text(), 'Wydawnictwo')]/a"
    # LC_genreXpath = "//a[@class='book__category d-sm-block d-none']"
    # LC_publishDateXpath = "//dt[contains(text(), 'Data wydania')]/following-sibling::dd"
    # LC_languageXpath = "//dt[contains(text(), 'Język')]/following-sibling::dd"
    # LC_regExp = ". \(tom +[0-9]\)" # regular expression for book of series
    # LC_seriesXpath = "//span[contains(text(), 'Cykl')]/a"
    # LC_isbnXpath = "//dt[contains(text(), 'ISBN')]/following-sibling::dd"



