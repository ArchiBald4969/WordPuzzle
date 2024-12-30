import tkinter as tk
import random
def start():
    global sentence
    global cipher
    global length
    global category
    symbols="!£$%^&*<>,.@:;[{]}()-=+#~?"
    symbolsindex=["",]*26
    phrases=[]
    fh=open('list.txt','r')
    for line in fh:
        phrases.append(line.strip())
    category=phrases[0]
    sentence=phrases[random.randint(1,len(phrases)-1)]
    sentence=sentence.upper()
    length=0
    cipher=[]
    for i in symbols:
        while True:
            r=random.randint(0,25)
            if symbolsindex[r]=="":
                symbolsindex[r]=i
                break
    #print(symbolsindex)
    for i in sentence:
        length=length+1
        if not i.isalpha():
            if i==" ":
                correct.append(" ")
                cipher.append([" "," ",tk.Label(root,text=" "),False])
            pass
        else:
            cipher.append([i,symbolsindex[sentence.index(i)],tk.Entry(root,width=5),False])
def checkpuzz():
    for i in range(0,len(cipher)):
        if cipher[i][0]!=" ":
            if cipher[i][2].get!="":
                if cipher[i][0]==cipher[i][2].get().upper()and cipher[i][3]==False:
                    cipher[i][2].config(disabledbackground="lime",state='disabled')
                    correct.append(cipher[i][0])
                    cipher[i][3]=True
                    if len(correct)==length:
                        win()
def window(first):
    global root
    root=tk.Tk()
    root.title('Coded Word Challenge')
    root.attributes('-fullscreen','True')
    if first==True:
        first=False
        start()
    cg=tk.StringVar()
    cg.set(category)
    cat=tk.Label(root,textvariable=cg,font=('comic sans',20))
    cat.grid(row=0,column=1,padx=20,columnspan=20)
    q=tk.Button(root,text="Quit",command=quit)
    q.grid(row=0,column=0)
    check=tk.Button(root,text="Check puzzle",command=checkpuzz)
    check.grid(row=4,column=0,pady=20)
    x=0
    for i in range(0,len(cipher)):
        txt=tk.StringVar()
        txt.set(cipher[i][1])
        cipher[i][2].grid(row=2,column=x,padx=10,pady=20)
        symbol=tk.Label(root,textvariable=txt).grid(row=3,column=x)
        x=x+1
    root.mainloop()
def win():
    root.destroy()
    winscr=tk.Tk()
    winscr.title("Congratulations!")
    winscr.attributes('-fullscreen','True')
    f1=('comic sans',100)
    answer=tk.StringVar()
    answer.set(sentence)
    cong=tk.Label(winscr, text="Congratulations!",font=f1)
    cong.grid(row=0,column=5,columnspan=10)
    cong.config(foreground='lime')
    ans=tk.Label(winscr, textvariable=answer)
    ans.grid(row=1,column=5,columnspan=10)
    qt=tk.Button(winscr,text='Quit',command=quit)
    qt.grid(row=2,column=5)
    winscr.mainloop()

    
first=True
correct=[]
window(first)
