import sys
import subprocess
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', "importlib"])
import importlib.util
successfullyInstalledPackages = []
alreadyInstalledPackages = []
missingPackages = []

# packagesList = ["pandas", "playsound", "ssl", "Django"]
packagesList=["selenium"
,"os"
,"datetime"
,"re"
,"time"
,"playsound"
,"simpleaudio"
,"os"
,"cv2"
,"pyzbar"
,"webdriver_manager"
,"webdriver_manager"
,"requests","urllib3"
,"ssl"
,"lxml.html"
]


for package in packagesList:
    packageInstalled = (importlib.util.find_spec(package) is not None)
    print(package, packageInstalled)
    if not packageInstalled:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            successfullyInstalledPackages.append(package)
        except Exception as e:
            errMsg = """
Package %s has not been installed,
error: %s
"""%(package, str(e))
            missingPackages.append(package)
            pass
    else:
        alreadyInstalledPackages.append(package)

successfullyInstalledPackagesStr = str(successfullyInstalledPackages).replace("'","")\
    .replace("[", "")\
    .replace("]","")

alreadyInstalledPackagesStr = str(alreadyInstalledPackages).replace("'","")\
    .replace("[", "")\
    .replace("]","")

missingPackegesStr = str(missingPackages).replace("'", "")\
    .replace("[", "")\
    .replace("]","")

summaryTxt = """

Summary:
successfully installed packages: %s
already installed packages: %s
unsuccessfully installed packages: %s

"""%(successfullyInstalledPackagesStr, alreadyInstalledPackagesStr, missingPackegesStr)

print(summaryTxt)





