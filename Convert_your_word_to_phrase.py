from gtts import  gTTS  # pip install gtts

import pyttsx3 # pip install pyttsx3
import os 
import sys 

def menu():
    print("================================")
    print("Convert a Text File into Speech") 
    print("================================")
    option= input("[A]-English\n[B]-French\n[C]-Arabic \n[M]-Menu\n[Q]-Quit\n======================\n[#]-Enter your Choice: ").upper()

    if option == "M":
        return menu() 
    
    #Exist 
    if option == "Q": 
        print("Thank you for using my App")
    
    #Input /Text , Name File
    text=input("Enter your Text: ") 
    name = input("name of your file: ")
    
    #voice = gTTS(text, lang='en', slow=True)
    #voice='male_2-local')
    
    #English 
    if option == "A":
        tts= gTTS(text, lang='en', slow='True')
    
    #French
    if option == "B": 
        tts= gTTS(text, lang='fr', slow="True")
        
   #Arabic
    if option=="C": 
        tts= gTTS(text, lang='ar', slow="True") 
    
    # create file 
    if not os.path.isfile(name):
        f = open(name, "w")
        f.write(name)
        tts.save(name+'.'+'mp3')
        print("Done!")
        sys.exit()
    #check if exist 
    if os.path.exists(name):
        name = input("It's Exist, Enter your new file: ")
        f = open(name, "w")
        f.write(name)
        tts.save(name+'.'+'mp3')
        print("Done!")
        sys.exit()
        
      
        
menu()
        
