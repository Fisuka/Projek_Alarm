from playsound import playsound
import tkinter as tk
import datetime
import time
import winsound
from threading import *
from pynput.keyboard import Key, Controller
from tkinter import *
from time import strftime
from PIL import Image, ImageTk

keyboard = Controller()

def volumeup():
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)

def volumdown():
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)

alarm_clock = Tk()

alarm_clock.title("Alarm Clock")
alarm_clock.geometry("1250x600+200+100")
alarm_clock.config(bg = "#02010A")

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

global hourt, minutet, secondt

def alarm():
    
    while True:
        set_alarm_time = f"{entri1.get()}:{entri2.get()}:{entri3.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        if current_time == set_alarm_time:
            print("Time to Wake up")
            freq = 5000

            # duration is set to 100 milliseconds
            dur = 10000

            winsound.Beep(1000,1000)
            winsound.Beep(1000,1100)
            winsound.Beep(1000,1200)
            winsound.Beep(1000,1300)
            break

def waktu():
    
    label1.config(text="Alarm Clock",font=("ds-digital",20,"bold"),bg="#04052E",fg='white')
    label1.place(x=321,y=23,width=734,height=65)
    label2.config(text="Set Time",font=("ds-digital",20,"bold"),bg="#04052E",fg='white', image='')
    label2.place(x=535,y=119,width=305,height=65)
    frame = Frame(alarm_clock)
    frame.pack()
    
    hourt=Label(text= "Hours :",font=("ds-digital",20,"bold"),bg="#001D3D",fg='white')
    hourt.place(x=292,y=215,width=243,height=65)
    entri1.config(font=("ds-digital",40,"bold"),bg="#140152",fg='white')
    entri1.place(x=292,y=300,width=243,height=65)

    minutet=Label(text= "Minutes :",font=("ds-digital",20,"bold"),bg="#001D3D",fg='white')
    minutet.place(x=566,y=215,width=243,height=65)
    entri2.config(font=("ds-digital",40,"bold"),bg="#140152",fg='white')
    entri2.place(x=566,y=300,width=243,height=65)

    secondt=Label(text= "Second :",font=("ds-digital",20,"bold"),bg="#001D3D",fg='white')
    secondt.place(x=840,y=215,width=243,height=65)
    entri3.config(font=("ds-digital",40,"bold"),bg="#140152",fg='white')
    entri3.place(x=840,y=300,width=243,height=65)

    button1.config(text="Set Alarm",font=("ds-digital",20,"bold"),bg="#04052E",fg='white',command=Threading)
    button1.place(x=292,y=380,width=243,height=65)
    button2.config(text="Volume UP", font=("ds-digital",20,"bold"),bg="#04052E",fg='white',command=volumeup)
    button2.place(x=566,y=380,width=243,height=65)
    button3.config(text="Volume Down", font=("ds-digital",20,"bold"),bg="#04052E",fg='white',command=volumdown)
    button3.place(x=840,y=380,width=243,height=65)
    button4.config(text="Disable",font=("ds-digital",20,"bold"),bg="#001D3D",fg='white',command=alarm_clock.destroy)
    button4.place(x=443,y=476,width=463,height=65)

def kalendar():
    date = datetime.datetime.now()
    format_date = f"{date:%A, %B %d %Y}"
    time_string = strftime('%H:%M:%S %p') # time format 

    label1.config(text=format_date, font=("ds-digital",20,"bold"), bg="#001D3D",fg='white')
    label1.pack(pady = 100)
    label2.config(text=time_string, font=("ds-digital",20,"bold"), bg="#001D3D",fg='white',image='')
    label2.pack()
    label2.after(1000,kalendar) # time delay of 1000 milliseconds
    
    entri1.config(state='disabled',bg="#000000",fg='black')
    entri2.config(state='disabled',bg="#000000",fg='black')
    entri3.config(state='disabled',bg="#000000",fg='black')
    
    button1.config(state='disabled',bg="#000000",fg='black')
    button2.config(state='disabled',bg="#000000",fg='black')
    button3.config(state='disabled',bg="#000000",fg='black')
    button4.config(state='disabled',bg="#000000",fg='black')

