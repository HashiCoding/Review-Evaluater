from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
from configData import trainModule
from tkinter import messagebox

def trainWindow(root):
    new = Toplevel(root)
    new.title('Train Mode')
    s_width,s_height =600,460 
    new.geometry('%dx%d+0+0' % (s_width,s_height))
    new.resizable(False, False)

    big = ttk.Labelframe(new,text="Train Mode")
    big.pack(pady=20,ipadx=10)

    entry = ttk.Label(big)
    entry.pack(pady=10)

    textField=Text(entry,height=15,width=65,font=('Tlwg Typist',10))
    textField.pack()
    textField.insert(END,"Enter the review here")

    result = ttk.Label(big)
    result.pack(pady=10)
    
    options=[
        '',
    'POSITIVE',
    'NEGATIVE',
    ]

    def changed(event):
        global eval
        eval = clicked.get()
        if eval=="POSITIVE":
            drop.config(style='success.TMenubutton')
        else:
            drop.config(style='danger.TMenubutton')

    clicked = StringVar()
    clicked.set(options[1])

    drop = ttk.OptionMenu(result,clicked,*options,command=changed,style='success.TMenubutton')
    drop.pack(pady=1)


    def write():
        review = textField.get("1.0","end-1c")
        if review == "Enter the review here" or review=="":
            messagebox.showwarning('warning', 'You need to input a review first')

        else:
            trainModule.train(review,eval)
            new.destroy()



    done =Label(result)
    done.pack(pady=10)  
    donekbtn = ttk.Button(result,text="Done",command=write)
    donekbtn.pack()
