from csv import reader
from pickletools import uint1
import PyPDF2
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget 
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
import threading
import nltk

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
ui="UI/English.ui"
class Language_Window(QMainWindow):
    
    SelectedUi="UI/English.ui"
    
    def __init__(self):
        super(Language_Window, self).__init__()
        self.Language_Window=QMainWindow()
        uic.loadUi("UI/Language_Select.ui", self)
        self.show()
        self.setWindowTitle("Text_To_Speech")
        self.setWindowIcon(QIcon("App_Icon.png"))
        
        #****************Language*********************#
        comboBox=QComboBox()
        self.comboBox.addItems(["Romana", "English", "Español"])
        self.pushButton.clicked.connect(self.OpenMainWindow)
        
        
    def OpenMainWindow(self):
        
       
        global ui
        ui="UI/"+self.comboBox.currentText()+".ui"
        print(ui)
        global window
        window=MyGUI()
        window.show()

class MyGUI(QMainWindow):
        
    def __init__(self):
        
        super(MyGUI, self).__init__()
        uic.loadUi(ui, self)

        self.setWindowTitle("Text_To_Speech")
        self.setWindowIcon(QIcon("App_Icon.png"))
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
        
        #****************Select Folder*********************#
        self.pushButton_8.clicked.connect(self.Select_Folder)
        
        #****************Save Folder*********************#
        self.pushButton_15.clicked.connect(self.Save_Folder)

        #****************Language*********************#
        """self.pushButton_10.clicked.connect(self.Language)
        comboBox=QComboBox()
        self.comboBox.addItems(["Romana", "English", "Español"])
        self.pushButton_13.clicked.connect(self.Save_Language)"""

        #****************Voice*********************#
        self.pushButton_11.clicked.connect(self.Voice)
        self.pushButton_14.clicked.connect(self.Save_Voice)

        #****************Progress Bar*********************#
        


        self.pushButton_7.clicked.connect(self.RunGO)
    
    def Close(self):
        sys.exit()

    #****************Speed*********************#
    def Speed(self):
        self.horizontalSlider.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        
    def Preview_Speed(self):
        Preview_Text="Acesta este un text pentru a testa rata de vorbire a vocii. Daca vorbeste prea rapid micsorati viteza!"
        rate=self.horizontalSlider.value()
        print(rate)
        engine.setProperty('rate', rate)
        engine.say(Preview_Text)
        engine.runAndWait()
        engine.setProperty('rate', 200)

    def Save_Speed(self):
        rate=self.horizontalSlider.value()
        engine.setProperty('rate', rate)
        print(rate)
        self.horizontalSlider.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_15.setEnabled(True)
    
    #****************Volume*********************#
    def Volume(self):
        self.horizontalSlider_2.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        
    def Preview_Volume(self):
        Preview_Text="Acesta este un text pentru a testa volumul de vorbire a vocii. Daca vorbeste prea tare micsorati volumul!"
        vol=self.horizontalSlider_2.value()/10
        print(vol)
        engine.setProperty('volume', vol)
        engine.say(Preview_Text)
        engine.runAndWait()
        engine.setProperty('volume', 1.0)

    def Save_Volume(self):
        vol=self.horizontalSlider_2.value()/10
        engine.setProperty('volume', vol)
        print(vol)
        self.horizontalSlider_2.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_15.setEnabled(True)
     
    #****************Select Folder*********************#
    def Select_Folder(self):
        self.dirName_Select = QFileDialog.getOpenFileName(self, "Select Folder", "c:/", "PDF files (*.pdf)")
        directory=str(self.dirName_Select[0])
        print(directory)
        print(type(directory))
        self.reader=PyPDF2.PdfReader(directory)
        
        Books=str(self.dirName_Select[0]).split("/")
        for i in Books:
            if ".pdf" in i:
                self.Book_Name=i
        print(self.dirName_Select[0])
        print(Books)
        self.Book_Name=self.Book_Name.replace(".pdf", "")
        print(self.Book_Name)

    #****************Save Folder*********************#
    def Save_Folder(self):
        self.dirName_Save = QFileDialog.getExistingDirectory(self, "Select Folder", "c:/")
    
    #****************Language*********************#
    def Language(self):
        self.comboBox.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_10.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_15.setEnabled(False)
    
    def Save_Language(self):
        self.comboBox.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_10.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        
    #****************Voice*********************#
    def Voice(self):
        self.comboBox_2.setEnabled(True)
        self.pushButton_14.setEnabled(True)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        
    def Save_Voice(self):
        self.comboBox_2.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_15.setEnabled(True)

    def GO(self):
        Text=""

        Translator=googletrans.Translator()

        page_no=len(self.reader.pages)

        Translate_From_Language=Function_Detect_Text_Language(self.reader)

        Text=Function_Translate_Text(Text, page_no, Translate_From_Language, self.reader, self.progressBar,  self.progressBarValue)  
        
        #print(Text)

        
        propozitii=re.split("\.", Text)
        #print(propozitii)
        piste=[]
        parte=""
        for i in propozitii:
            length=len(nltk.word_tokenize(parte))
            #print(length)
            if length<2900:
                parte=parte+i+"."
            else:
                piste.append(parte)
                parte=""
                parte=""
        
        if parte!="":
            piste.append(parte)

        #print(piste)

        Function_Creare_Piste(piste, self.dirName_Save, self.Book_Name)


    def RunGO(self):
        threading.Thread(target=self.GO).start()

