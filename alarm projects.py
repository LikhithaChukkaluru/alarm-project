import datetime
from playsound import playsound
from tkinter import*
from tkinter.ttk import Combobox
from tkinter.messagebox import*

root=Tk()
def alarm():
    hour=int(c.get())
    minute=int(c1.get())
    # p=c2.get()
    showinfo("Alarm Notification","Alaram has been set")
    print(hour,":",minute)
    print(datetime.datetime.now())
    while True:
        if hour==datetime.datetime.now().hour and minute==datetime.datetime.now().minute :
            print("its wake up time",hour,":",minute)
            playsound("/home/sreekanya/Downloads/swapna pandu")
            break
            



root.title("MY ALARM CLOCK")
l1=Label(root,text="set alarm hour")
l1.grid(row=0,column=0)
hour=list(range(1,24))
c=Combobox(root,values=hour)
c.grid(row=0,column=1)

l2=Label(root,text="set alarm minits")
l2.grid(row=1,column=0)
minit=list(range(1,61))
c1=Combobox(root,values=minit)
c1.grid(row=1,column=1)


l3 =Label(root,text="set time period")
l3.grid(row=2,column=0)
period=["am","pm"]
c2=Combobox(root,values=period)
c2.grid(row=2,column=1)

btn=Button(root,text="Set Alarm",command=alarm)
btn.grid(row=4,columnspan=2)
root.mainloop()


