from tkinter import*
import tkinter.ttk as ttk
import os 
from tkinter import filedialog
from PIL import Image
import tkinter.messagebox as msgbox

root =Tk()
root.title('[Sohyun] GIF MAKER')
root.geometry()

path = os.path.dirname(__file__)

btn_frame = Frame(root)
btn_frame.pack(padx=5, pady=5, fill='x')

def addFile() :
    files = filedialog.askopenfilenames(title="Select Images",              # Ask directory = open folder
                                        filetypes = (("JPG File", "*.jpg"), ("All Files", "*.*")),        # *.* = "anything"."anything"
                                        initialdir=path)
    for file in files: 
        img_list.insert(END, file)          # Brings files to the bottom not top

btn_add = Button(btn_frame, text='Add Files', command=addFile)
btn_add.pack(padx=5, pady=5, side='left')

def delFile() :
    for index in reversed(img_list.curselection()):         # Reversed = to keep the files at the same order
        img_list.delete(index)

btn_del = Button(btn_frame, text='Del Files', command=delFile)
btn_del.pack(padx=5, pady=5, side='right')

# List Frame 
list_frame = Frame(root)
list_frame.pack(padx=5, pady=5, fill='both')            #  Fill both means fill both x and y axes fully

# Scroll Bar
scr = Scrollbar(list_frame)
scr.pack(padx=5, pady=5, side='right', fill='y')

img_list = Listbox(list_frame, selectmode='extension', height=15, yscrollcommand=scr.set)      # "extension" = multiselect, "heigh=15" means it can fit 15 files till scroll needed
img_list.pack(pady=5, fill='both', expand=True, side="left")
scr.config(command=img_list.yview)

# Save Path
path_frame = LabelFrame(root, text='Save As...')
path_frame.pack(padx=5, pady=5, fill='x')

folder_path = path

path_label = Label(path_frame, text=folder_path)
path_label.pack(padx=5, pady=5, side='left')

# word_word = (usually) variable name 
# wordWordWord = fucntion name : Camel Case

def pathBrowser() :
    global folder_path
    folder_path = filedialog.askdirectory(initialdir=folder_path)
    if folder_path == "":
        return
    path_label.config(text=folder_path)


path_btn = Button(path_frame, text="Browse...", command=pathBrowser) 
path_btn.pack(padx=5, pady=5, side='right')

# Option Frame
opt_frame = LabelFrame(root, text="Options")
opt_frame.pack(padx=5, pady=5, fill='x')

# Width
label_width = Label(opt_frame, text="Width")
label_width.grid(row='1', column='1')

selected_width = ["Original", "1024", "640"]
cmb_width = ttk.Combobox(opt_frame, state="readonly", values = selected_width, width=10)
cmb_width.current(0)                    # put in "original" in box first
cmb_width.grid(row='1', column='2')

# Duration
label_duration = Label(opt_frame, text="Duration (ms)")
label_duration.grid(row='1', column='3')

e_duration = Entry(opt_frame, width=10)            # "entry" = one line 
e_duration.grid(row='1', column='4')

# File name
label_fname = Label(opt_frame, text="File Name")
label_fname.grid(row='1', column='5')

e_file_name = Entry(opt_frame, width=10) 
e_file_name.grid(row='1', column='6')

pro_frame = LabelFrame(root, text="Progress Bar")
pro_frame.pack(padx=5, pady=5, fill='x')

pro_var = DoubleVar()
progress_bar = ttk.Progressbar(pro_frame, maximum = 100, variable=pro_var)
progress_bar.pack(padx=5, pady=5, fill='x')

#  Button at the bottom
bottom_frame = Frame(root)
bottom_frame.pack(padx=5, pady=5, fill='x')

btn_close = Button(bottom_frame, text='Close', command=root.quit)
btn_close.pack(padx=5, pady=5, side='right')

def run():
    # 1. Get Image from Listbox as Files 
    images = [Image.open(file_path) for file_path in img_list .get(0, END)]

    # 2. Get maxes of width, hieght for canvas
    image_size = []
    img_width = cmb_width.get()

    if img_width == "Original":
        img_width = -1
    else:
        img_width = int(img_width)

    if img_width < 0:
        image_size = [(image.size[0], image.size[1]) for image in images]
    else :
        image_size = [(int(img_width), int(img_width * image.size[1] / image.size[0])) for image in images]

    widths, heights = zip(*(image_size))
    max_width, max_height = max(widths), max(heights)
    
    # 3. Make GIF files
    result_img = []

    for idx, img in enumerate(images):          # idx + images
        # resizing - Option (width)
        if img_width != "Original":
            img = img.resize(image_size[idx])

            img_w, img_h = img.size

            result_img.append(Image.new("RGB", (max_width, max_height), (0,0,0)))       # (0, 0, 0) = (R, G, B) = Black background
            result_img_w, result_img_h = result_img[0].size

            offset = ((result_img_w - img_w) // 2, (result_img_h - img_h) // 2)         # offest --> to move images to the middle
            result_img[idx]. paste(img, offset)

    gif = result_img[0]
    duration = int(e_duration.get())

    file_name = e_file_name.get()

    gif.save(f'{file_name}.gif', save_all = True, append_images = result_img[1:], loop = 0xff, duration = duration)
    msgbox.showinfo("Notice", "DONE!")

def startMake() :
    #List - error check
    if img_list.size() == 0:
        msgbox.showwarning("Warning", "Add images Files")
        return

    #Duration - error check 
    if e_duration.get() == "":
        msgbox.showwarning("Warning", "Input Duration Value")
        return
    
    # File Name - error check 
    if e_file_name.get() == "":
        msgbox.showwarning("Warning", "Input File Name")
        return

    # Run
    run()
    
    print("OKAY")

btn_start = Button(bottom_frame, text='Start', command=startMake)
btn_start.pack(padx=5, pady=5, side='right')


root.mainloop()