from ttkbootstrap import Style
from tkinter import ttk
from tkinter import *
from configData import read
from tkinter import messagebox
from testMode import trainWindow


style = Style(theme='flatly')
window = style.master
window.title("Review Reader")
s_width,s_height =600,460 #window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (s_width,s_height))
window.resizable(False, False)


def check():
    review = textField.get("1.0","end-1c")

    if review == "Enter the review here" or review=="":
        messagebox.showwarning('warning', 'You need to input a review first')
            
    else:
        predict = read.prediction(review) 
        checkbtn.pack_forget()

        if predict=="POSITIVE":
            global pos
            pos = ttk.Button(result, text='POSITIVE', style='success.TButton',command=clear)
            pos.pack()
            
        else:
            global neg
            neg = ttk.Button(result, text='NEGATIVE', style='danger.TButton',command=clear)
            neg.pack()

        trainbtn.config(text="Not what you expected? Train the module here")
    
def clear():
    try:
        neg.pack_forget()
    except:
        pos.pack_forget()
    checkbtn.pack()
    

big = ttk.Labelframe(window,text="Evaluvate Mode")
big.pack(pady=20,ipadx=10)

entry = ttk.Label(big)
entry.pack(pady=10)

textField=Text(entry,height=15,width=65,font=('Tlwg Typist',10))
textField.pack()
textField.insert(END,"Enter the review here")

result = Label(big)
result.pack(pady=20)
checkbtn = ttk.Button(result,text="Check",command=check)
checkbtn.pack()

train = ttk.Label(big)
train.pack(pady=10)
trainbtn= ttk.Button(train,text="Train Mode", style='secondary.Link.TButton',cursor='hand2',command=lambda:trainWindow(window))
trainbtn.pack()



window.mainloop()