def stopwatch():
    counter = 66600
    running = False
    def counter_label(label2):
        def count():
            if running:
                global counter
    
                # To manage the initial delay.
                if counter==66600:            
                    display="Starting..."
                else:
                    tt = datetime.datetime.fromtimestamp(counter)
                    string = tt.strftime("%H:%M:%S")
                    display=string
    
                label2['text']=display 
                label2.after(1000, count) 
                counter += 1
    
        # Triggering the start of the counter.
        count()     
    
    # start function of the stopwatch
    def Start(label2):
        global running
                
        running=True
        counter_label(label2)
        button1['state']='disabled'
        button2['state']='normal'
        button3['state']='normal'
    
    # Stop function of the stopwatch
    def Stop():
        global running
        button1['state']='normal'
        button2['state']='disabled'
        button3['state']='normal'
        running = False
    
    # Reset function of the stopwatch
    def Reset(label2):
        global counter
        counter=66600
    
        # If rest is pressed after pressing stop.
        if running==False:      
            button3['state']='disabled'
            label2['text']="Welcome!"
    
        # If reset is pressed while the stopwatch is running.
        else:               
            label2['text']="Starting..."
    
    label1.config(text="Stopwatch",font=("ds-digital",20,"bold"),bg="#04052E",fg='white')
    label1.place(x=350,y=23,width=734,height=65)

    label2.config(text="", bg="#000000",fg='black',image='')
    label2.place(x=350,y=150,width=734,height=65)
 
    entri1.config(state='disabled',bg="#000000",fg='black')
    entri2.config(state='disabled',bg="#000000",fg='black')
    entri3.config(state='disabled',bg="#000000",fg='black')
 
    button1.config(text="Start", font=("ds-digital",40,"bold"),bg="#140152",fg='white', command=lambda:Start(label1))
    button1.place(x=350,y=215,width=243,height=65)

    button2.config(text="Stop", font=("ds-digital",40,"bold"),bg="#140152",fg='white',state='disabled', command=Stop)
    button2.place(x=350,y=300,width=243,height=65)

    button3.config(text="Reset", font=("ds-digital",40,"bold"),bg="#140152",fg='white', state='disabled', command=lambda:Reset(label1))
    button3.place(x=350,y=400,width=243,height=65)
    button4.config(state='disabled',bg="#000000",fg='black')

def timer():

    def set_timer():
        t = 0
        t = t+int(entri1.get())
        return t

    def countdown():
        global t
        t = int(entri1.get())
        if t > 0:
            print(t)
            label2.config(text=t, font=("ds-digital",40,"bold"),bg="#140152",fg='white')
            t = t-1
            label2.after(1000,countdown)
        elif t==0:
            print("end")
            label2.config(text="Gooo", font=("ds-digital",40,"bold"),bg="#140152",fg='white')

    label1.config(text="Timer",font=("ds-digital",20,"bold"),bg="#04052E",fg='white')
    label1.place(x=350,y=23,width=734,height=65)

    label2.config(text = "", font=("ds-digital",40,"bold"),bg="#140152",fg='white',image='')
    label2.place(x=350,y=119,width=305,height=65)

    times=StringVar()
    entri1.config( font=("ds-digital",40,"bold"),bg="#140152",fg='white', textvariable=times)
    entri1.place(x=350,y=215,width=243,height=65)

    entri2.config(state='disabled',bg="#000000",fg='black')
    entri3.config(state='disabled',bg="#000000",fg='black')

    button1.config(text="Set", font=("ds-digital",40,"bold"),bg="#140152",fg='white', command=set_timer)
    button1.place(x=350,y=300,width=243,height=65)

    button2.config(text="Start", font=("ds-digital",40,"bold"),bg="#140152",fg='white', command=countdown)
    button2.place(x=350,y=400,width=243,height=65)

    button3.config(state='disabled',bg="#000000",fg='black')
    button4.config(state='disabled',bg="#000000",fg='black')

menubar = Menu(alarm_clock)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Alarm", command = waktu)
filemenu.add_command(label="Date & Clock", command = kalendar)
filemenu.add_command(label="Stopwatch", command = stopwatch)
filemenu.add_command(label="Timer", command = timer)
filemenu.add_separator()
filemenu.add_command(label="Exit", command = alarm_clock.quit)
menubar.add_cascade(label="File", menu=filemenu)
alarm_clock.config(menu=menubar)

label1=Label(alarm_clock, text="Welcome To Alarm Clock",font=("ds-digital",20,"bold"),bg="#04052E",fg='white')
label1.pack()

photo = PhotoImage(file = r"D:\M. Fijar S K\Matkul Semester 5\Pemrograman Lanjut\Source Code\Projek-removebg-preview.png")

label2=Label(alarm_clock, text="", image=photo, bg="#000000")
label2.pack()

entri1=Entry(alarm_clock)
entri2=Entry(alarm_clock)
entri3=Entry(alarm_clock)

button1=Button(alarm_clock, text="")
button2=Button(alarm_clock, text="")
button3=Button(alarm_clock, text="")
button4=Button(alarm_clock, text="")

alarm_clock.mainloop()