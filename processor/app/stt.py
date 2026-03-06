import speech_recognition as sr
r = sr.Recognizer()

def speech_to_text(file_path):
    file = sr.AudioFile(file_path)
    with file as source:
        audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        print("Text: "+s)
    except Exception as e:
        print("Exception: "+str(e))
