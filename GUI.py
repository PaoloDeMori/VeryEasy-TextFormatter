import tkinter as tkt
from tkinter import messagebox
import textFixer as tF
import sys

color = "snow3"

def modifyChars():
    global chars1
    text = entryOption1.get()
    if len(text) > 1:
        messagebox.showerror("Errore","Un solo carattere da aggiungere per volta")
        return
    if text in chars1 :
        messagebox.showerror("Errore","Carattere già presente")
        return
    chars1+=text
    labelOption2.config(text=chars1)
    entryOption1.delete(0,tkt.END)

def modifyText():
   stringa = textField1.get(1.0,tkt.END)
   textField2.delete(1.0,tkt.END)
   textField2.insert(1.0,tF.textFixer(stringa,chars1))

def onClosing(event=None):
    global root
    try:
        root.destroy()
    except:
        sys.exit(0)
    sys.exit(0)



def startGui(specialChars):
    global chars1
    chars1=specialChars
    title = "TextFormatter"
    global root
    root = tkt.Tk()
    root.title(title)
    root.config(bg=color)
    root.geometry("900x900")
    mainWindow = tkt.Frame(root)
    mainWindow.config(bg=color)
    mainWindow.pack()
    titleLabel=tkt.Label(mainWindow, text=title, font=("Arial",20))
    titleLabel.pack(pady=25)
    optionFrame=tkt.Frame(mainWindow)
    optionFrame.config(bg=color)
    optionFrame.pack(pady=25)

    labelOption1 = tkt.Label(optionFrame, text="Caratteri Considerati Speciali")
    labelOption1.grid(row=0, column=0,padx=15,pady=15)
    global labelOption2
    labelOption2 = tkt.Label(optionFrame, text=specialChars,font=("arial",19))
    labelOption2.grid(row=0, column=1,padx=15,pady=15)

    global entryOption1
    entryOption1 = tkt.Entry(optionFrame,font=("arial",12))
    entryOption1.grid(row=1,column=0,padx=15,pady=15)
    entryButton1 = tkt.Button(optionFrame,text="Aggiungi Un Carattere Speciale", command=modifyChars)
    entryButton1.grid(row=1,column=1,padx=15,pady=15)


    textsFrame=tkt.Frame(mainWindow)
    textsFrame.config(bg=color)
    textsFrame.pack(pady=25)
    label1 = tkt.Label(textsFrame, text="Inserisci Qui Il testo Da Modificare",font=("arial",10))
    label1.grid(row=0, column=1,padx=15,pady=15)
    label1 = tkt.Label(textsFrame, text="Testo modificato",font=("arial",10))
    label1.grid(row=0, column=3,padx=15,pady=15)

    global textField1
    textField1 = tkt.Text(textsFrame,font=("arial",10), height=30, width=50)
    scrollbar1 = tkt.Scrollbar(textsFrame,orient="vertical", command=textField1.yview)
    textField1.config(yscrollcommand=scrollbar1.set)
    scrollbar1.grid(row=1, column=0, sticky="ns")
    textField1.grid(row=1, column=1,padx=(15,0),pady=15)

    entryButton2 = tkt.Button(textsFrame,text="-->", command=modifyText,font=("arial",10))
    entryButton2.grid(row=1,column=2,padx=15)

    global textField2
    textField2 = tkt.Text(textsFrame,font=("arial",10), height=30, width=50)
    scrollbar2 = tkt.Scrollbar(textsFrame,orient="vertical", command=textField2.yview)
    textField2.config(yscrollcommand=scrollbar2.set)
    textField2.grid(row=1, column=3,padx=(0,15),pady=15)
    scrollbar2.grid(row=1, column=4, sticky="ns")
    root.protocol("WM_DELETE_WINDOW", onClosing)
    root.mainloop()

