## Copyright (Abeer Joshi)

#___________________________________________________Imports_________________________________________________
import speech_recognition as sr
from tkinter import *
from tkinter import messagebox
import tqdm
import pyttsx3
import datetime
import webbrowser
import subprocess
import os
import wikipedia
import datetime
current_time = datetime.datetime.now()
print (">>> Last Executed:  ", end = "")
print (current_time)
from tqdm import tqdm
import time
print(">>> Booting...[Speak 'Support' to report issue/bugs]")
for i in (range(100)):
    time.sleep(0.001)
print(">>> Boot Complete! Loading Environment...")

def main():
    #_______________________________________________________________Speech to text____________________________
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration = 2)
            print("________________")
            print(">>> Listening...")
            voice = listener.listen(source, phrase_time_limit=10)
            text = listener.recognize_google(voice)
            text = text.lower()
            print("Abeer : ", text)
    except Exception as e:
        print(e)
        print("Didn't get that. kidly try again sir.")
        main()
    #_____________________________________________________text to Speech_________________________________
    #_________________________________________________________________texts_________________________________

    if "hi" in text:
        pass
    elif "hello" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("Hello, how can I help you?")
        engine.runAndWait()     
    elif "thank you" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("Your welcome, I am always there to help you!")
        engine.runAndWait()
    elif "thanks" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("Never mind, Abeer")
        engine.runAndWait()
    elif "check for updates" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("Checking for updates")
        engine.say("Nope. There aren't any.")
        engine.runAndWait()
    elif text == "help":
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("I can help you with several things, I can be used as a simple google searcher and find great things or deals while you are online!")
        engine.say("I can also shutdown your computer and perform several tasks in your operating system, in the latest version of mine there is a lot of flexiblity, and I can also open your favourite webpages for sure.")
        engine.runAndWait()
    elif "how are you" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("I am good and you?")
        engine.runAndWait()
    elif "Google" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("opening Google")
        engine.runAndWait()
        webbrowser.open("www.google.com")
    elif "youtube" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("Opening Youtube")
        engine.runAndWait()
        webbrowser.open("www.youtube.com")
    elif "gmail" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("Opening G-mail")
        engine.runAndWait()
        webbrowser.open("https://mail.google.com/")
    elif "music" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("playing music online")
        engine.runAndWait()
        webbrowser.open("https://www.open.spotify.com/")
    elif "notepad" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("opening notepad")
        engine.runAndWait()
        subprocess.call('notepad.exe')
    elif "echo" in text:
        ech = input('What do you want to hear from Volta? : ')
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say(ech)
        engine.runAndWait()
    elif "calculator" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("opening calculator")
        engine.runAndWait()
        subprocess.call('calc.exe')
    elif "who are you" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("I am Volta. your personal assistant Abeer")
        engine.runAndWait()
    elif "google" in text:
        er = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                er.adjust_for_ambient_noise(source, duration = 2)
                print("Listening, for a Google Query...")
                vo = er.listen(source, phrase_time_limit=10)
                go = er.recognize_google(vo)
                go = go.lower()
                print("Google Query: ", go)
        except Exception as e:
            print(e)
            print("Didn't get that. kidly try again sir to search google")
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")
        qu = go
        for j in search(qu, tld="co.in", num = 10, stop=5, pause=5):
            print(j)
        yena = input('Want to open these results in Browser? (Type yes/no) :  ')
        if yena == 'yes':
            webbrowser.open(j)
        elif yena == 'no':
            pass
        elif yena == 'alright':
            webbrowser.open(j)
        elif yena == 'sure':
            webbrowser.open(j)
        else:
            print("Kindly run the script again and then try to type yes or no...")
    elif "shut down" in text:
        run = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                run.adjust_for_ambient_noise(source,duration = 2)
                print("Are you sure you want to Shutdown your computer?")
                vio = run.listen(source, phrase_time_limit=10)
                gu = run.recognize_google(vio)
                gu = gu.lower()
                print("Shutdown?: ", gu)
        except Exception as e:
            print(e)
            print("Didn't get that. kidly try again")        
            #
        if "yes" in gu:
            engine = pyttsx3.init()
            engine.setProperty("rate",130)
            engine.say("Closing Programs and services. Preparing to Shutdown")
            engine.runAndWait()
            os.system("shutdown /p")
        elif "no" in gu:
            print("Shutdown Aborted")
        else:
            print("Kindly run the script again, and answer in 'yes' or 'no' ")

    elif "shutdown" in text:
        run = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                run.adjust_for_ambient_noise(source,duration = 2)
                print("Are you sure you want to Shutdown your computer? (yes/no)")
                vio = run.listen(source, phrase_time_limit=10)
                gu = run.recognize_google(vio)
                gu = gu.lower()
                print("Shutdown?: ", gu)
        except Exception as e:
            print(e)
            print("Didn't get that. kidly try again")        
            #
        if "yes" in gu:
            engine = pyttsx3.init()
            engine.setProperty("rate",130)
            engine.say("Closing Programs and services. Preparing to Shutdown")
            engine.runAndWait()
            os.system("shutdown /p")
        elif "no" in gu:
            print("Shutdown Aborted")
        else:
            print("Kindly run the script again, and answer in 'yes' or 'no' ")
    elif "deactivate" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("Deactivating Program")
        engine.runAndWait()
        exit()
    elif "bye" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("Bye")
        engine.runAndWait()
        exit()
    elif "exit" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("Deactivating Program")
        engine.runAndWait()
        exit()    
    elif "pause" in text:
        pu = input('Volta Paused!. hit ENTER to resume Volta...')
        if pu == '':
            pass
        else:
            exit()
    elif "happy" in text:
        print("I am happy to know that you are happy!")
    elif "coin" in text:
        import random
        print("You got a: ")
        coin = ['> Head', '> Tails']
        print(random.choice(coin))
    elif "volta" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate",130)
        engine.say("Over here, I am here to help you out")
        engine.runAndWait()
    elif "time" in text:
        now = datetime.datetime.now()
        print(now.strftime("Time:  %H:%M"))
    elif "web address" in text:
        opwe = input('Enter web address: ')
        webbrowser.open(opwe)
    elif text == 'open':
        opwe = input('Enter web address: ')
        webbrowser.open(opwe)
    elif "my day" in text:
        def todo():
            root = Tk()
            root.title('Abeer Joshi')
            root.geometry('300x400')
            root.resizable(0, 0)
            Label(root, text='My Day', font=("Trebuchet", 15), wraplength=300).pack()
            tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
            scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
            scroller.place(x=260, y=50, height=232)
            tasks.config(yscrollcommand=scroller.set)
            tasks.place(x=35, y=50)
            def add_item(entry: Entry, listbox: Listbox):
                new_task = entry.get()
                listbox.insert(END, new_task)
                with open('tasks.txt', 'a') as tasks_list_file:
                        tasks_list_file.write(f'\n{new_task}')
            def delete_item(listbox: Listbox):
                listbox.delete(ACTIVE)
                with open('tasks.txt', 'r+') as tasks_list_file:
                    lines = tasks_list_file.readlines()
                    tasks_list_file.truncate()
                    for line in lines:
                        if listbox.get(ACTIVE) == line[:-2]:
                            lines.remove(line)
                        tasks_list_file.write(line)
                    tasks_list_file.close()
            with open('tasks.txt', 'r+') as tasks_list:
                for task in tasks_list:
                    tasks.insert(END, task)
                tasks_list.close()
            new_item_entry = Entry(root, width=37)
            new_item_entry.place(x=35, y=310)
            add_button = Button(root,border = "0", text='Add Item', bg='Azure', width=10, font=('Helvetica', 12),
                            command=lambda: add_item(new_item_entry, tasks))
            add_button.place(x=45, y=350)
            delete_btn = Button(root,border = "0", text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12),
                            command=lambda: delete_item(tasks))
            delete_btn.place(x=150, y=350)
            root.update()
            root.mainloop()
        todo()
    elif text == 'support':
        root = Tk()
        root.title("Volta Support")
        root.geometry("350x300+500+150")
        la = Label(root, text = "Volta Support").pack()
        howla = Label(root, text = "Tell me, what is the issue?").place(x = 12, y = 40)
        inp = Text(root, height = 10, width = 40).place(x = 12.5, y = 70)
        def jand():
            messagebox.showinfo("Success!", "Reported issue Successfully!")
        bu = Button(root, text = "Report", bg = "light Blue", fg = "Black", command = jand).place(x = 12, y = 250)
        root.mainloop()
    elif "wikipedia" in text:
        #
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source,duration = 5)
                print("Listening for a Wikipedia Query...")
                voi = r.listen(source)
                wk = r.recognize_google(voi)
                wk = wk.lower()
                print("Search Wikipedia: ",wk)
        except Exception as e:
            print(e)
            print("Didn't get that. kidly try again to search Wikipedia")
        #
        ru = wk
        result = wikipedia.summary(ru, sentences = 2)
        engine = pyttsx3.init()
        engine.setProperty("rate", 130)
        engine.say(result)
        engine.runAndWait()
    elif "weather" in text:
        engine = pyttsx3.init()
        engine.setProperty("rate", 130)
        engine.say("Got it, opening the result in Browser. Kindly wait.")
        engine.runAndWait()
        webbrowser.open("https://www.accuweather.com/en/in/ghaziabad/206683/weather-forecast/206683")
    elif "add" in text:
        subprocess.call('calc.exe')
    elif "subtract" in text:
        subprocess.call('calc.exe')
    elif "multiply" in text:
        subprocess.call('calc.exe')
    elif "divide" in text:
        subprocess.call('calc.exe')
    elif "map" in text:
        mapu = input('Search for a place: ')
        webbrowser.open("https://www.google.com/maps/place/" + mapu)
    elif "navigate" in text:
        mapu = input('Search for a place: ')
        webbrowser.open("https://www.google.com/maps/place/" + mapu)
    elif "route" in text:
        mapu = input('Search for a place: ')
        webbrowser.open("https://www.google.com/maps/place/" + mapu)
    else:
        print("Unable to get that, please try again. Make sure you have a proper internet connection...")
        main()        
for x in range(1000000000000):
    main()
    

## Copyright (Abeer Joshi)
