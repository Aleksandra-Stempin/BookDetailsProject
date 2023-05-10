# do not use latin extended characters in paths (cv2 package doesn't read them)

import ClassBookDetailsToFileFromBarcode as BD
import ClassBookDetailsReadBarCodeWebScraping as WS
import ClassBookDetailsFromBarCodeGooDReadersFirst as GRWS
import self
import ClassFileHandling as fh
import sys
import ClassPingMe as pm
import ClassPingMeWithSimpleaudio as pmsa

# output directory to save book details files
outDir = r"C:\Users\Olenka\Documents\bookDetailsPython\testFilesFolder"
outDir = r"C:\Users\Olenka\Desktop\boook"
# directory with barcodes images
dirPath = r"C:\Users\Olenka\Documents\bookDetailsPython\barcodes"
dirPath=r"C:\Users\Olenka\Desktop\boook"
dirPath=r"C:\Users\aleksandra.stempin\OneDrive - Accenture\!Sync\Downloads\NewBooks"
# dirPath=r"C:\book"

# name for book details file, every file will be named fileName_currentDatetime
fileName = "MyBookDetails"


GRWS.BookDetailsFromBarCodeGooDReadersFirst.GetBookDet(self,
barcodeImgDir=dirPath
,bookDetFilesDir=dirPath
,bookDetFileName=fileName
,headlessMode=False
)


#
# pmsa.PingMeWithSimpleaudio.succesNotification(self)
# pmsa.PingMeWithSimpleaudio.failNotification(self)