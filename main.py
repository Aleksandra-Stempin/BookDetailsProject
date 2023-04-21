# do not use latin extended characters in paths (cv2 package doesn't read them)

import ClassBookDetailsToFileFromBarcode as BD
import ClassBookDetailsReadBarCodeWebScraping as WS
import ClassBookDetailsFromBarCodeGooDReadersFirst as GRWS
import self
import ClassFileHandling as fh
import sys

# output directory to save book details files
outDir = r"C:\Users\Olenka\Documents\bookDetailsPython\testFilesFolder"
outDir = r"C:\Users\Olenka\Desktop\boook"
# directory with barcodes images
dirPath = r"C:\Users\Olenka\Documents\bookDetailsPython\barcodes"
dirPath=r"C:\Users\Olenka\Desktop\boook"
# dirPath=r"C:\book"

# name for book details file, every file will be named fileName_currentDatetime
fileName = "MyBookDetails"


GRWS.BookDetailsFromBarCodeGooDReadersFirst.GetBookDet(self,
barcodeImgDir=dirPath
,bookDetFilesDir=outDir
,bookDetFileName=fileName
,headlessMode=False
)


