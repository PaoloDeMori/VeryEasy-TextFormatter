import tkinter as tkt
from tkinter import messagebox
import textFixer as tF
import sys

color = "snow3"
size = "1400x650"
standardPadding = 15
standardFont= ("arial",10) 
global isSpecialDeleterOn
global isFLSpaceDeleterOn
global isSpaceDeleterOn

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
   textField2.insert(1.0,tF.textFixer(stringa,chars1,isSpaceDeleterOn.get(),isFLSpaceDeleterOn.get(),isSpaceDeleterOn.get()))

def copyText():
    global root
    global textField2
    root.clipboard_clear()
    st=textField2.get(1.0, tkt.END)
    if st[-1]=='\n':
        st=st[:-1]
    root.clipboard_append(st)

def onClosing(event=None):
    global root
    try:
        root.destroy()
    except:
        sys.exit(0)
    sys.exit(0)


def mainWindowBuilder(specialChars):
    global root
    mainWindow = tkt.Frame(root)
    root.resizable(False,False)
    mainWindow.config(bg=color)
    global isSpaceDeleterOn
    isSpaceDeleterOn=tkt.BooleanVar()
    global isFLSpaceDeleterOn
    isFLSpaceDeleterOn=tkt.BooleanVar()
    global isSpecialDeleterOn
    isSpecialDeleterOn=tkt.BooleanVar()
    mainWindow.grid(row=0,column=1,sticky="ns",padx=standardPadding,pady=standardPadding)
    titleLabel=tkt.Label(mainWindow, text=title, font=("Arial",20))
    titleLabel.pack(pady=25)
    optionFrame=tkt.Frame(mainWindow)
    optionFrame.config(bg=color)
    optionFrame.pack(pady=25)

    labelOption1 = tkt.Label(optionFrame, text="Caratteri Considerati Speciali")
    labelOption1.grid(row=0, column=0,padx=standardPadding,pady=standardPadding)
    global labelOption2
    labelOption2 = tkt.Label(optionFrame, text=specialChars,font=("arial",19))
    labelOption2.grid(row=0, column=1,padx=standardPadding,pady=standardPadding)

    global entryOption1
    entryOption1 = tkt.Entry(optionFrame,font=("arial",12))
    entryOption1.grid(row=1,column=0,padx=standardPadding,pady=standardPadding)
    entryButton1 = tkt.Button(optionFrame,text="Aggiungi Un Carattere Speciale", command=modifyChars)
    entryButton1.grid(row=1,column=1,padx=standardPadding,pady=standardPadding)


    textsFrame=tkt.Frame(mainWindow)
    textsFrame.config(bg=color)
    textsFrame.pack(pady=25)
    label1 = tkt.Label(textsFrame, text="Inserisci Qui Il testo Da Modificare",font=standardFont)
    label1.grid(row=0, column=1,padx=standardPadding,pady=standardPadding)
    label1 = tkt.Label(textsFrame, text="Testo modificato",font=standardFont)
    label1.grid(row=0, column=3,padx=standardPadding,pady=standardPadding)

    global textField1
    textField1 = tkt.Text(textsFrame,font=standardFont, height=standardPadding, width=50)
    scrollbar1 = tkt.Scrollbar(textsFrame,orient="vertical", command=textField1.yview)
    textField1.config(yscrollcommand=scrollbar1.set)
    scrollbar1.grid(row=1, column=0, sticky="ns")
    textField1.grid(row=1, column=1,padx=(standardPadding,0),pady=standardPadding)

    entryButton2 = tkt.Button(textsFrame,text="-->", command=modifyText,font=standardFont)
    entryButton2.grid(row=1,column=2,padx=standardPadding)

    global textField2
    textField2 = tkt.Text(textsFrame,font=standardFont, height=standardPadding, width=50)
    scrollbar2 = tkt.Scrollbar(textsFrame,orient="vertical", command=textField2.yview)
    textField2.config(yscrollcommand=scrollbar2.set)
    textField2.grid(row=1, column=3,padx=(0,standardPadding),pady=standardPadding)
    scrollbar2.grid(row=1, column=4, sticky="ns")

    entryButton3 = tkt.Button(textsFrame,text="Copia", command=copyText,font=standardFont)
    entryButton3.grid(row=1,column=5,padx=standardPadding)

def checkBoxCreator():
    checkBoxFrame=tkt.Frame(root)
    checkBox1=tkt.Checkbutton(checkBoxFrame,text="Attivare l'eliminazione dei doppi spazi?",variable=isSpaceDeleterOn,onvalue=True,offvalue=False)
    checkBox1.pack(anchor="w")
    checkBox2=tkt.Checkbutton(checkBoxFrame,text="Attivare l'eliminazione degli spazi iniziali o finali",variable=isFLSpaceDeleterOn,onvalue=True,offvalue=False)
    checkBox2.pack(anchor="w")
    checkBox3=tkt.Checkbutton(checkBoxFrame,text="Attivare l'eliminazione dei caratteri speciali?",variable=isSpecialDeleterOn,onvalue=True,offvalue=False)
    checkBox3.pack(anchor="w")
    checkBoxFrame.grid(row=0,column=0,sticky="ns",padx=standardPadding,pady=standardPadding)




def startGui(specialChars):
    global chars1
    chars1=specialChars
    global title
    title = "TextFormatter"
    global root
    root = tkt.Tk()
    root.title(title)
    root.config(bg=color)
    root.geometry(size)
    mainWindowBuilder(specialChars)
    checkBoxCreator()
    
    root.protocol("WM_DELETE_WINDOW", onClosing)
    root.mainloop()