def Function_Create_Save(dirName_Save, Book_Name):
    folderpath=dirName_Save
    createfolder=f"{Book_Name}--Carte Audio--Sintetica"
    path=os.path.join(folderpath, createfolder)
    print(path)
    path=path.replace("\\", "/")
    print(path)
    os.makedirs(path)
    return path
    
    
def Function_Save_Pista(path, count, i, Book_Name):
    filename=f"Pista-{count}--{Book_Name}.mp3"#mp3
    save_path=os.path.join(path, filename)
    engine.save_to_file(f"{Book_Name} Pista {count}"+i, save_path)
    engine.runAndWait()

def Function_Detect_Text_Language(reader):
    Page_Reader=reader.pages[int(len(reader.pages)/2)]
    Page_Text=Page_Reader.extract_text()

    langdetect.DetectorFactory.seed = 0
    Translate_From_Language=langdetect.detect(Page_Text)
    print(Translate_From_Language)
    return(Translate_From_Language)

def Function_Translate_Text(Text, page_no, Translate_From_Language, reader):
    #page_no
    for i in range(page_no):
        Page_Reader=reader.pages[i]
        Page_Text=Page_Reader.extract_text()
    
        """if "CONTENTS" in Page_Text:
            pass
        else:"""
        if Translate_From_Language != "ro":
            Translated_Page=GoogleTranslator(source=Translate_From_Language, target="ro").translate(Page_Text)
            #Translated_Page=str(Translator.translate(Page_Text, src=Translate_From_Language, dest="ro"))
            Text=Text+Translated_Page
        else:
            Text=Text+Page_Text
        #print("Pagina-",i,"a fost tradusa si scrisa.")
    
    #print(len(Text))
    return Text

def Function_Delete_First_Pages(Text):
    lista=[]
    lista=re.split('(CAPITOLUL I\n)', Text)
    str_count=lista.count("CAPITOLUL I\n")
  
    find=0
    #find!=str_count
    for i in lista:
        if i!="CAPITOLUL I\n" and find!=str_count:
            lista.remove(i)
            find=find+1
 
    #print(lista)
    return lista
                
def Function_Split_In_Chapters(lista):
    Text=""
    for i in lista:
        Text=Text+i
    
    lista=re.split('Capitolul', Text, flags=re.IGNORECASE)
    
    lista.pop(0)
    for i in range(len(lista)):
        lista[i]="CAPITOLUL"+lista[i]
    #print(lista)

    return lista

def Function_Split_In_20min(lista):
    """for i in range(len(lista)):
        print("\n")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(f"CAPITOLUL {i+1}")
        print(len(lista[i].split()))
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")"""

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

    """for i in range(len(piste)):
        print("\n\n")
        print(len(piste[i].split()))
        print(f"PARTEA {i+1}")
        print(piste[i])"""
        
    return piste

def Function_Creare_Piste(piste, dirName_Save, Book_Name):
    path=Function_Create_Save(dirName_Save, Book_Name)
    count=1
    for i in piste:
        #print("***PISTA***")
        #print(i)
        """folderpath=dirName_Save
        createfolder=f"{Nume_Carte}--Carte Audio--Sintetica"
        path=os.path.join(folderpath, createfolder)
        filename=f"Pista-{count}--{Nume_Carte}.mp3"
        save_path=os.path.join(path, filename)
        engine.save_to_file(f"Pista {count}"+i, save_path)
        engine.runAndWait()"""
        print(dirName_Save)
        Function_Save_Pista(path, count, i, Book_Name)
        #print("Pista", count, Book_Name, "a fost salvata.")
        count=count+1
    playsound('ding.mp3')
    

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_roRO_Andrei")
engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)


app=QApplication([])
#window=MyGUI()
window=Language_Window()
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