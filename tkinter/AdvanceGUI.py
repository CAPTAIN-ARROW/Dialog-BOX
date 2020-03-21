try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import os

mainwindow = tkinter.Tk()

mainwindow.title("Grid Demo")
mainwindow.geometry('640x480-8-200')
mainwindow['padx']=10

label= tkinter.Label(mainwindow, text= "Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

mainwindow.columnconfigure(0, weight=1)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=3)
mainwindow.columnconfigure(3, weight=3)
mainwindow.columnconfigure(4, weight=3)
mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=10)
mainwindow.rowconfigure(2, weight=1)
mainwindow.rowconfigure(3, weight=3)
mainwindow.rowconfigure(4, weight=3)

filelist = tkinter.Listbox(mainwindow)
filelist.grid(row=1, column=0, sticky='nsew', rowspan=2)
filelist.config(border=2, relief='sunken')
for zone in os.listdir('/Windows/System32'):
    filelist.insert(tkinter.END, zone)

listscroll = tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command=filelist.yview)
listscroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
filelist['yscrollcommand'] = listscroll.set

#frame for the radio buttons
optionframe = tkinter.LabelFrame(mainwindow, text="File Details")
optionframe.grid(row=1, column=3, sticky='ne')

RBvalue = tkinter.IntVar()
RBvalue.set(2)
#radio buttons
radio1 = tkinter.Radiobutton(optionframe,text="Filename", value=1, variable= RBvalue)
radio2 = tkinter.Radiobutton(optionframe,text="Path", value=1, variable= RBvalue)
radio3 = tkinter.Radiobutton(optionframe,text="Timestamp", value=1, variable= RBvalue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

#widget to display result
resultlabel= tkinter.Label(mainwindow, text="Result")
resultlabel.grid(row= 2, column=2,sticky='sw')
result= tkinter.Entry(mainwindow)
result.grid(row=2, column=2, sticky='new')

#frame for time spinners
timeframe=tkinter.LabelFrame(mainwindow,text="Time")
timeframe.grid(row=3, column= 0, sticky='new')
#Time Spinners
hourspinner= tkinter.Spinbox(timeframe, width=2, values=tuple(range(0,24)))
minutespinner= tkinter.Spinbox(timeframe, width=2, values=tuple(range(0,60)))
secondspinner= tkinter.Spinbox(timeframe, width=2, values=tuple(range(0,60)))
hourspinner.grid(row=0,column=0)
tkinter.Label(timeframe, text=':').grid(row= 0, column=1)
minutespinner.grid(row=0,column=2)
tkinter.Label(timeframe, text=':').grid(row= 0, column=1)
secondspinner.grid(row=0,column=3)
timeframe['padx']= 36

#frame for the Date spinners
dateframe = tkinter.Frame(mainwindow)
dateframe.grid(row=4,column= 0, sticky='new')
#date labels
daylabel= tkinter.Label(dateframe, text="Day")
monthlabel= tkinter.Label(dateframe, text="Month")
yearlabel= tkinter.Label(dateframe, text="Year")
daylabel.grid(row=0,column=0,sticky='w')
monthlabel.grid(row=0,column=0,sticky='w')
yearlabel.grid(row=0,column=0,sticky='w')
#date spinners
dayspin=tkinter.Spinbox(dateframe,width =5, values=tuple(range(0,32)))
monthspin=tkinter.Spinbox(dateframe,width =5, values=tuple(range(0,13)))
yearspin=tkinter.Spinbox(dateframe,width =5, values=tuple(range(2000,2999)))
dayspin.grid(row=1,column=0)
monthspin.grid(row=1,column=1)
yearspin.grid(row=1,column=2)
#frame for ok and cancel
okbutton= tkinter.Button(mainwindow, text="OK")
cancelbutton= tkinter.Button(mainwindow, text="CANCEL", command=mainwindow.destroy)
okbutton.grid(row=4,column=3,sticky='e')
cancelbutton.grid(row=4, column=4 , sticky='w')

mainwindow.mainloop()
print(RBvalue.get())
