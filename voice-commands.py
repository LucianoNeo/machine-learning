import speech_recognition as sr
import pyaudio as pa
import os

pa.PyAudio.get_default_input_device_info(0)


def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)

        print("Diga alguma coisa: ")

        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")

        elif "Excel" in frase:
            os.system("start Excel.exe")

    except sr.UnknownValueError:
        print("Não entendi")

        return frase


ouvir_microfone()
