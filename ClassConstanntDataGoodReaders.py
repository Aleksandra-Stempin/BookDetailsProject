class ConstanntDataGoodReaders():
    GR_url = "https://www.goodreads.com/"
    GR_noResultsXpath = '//h3[@class="searchSubNavContainer"]'
    GR_bookUrl = "https://www.goodreads.com/search?q=%s"
    GR_searchMainPageID = "sitesearch_field"
    GR_seachFieldName = "q"
    GR_authorXpath = '//div[@id="bookAuthors"]//div[@class="authorName__container"]//span'
    GR_titleXpath = '//h1[@id="bookTitle"]'
    GR_originalTitleXpath = '//div[contains(text(), "Original Title")]//following-sibling::div'
    GR_seriesXpath = '//h2[@id="bookSeries"]/a'
    GR_publisherNameAndPublishDateXpath = "//div[@id='details']/div[contains(text(), 'Published')]"
    GR_gerneXpath = '//div[@class="bigBoxBody"]//div[@class="elementList "]/div[@class="left"]/a'
    # GR_languageXpath = "//div[contains(text(), 'Edition Language')]//following-sibling::div"
    GR_languageXpath = '//div[@itemprop="inLanguage"]'
    GR_isbnXpath = '//span[@itemprop="isbn"]'
