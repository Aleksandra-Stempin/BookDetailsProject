import os
import simpleaudio as sa
class PingMeWithSimpleaudio():
    global _successSoundPath
    global _failSoundPath
    _successSoundPath = r'sounds\ok.wav'
    _failSoundPath = r'sounds\notOk.wav'
    # _successSoundPath = r"C:\Users\aleksandra.stempin\OneDrive - Accenture\!Sync\Desktop\ok.wav"

    def _playSound(self, soundName, infoText=""):
        try:
            if len(infoText)>1:
                print("\n"+infoText+"\n")
            if str(soundName).endswith(".wav") and os.path.exists(soundName):
                # audio_message = AudioSegment.from_wav(soundName)
                # play(audio_message)
                audio_message = sa.WaveObject.from_wave_file(soundName)
                play_audio_message = audio_message.play()
                play_audio_message.wait_done()
            else:
                print("Sound %s couldn't be played." % soundName)

        except Exception as e:
            errMsg = "\nError in pydub sound: %s\nerror: %s\n" % (soundName, str(e))
            print(errMsg)

    def succesNotification(self):
         PingMeWithSimpleaudio._playSound(self, soundName=_successSoundPath, infoText="Everything ok.")

    def failNotification(self):
        PingMeWithSimpleaudio._playSound(self, soundName=_failSoundPath, infoText="Something bad has happened, I am "
                                                                                  "so sorry.")




