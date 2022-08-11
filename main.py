import ClassBookDetailsToFileFromBarcode as BD
import ClassBookDetailsReadBarCodeWebScraping as WS
import ClassBookDetailsFromBarCodeGooDReadersFirst as GRWS
import self
import ClassFileHandling as fh
import sys
outDir = r"C:\Users\aleksandra.stempin\OneDrive - Accenture\!Sync\Downloads\testFilesFolder"
dirPath = r'C:\Users\aleksandra.stempin\OneDrive - Accenture\!Sync\Downloads\NewBooks'
fileName = "MyBookDetails"


GRWS.BookDetailsFromBarCodeGooDReadersFirst.GetBookDet(self,
barcodeImgDir=dirPath
,bookDetFilesDir=outDir
,bookDetFileName=fileName
,headlessMode=False
)


