import speech_recognition as sr
import threading
import time

# obtain path to "english.wav" in the same folder as this script
#from os import path
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "F:\\UIPath\\Python\\Speech Recognition\\night.wav")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
#r=sr.Recognizer()
#with sr.AudioFile(AUDIO_FILE) as source:
#    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
#try:
#    print("Sphinx thinks you said \n" + r.recognize_sphinx(audio))
#except sr.UnknownValueError:
#    print("Sphinx could not understand audio")
#except sr.RequestError as e:
#    print("Sphinx error; {0}".format(e))

#This will create a WAV file called microphone-results.wav, containing the recorded audio,
#import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=5)
    r.dynamic_energy_threshold = True
    print("Say something!")
    audio = r.listen(source,phrase_time_limit=5)
#    time.sleep(5);
    print("Done listening!")
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())
try:
    print("Sphinx thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


#with sr.Microphone() as source:
#with sr.Microphone(1) as source:
#with sr.Microphone(7) as source:
#with sr.Microphone(15) as source:
#with sr.Microphone(18) as source:
#r = sr.Recognizer()
#with sr.Microphone() as source:
#    r.adjust_for_ambient_noise(source, duration=5)
#    r.dynamic_energy_threshold = True
#    print("SAY SOMETHING");
#    audio = r.listen(source)
#    time.sleep(5);
#    print("TIME OVER, THANKS");

#try:
#    print("You said " + r.recognize(audio))
#    print("TEXT: " + r.recognize_google(audio));
#    print("TEXT in Hindi: " + r.recognize_google(audio, language='hi-IN'));
#    print("Could not understand audio")
#except sr.UnknownValueError:
#    print("Sorry sir, but, I could not understand what you said!")
#except sr.RequestError as e:
#    print("Could not request results from Google Speech Recognition service; {0}".format(e))
#except:
#    pass;