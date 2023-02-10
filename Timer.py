import tkinter as tk
from tkinter import *
import datetime
import winsound as ws

class Countdown(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left= 0
        self._timer_on=False
        
    def show_widgets(self):
        self.label.pack(pady=20)
        self.entry.pack(pady=8)
        self.start.pack(pady=10)
        self.stop.pack()
        self.reset.pack(pady=10)
        
    def create_widgets(self): 
        ''' this function creates the widgets and includes the styling of each widget '''
        self.label=tk.Label(self, text="Enter the Time(In seconds)",font="arial 13 normal")
        self.entry = tk.Entry(self,justify="center",width=25,)
        self.entry.focus_set()
        self.reset=tk.Button(self,text="Reset Timer", width=13 , font="arial 10 normal",command = self.reset_button)
        self.stop= tk.Button(self,text="Stop Timer", width=13 , font="arial 10 normal", command = self.stop_button)
        self.start= tk.Button(self,text="Start Timer", width=13 , font="arial 10 normal",command = self.start_button)
        
    def countdown(self):
        self.label["text"]= self.convert_seconds_left_to_time()
        
        if self.seconds_left:
            ''' Tests if the time is on and it its on it starts the countdown function'''
            self.seconds_left -= 1
            self._timer_on=self.after(1000,self.countdown)
        else:
            ''' When the timmer finally reaches 0 the alarm sound starts playing '''    
            self._time_on=False
            ws.PlaySound("Alarm Clock Sound",ws.SND_FILENAME)
            
        
    def reset_button(self):
        self.seconds_left=0
        self.stop_timer()
        self._timer_on=False
        self.label["text"]= "Enter the Time(In seconds)"
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack(pady=10)
        self.stop.pack()
        self.reset.pack(pady=10)
        
    def stop_button(self):
        self.seconds_left = int(self.entry.get())
        self.stop_timer()
        
    def start_button(self):
        self.seconds_left=int(self.entry.get())
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack(pady=10)
        self.stop.pack()
        self.reset.pack(pady=10)
        
    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False
            
    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds= self.seconds_left)
    
if __name__=="__main__":
    root=tk.Tk()
    root.title("Countdown Timer")
    root.geometry("400x300")
    root.resizable(False,False,)
    
    Image_icon= PhotoImage(file="img/logo.png")
    root.iconphoto(False,Image_icon)

    
    countdown = Countdown(root)
    countdown.pack()
    
    root.mainloop()
         