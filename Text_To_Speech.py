import pypdf
import gtts
from gtts import gTTS
import pyttsx3
import langdetect
from deep_translator import GoogleTranslator
import googletrans
import os
import time
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_roRO_Andrei")


reader=pypdf.PdfReader(r'C:\Users\Volmer\OneDrive\Desktop\Carti PDF\The-Travels-of-Marco-Polo-Volume-2.pdf')
Text=""

Translator=googletrans.Translator()

page_no=len(reader.pages)

Page_Reader=reader.pages[50]
Page_Text=Page_Reader.extract_text()

langdetect.DetectorFactory.seed = 0
Translate_From_Language=langdetect.detect(Page_Text)
print(Translate_From_Language)

Text=""
#page_no
for i in range(39, page_no):
    Page_Reader=reader.pages[i]
    Page_Text=Page_Reader.extract_text()
    
    if Translate_From_Language != "ro":
        Translated_Page=GoogleTranslator(source=Translate_From_Language, target="ro").translate(Page_Text)
        #Translated_Page=str(Translator.translate(Page_Text, src=Translate_From_Language, dest="ro"))
        Text=Text+Translated_Page
    else:
        Text=Text+Page_Text
    print("Pagina-",i,"a fost tradusa si scrisa.")
    
print(len(Text))

n=10000
Substrings=[]
for i in range(0, len(Text), n):
    substring=Text[i:i+n]
    Substrings.append(substring)



    #len(Substrings)
for i in range(len(Substrings)):
    time.sleep(60)
    folderpath=r'C:\Users\Volmer\OneDrive\Desktop\Carti Audio\The-Travels-of-Marco-Polo-Volume-2--Carte Audio--Sintetic'
    filename=f"Pista-{i}--The-Travels-of-Marco-Polo-Volume-2.mp3"
    save_path=os.path.join(folderpath, filename)
    
    #Text_To_Speech=gTTS(text=f"Pista {i}"+Substrings[i], lang='ro', slow=False)
    #Text_To_Speech.save(save_path)
    engine.save_to_file(f"Pist {i}"+Substrings[i], save_path)
    engine.runAndWait()
    print("Pista", i, "a fost salvata.")
    
