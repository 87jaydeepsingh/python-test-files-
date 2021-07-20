from tkinter import *
import speech_recognition as sr
from gtts import gTTS
import threading
import os
import webbrowser
from playsound import playsound
from datetime import datetime
def test():
    t2 = threading.Thread(target=test1)
    t2.start()

root=Tk()
root.title('Assistence')
l1=Label(root)
b1=Button(root,text="Speak",width="30",height="10",command=test)
b1.pack()

def test1():
    playsound('abcd.mp3')
    test=datetime.now()
    h=test.hour
    m=test.minute
    s=test.second
    d=test.day
    M=test.month
    y=test.year
    timestr=str(h)+":"+str(m)+":"+str(s)
    datestr=str(d)+":"+str(M)+":"+str(y)
    l1['text']=""
    l1.pack()
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=7)
        l1['text']="Speak"
        audio = r.listen(source)
        abc=r.recognize_google(audio)
        l1['text']="Command:"+abc
        list1=abc.split(' ',1)
        try:
            filt=list1[0]           
            main=list1[1]            
            list2=abc.split()           
            fread=list2[1]            
            txt=list2[2]            
            fout=list2[3]
            exp=list2[4]
            get=list2[5]
            fol=list2[6]
            init=list2[7]
        finally:
            if filt=="play" and txt=="from":
                if exp=="folder":
                    os.startfile(fol+":\\"+fout+"\\"+fread+".mp3")
                else:
                    os.startfile(fout+":\\"+fread+".mp3")
                
            elif filt=="document":
                if txt=="from" and exp=="drive":
                    os.startfile(fout+":\\"+fread+".docx")
                elif txt=="in":
                    os.startfile(fol+":\\"+fout+"\\"+fread+".docx")
                    
            elif filt=="powerpoint":
                if txt=="from" and exp=="drive":
                    os.startfile(fout+":\\"+fread+".pptx")
                elif txt=="in":
                    os.startfile(fol+":\\"+fout+"\\"+fread+".pptx")
                    
            elif filt=="excel" and exp=="drive":
                if txt=="from":
                    os.startfile(fout+":\\"+fread+".xlsx")
                elif txt=="in":
                    os.startfile(fol+":\\"+fout+"\\"+fread+".xlsx")
                    
            elif filt=="play":
                webbrowser.open("https://www.youtube.com/results?search_query="+main)
                
            elif filt=="open":   
                webbrowser.open("www."+main+".com")
                
            elif filt=="text":
                if txt=="from" and exp=="drive":
                    os.startfile(fout+":\\"+fread+".txt")
                elif txt=="in":
                    os.startfile(fol+":\\"+fout+"\\"+fread+".txt")
                    
            elif filt=="search":
                webbrowser.open("https://www.google.co.in/search?q="+main)
            elif filt=="time":
                l1['text']+="\nTime:"+timestr
            elif filt=="date":
                l1['text']+="\nDate:"+datestr
            else:
                print("failed")
root.mainloop()
