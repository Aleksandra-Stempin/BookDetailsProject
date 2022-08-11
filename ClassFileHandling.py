import os


class CreateWriteReadCloseFiles():
    """file handling"""
    import datetime as dt
    import os.path
    myFileName= ""
    def __init__(self, filesOutDir, fileName):
        self.filesOutDir = filesOutDir
        self.fileName = fileName

    def _CreateDataTimeStamp(self):
        """create datestamp in format YYYY-MM-DD_hh-mm-ss"""
        currTime = self.dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return currTime

    def _CreateFileName(self):
        """creates file name in format name_datestamp"""
        ts = self._CreateDataTimeStamp()
        # full file's path
        fullFileName = "{}_{}".format(self.fileName, ts)
        return fullFileName

    def CreateFile(self):
        """creating new text file with encoding utf-8 and saving in out folder"""
        global myFile
        global myFileName
        myFileName = "{}\{}.txt".format(self.filesOutDir,self._CreateFileName())
        myFile = open(myFileName, 'a', encoding="utf-8")
        # print(myFileName + " has been created")

    def ReadFile(self, filePath):
        """reads from file"""
        textFromFile = ""
        try:
            fileExists = self.os.path.exists(filePath)
            if fileExists:
                f = open(filePath)
                textFromFile = f.read()
                f.close()
            else:
                print("File {} doesn't exist".format(myFileName))
        except Exception as e:
            errMsg = "Something is wrong\n{}".format(str(e))
            print(errMsg)
        finally:
            return textFromFile

    def ReadMyFile(self):
        """reads from file"""
        textFromFile = ""
        try:
            fileExists = self.os.path.exists(myFileName)
            print(fileExists)


            if True:
                f = open(myFileName, 'r', encoding="utf-8")
                textFromFile = f.read()
                print("textFromFile", textFromFile)
                f.close()
            else:
                print("File {} doesn't exist".format(myFileName))
        except Exception as e:
            errMsg = "Something is wrong\n{}".format(str(e))
            print(errMsg)
        finally:
            return textFromFile

    def WriteToFile(self, textToFile):
        """writes to file"""
        try:
            fileExists = self.os.path.exists(myFileName)
            if fileExists:
                textToFile = textToFile + "\n"
                myFile.write(textToFile)
            else:
                print("File {} doesn't exist".format(myFileName))
        except Exception as e:
            errMsg = "Something is wrong\n{}".format(str(e))
            print(errMsg)

    def CloseFile(self):
        """writes to file"""
        try:
            fileExists = self.os.path.exists(myFileName)
            if fileExists:
                myFile.close()
            else:
                print("File {} doesn't exist".format(myFileName))
        except Exception as e:
            errMsg = "Something is wrong\n{}".format(str(e))
            print(errMsg)

    def DeleteFile(self):
        """deletes file"""
        try:
            os.remove(myFileName)
        except Exception as e:
            print("DeleteFile not ok", str(e))
            pass








# outDir = r"C:\Users\aleksandra.stempin\OneDrive - Accenture\!Sync\Downloads\testFilesFolder"
# fileName = "MyFile"
# screenShotName = "MySC"
# # readFile = r"C:\Users\aleksandra.stempin\OneDrive - Accenture\!Sync\Downloads\testFilesFolder\MyFile_2022-07-06_12-00-55.txt"
# fs = CreateWriteReadCloseFiles()
# fs.CreateFile(outDir, fileName)
# # fs.WriteToFile("nakarm kitku")
# # fs.CloseFile()
# # fs.ReadFile(readFile)