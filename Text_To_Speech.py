﻿import PyPDF2 
import gtts
from gtts import gTTS
import pyttsx3
import langdetect
from deep_translator import GoogleTranslator
import googletrans
import os
import time
import re
from nltk import tokenize
from playsound import playsound
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys, os

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)


class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("untitled.ui", self)
        self.show()
        self.setWindowTitle("Text_To_Speech")
        self.setWindowIcon(QIcon("Cult-Cover.jpg"))
        shortcut = QKeySequence(Qt.CTRL + Qt.Key_Q)
        self.shortcut = QShortcut(shortcut, self)
        self.shortcut.activated.connect(self.Close)
        
        #****************Speed*********************#
        self.pushButton_5.clicked.connect(self.Speed)
        self.pushButton.clicked.connect(self.Save_Speed)
        self.pushButton_2.clicked.connect(self.Preview_Speed)
        
        #****************Volume*********************#
        self.pushButton_6.clicked.connect(self.Volume)
        self.pushButton_4.clicked.connect(self.Save_Volume)
        self.pushButton_3.clicked.connect(self.Preview_Volume)
        

        self.pushButton_7.clicked.connect(self.GO)
    
    def Close(self):
        sys.exit()

    #****************Speed*********************#
    def Speed(self):
        self.spinBox.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        
    def Preview_Speed(self):
        Preview_Text="Acesta este un text pentru a testa rata de vorbire a vocii. Daca vorbeste prea rapid micsorati viteza!"
        rate=self.spinBox.value()
        print(rate)
        engine.setProperty('rate', rate)
        engine.say(Preview_Text)
        engine.runAndWait()
        engine.setProperty('rate', 200)

    def Save_Speed(self):
        rate=self.spinBox.value()
        engine.setProperty('rate', rate)
        print(rate)
        self.spinBox.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
    
    #****************Volume*********************#
    def Volume(self):
        self.doubleSpinBox.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        
    def Preview_Volume(self):
        Preview_Text="Acesta este un text pentru a testa volumul de vorbire a vocii. Daca vorbeste prea tare micsorati volumul!"
        vol=self.doubleSpinBox.value()
        print(vol)
        engine.setProperty('volume', vol)
        engine.say(Preview_Text)
        engine.runAndWait()
        engine.setProperty('volume', 1.0)

    def Save_Volume(self):
        vol=self.doubleSpinBox.value()
        engine.setProperty('volume', vol)
        print(vol)
        self.doubleSpinBox.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        

    def GO(self):
        Text=""

        Translator=googletrans.Translator()

        page_no=len(reader.pages)

        Translate_From_Language=Function_Detect_Text_Language()

        Text=Function_Translate_Text(Text, page_no, Translate_From_Language)    

        lista=Function_Delete_First_Pages(Text)
        #lista.pop(0)

        lista=Function_Split_In_Chapters(Text, lista)

        Piste=Function_Split_In_20min(lista)

        Function_Creare_Piste(Piste)



def Function_Detect_Text_Language():
    Page_Reader=reader.pages[50]
    Page_Text=Page_Reader.extract_text()

    langdetect.DetectorFactory.seed = 0
    Translate_From_Language=langdetect.detect(Page_Text)
    print(Translate_From_Language)
    return(Translate_From_Language)

def Function_Translate_Text(Text, page_no, Translate_From_Language):
    #page_no
    for i in range(page_no):
        Page_Reader=reader.pages[i]
        Page_Text=Page_Reader.extract_text()
    
        if "CONTENTS" in Page_Text:
            pass
        else:
            if Translate_From_Language != "ro":
                Translated_Page=GoogleTranslator(source=Translate_From_Language, target="ro").translate(Page_Text)
                #Translated_Page=str(Translator.translate(Page_Text, src=Translate_From_Language, dest="ro"))
                Text=Text+Translated_Page
            else:
                Text=Text+Page_Text
            print("Pagina-",i,"a fost tradusa si scrisa.")
    
    print(len(Text))
    return Text

def Function_Delete_First_Pages(Text):
    lista=[]
    lista=re.split('(CAPITOLUL I\n)', Text)
    str_count=lista.count("CAPITOLUL I\n")
  
    find=0
    for i in lista:
        if i!="CAPITOLUL I\n" and find!=str_count:
            lista.remove(i)
            find=find+1
 
    #print(lista)
    return lista

def Function_Split_In_Chapters(Text, lista):
    Text=""
    for i in lista:
        Text=Text+i
    
    lista=re.split('CAPITOLUL', Text)
    
    lista.pop(0)
    for i in range(len(lista)):
        lista[i]="CAPITOLUL"+lista[i]
    print(lista)

    return lista

def Function_Split_In_20min(lista):
    for i in range(len(lista)):
        print("\n")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(f"CAPITOLUL {i+1}")
        print(len(lista[i].split()))
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    piste=[]
    propozitii=[]
    parte=""
    for i in range(len(lista)):
        parte=""
        length=len(lista[i].split())
        if length >2900:
            propozitii=re.split('(\.)', lista[i])
            for j in propozitii:
                if len(parte.split())<2900:
                    parte=parte+j
                else:
                    piste.append(parte)
                    parte=""
            if parte!="":
                if len(parte.split())<=1000:
                    piste[-1]=piste[-1]+parte
                else:
                    piste.append(parte)
        else:
            piste.append(lista[i])

    for i in range(len(piste)):
        print("\n\n")
        print(len(piste[i].split()))
        print(f"PARTEA {i+1}")
        print(piste[i])
        
    return piste

def Function_Creare_Piste(Piste):
    count=1
    for i in Piste:
        print("***PISTA***")
        print(i)
        folderpath=r'C:\Users\Volmer\OneDrive\Desktop\Carti Audio\Allans-Wife--Carte Audio--Sintetic'
        filename=f"Pista-{count}--Allans-Wife.mp3"
        save_path=os.path.join(folderpath, filename)
        engine.save_to_file(f"Pista {count}"+i, save_path)
        engine.runAndWait()
        print("Pista", count, "a fost salvata.")
        count=count+1
    playsound('F:\Teme Programare\Text-To-Speech\Text-To-Speech\ding.mp3')
    

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_roRO_Andrei")
engine.setProperty('rate', 145)
engine.setProperty('volume', 1.0)

reader=PyPDF2.PdfReader(r'C:\Users\Volmer\OneDrive\Desktop\Carti PDF\Procesate\Allans-Wife.pdf')

   



app=QApplication([])
window=MyGUI()
app.exec_()

r"""
n=10000
Substrings=[]
for i in range(0, len(Text), n):
    substring=Text[i:i+n]
    Substrings.append(substring)



    len(Substrings)
for i in range(len(Substrings)):
    folderpath=r'C:\Users\Volmer\OneDrive\Desktop\Carti Audio\The-Travels-of-Marco-Polo-Volume-2--Carte Audio--Sintetic'
    filename=f"Pista-{i}--The-Travels-of-Marco-Polo-Volume-2.mp3"
    save_path=os.path.join(folderpath, filename)
    
    #Text_To_Speech=gTTS(text=f"Pista {i}"+Substrings[i], lang='ro', slow=False)
    #Text_To_Speech.save(save_path)
    engine.save_to_file(f"Pist {i}"+Substrings[i], save_path)
    engine.runAndWait()
    print("Pista", i, "a fost salvata.")
"""