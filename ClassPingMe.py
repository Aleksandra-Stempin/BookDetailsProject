# if you get an error "Cannot specify extra characters after a string enclosed in quotation marks." downgrade playsound
# pip uninstall playsound
# pip install playsound==1.2

from playsound import playsound
from self import self
import os

class PingMe():
    global _successSoundPath
    global _failSoundPath
    _successSoundPath = r'sounds\ok.mp3'
    _successSoundPath = 'sounds/ok.mp3'
    # _successSoundPath = r'C:\Users\Olenka\PycharmProjects\BookDetailsProject2\sounds\ok.mp3'
    _failSoundPath = r'sounds\notOk.mp3'


    def _PlaySound(self, soundName, infoText=""):
        try:
            print("\n"+infoText+"\n")
            # print("sound is file", os.path.exists(soundName))
            if str(soundName).endswith(".mp3") and os.path.exists(soundName):
                playsound(str(soundName))
            else:
                print("Sound %s couldn't be played."%soundName)
        except Exception as e:
            errMsg = "Error in PlaySound sound: %s\nerror: %s"%(soundName, str(e))
            print("\n"+errMsg+"\n")

    def SuccessNotyfication(self):
        PingMe._PlaySound(self, soundName= str(_successSoundPath), infoText="Everything ok")


    def FailNotyfication(self):
        PingMe._PlaySound(self, soundName=str(_failSoundPath), infoText="Something bad has happened, I am so sorry.")


