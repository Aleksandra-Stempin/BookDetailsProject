class ReadBarcode():
    import os
    import cv2
    import pyzbar
    from pyzbar.pyzbar import decode

    def __init__(self, barcodeDir):
        self. barcodeDir = barcodeDir

    def _ListFilesInDirectory(self):
        """creating list of images in directory"""
        imgList = []
        imgExtensions = ['jpg', 'png', 'gif', 'bmp', "jpg"]
        for img in self.os.listdir(self.barcodeDir):
            # print("img", img, img.split('.')[1])
            if img.split('.')[1] in imgExtensions:
                imgList.append(img)
        return imgList

    def _IsbnValidator(self, isbn):
        """ISBN number validation based on https://www.instructables.com/How-to-verify-a-ISBN/ """
        isbn_str = str(isbn)
        # remainder of the division, if ISBN is valid the remainder is 0
        remainder = 5
        sum = 0
        # validation of ISBN 13
        if len(isbn_str) == 13:
            # multiplication factor for validation of ISBN-13
            m = 1
            for i in range(len(isbn_str)):
                sum = sum + int(isbn_str[i]) * m
                if m == 1:
                    m = 3
                elif m == 3:
                    m = 1
            remainder = sum % 10

        # validation of ISBN 10
        elif len(isbn_str) == 10:
            for i in range(len(isbn_str)):
                sum = sum + int(isbn_str[i]) * (10 - i)
            remainder = sum % 11
        else:
            return False

        if remainder == 0:
            return True
        else:
            return False

    def ReadFromBarcode(self):
        """read ISBN number from bar code photo and after validation adds to ISBN list"""
        # list of barcodes images in directory and declaration of isbn list
        imgList = ReadBarcode._ListFilesInDirectory(self)
        isbnDic = {}
        # reading barcodes from images
        for img in imgList:
            try:
                imgName = img
                # adding full path to img name
                img = "%s\\%s" % (self.barcodeDir, img)

                # opening image
                barcodeImg = self.cv2.imread(img)
                # converting to gray scale
                barcodeImg = self.cv2.cvtColor(barcodeImg, self.cv2.COLOR_BGR2GRAY)
                # extracting ISBN number from data read from barcode
                barCodeInfo = self.pyzbar.pyzbar.decode(barcodeImg)
                # print(imgName, barCodeInfo)
                # print('barCodeInfo', barCodeInfo)
                isbn = str(barCodeInfo).split(",")[0]
                isbn = isbn.split("'")[-2]
                isbn = isbn.strip()
            except:
                isbn = "No ISBN detected from picture %s\n" % (imgName)
            # if ISBN is valid it is added to list os ISBN numbers
            if ReadBarcode._IsbnValidator(self, isbn):
                isbnDic.update({isbn: imgName})

            else:
                if isbn.isdigit():
                    errText = '''%s is not a valid book ISBN.
Please check your source in picture %s.
''' % (isbn, imgName)
                else:
                    errText = isbn
                print(errText)
        return isbnDic


# dirPath = r'C:\Users\aleksandra.stempin\OneDrive - Accenture\!Sync\Downloads\imageToText2'
# rb = ReadBarcode(dirPath)
# filesList = rb.ListFilesInDirectory()
# # print(filesList)
# dicBarcode = rb.ReadFromBarcode()
# print(dicBarcode)