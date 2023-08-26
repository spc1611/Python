from tkinter import *               # * : all

root = Tk()
root. title("CINDY GUI SAMPLE")
root.geometry("640x480")            # size of program
root.resizable(TRUE, FALSE)         # Is it resizable on its width, height?

# Function
def clicked() :
    btn1.config(text="clicked")
    label.config(text="clicked!!")

# Button
btn1 = Button(root, text="button1", command=clicked)     # (position of button (inside root), how it will be named)
#btn1.pack(side="left")          //position              # position of button on screen
btn1.pack()

# Frame 
frame1 = Frame(root, relief="solid", bd=1)
frame1.pack(fill="both")

# Label (of the button)
label = Label(frame1, text="Hello")
label.pack()

def Txt2Label() :
    change = txt.get("1.0", END)                          # memorize "get"
    label.config(text=change)
    txt.delete("1.0", END)                                # "1.0", END --> means from start to end

#Text
txt = Text(frame1, width=30, height=10)
txt.pack(fill="both")                                     # fill : x, y, both // x : left to right, y: top to bottom

btn2 = Button(frame1, fg='red', text="Textbox to Label", command=Txt2Label)         # Def always on top bc it is function
btn2.pack(side="right")

# Frame 
frame2 = Frame(root, relief="solid", bd=1)
frame2.pack(fill="both")

# Radio Button
selected = IntVar()
radio1 = Radiobutton(frame2, text="1", value=1, variable=selected, padx=5, pady=5)
radio2 = Radiobutton(frame2, text="2", value=2, variable=selected, padx=5, pady=5)
radio3 = Radiobutton(frame2, text="3", value=3, variable=selected, padx=5, pady=5)
radio4 = Radiobutton(frame2, text="4", value=4, variable=selected, padx=5, pady=5)
radio5 = Radiobutton(frame2, text="5", value=5, variable=selected, padx=5, pady=5)

radio1.grid(row=1, column=1, sticky="w")                   # Maybe we don't need sticky="w" or sticky="ew"? Maybe for columnspan=2, we need the ew?
radio2.grid(row=1, column=2, sticky="w")
radio3.grid(row=2, column=1, sticky="w")
radio4.grid(row=2, column=2, sticky="w")
radio5.grid(row=3, columnspan=2, sticky="ew")

def test():
    print(selected.get())

btn3 = Button(frame2, text="Radio Test", command=test)
btn3.grid()


root.mainloop()

#source ./sohyun/bin/activate
