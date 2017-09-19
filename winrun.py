import pyttsx3
import subprocess
import sys

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# If no argument terminated then

t2s = ''
import speech_recognition as sr

while True:
    print("Recording Voice")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print("Analyzing")
        input = r.recognize_google(audio)
    except:
        # t2s = "Sorry I can't recognize your speech"
        # engine.say(t2s)
        # engine.runAndWait()
        continue
    callstr = "python core.py " + "\"" + input + "\""
    callback = subprocess.Popen(callstr, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    t2s = str(callback.communicate()[0])
    t2s = t2s.replace("\\r", '')
    t2s = t2s.replace("\'b\'", '')
    t2s = t2s.replace("b\'", '')
    t2s = t2s.replace("b\"", '')
    t2s = t2s.replace("\'", '')
    t2s = t2s.replace("\\n", '')
    t2s = t2s.replace("\"", '')
    engine.say(input)
    engine.say(t2s)
    print(t2s)
    print(input)
    engine.runAndWait()
    if '!shutdown' in t2s:
        sys.exit()
