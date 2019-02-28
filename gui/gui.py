import tkinter

from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

import fastai
import fastai.vision as vision
from pathlib import Path
# from ttkthemes import ThemedTk

def get_model(model_dir):
    path = Path(model_dir)
    empty_data = vision.ImageDataBunch.load_empty(path)
    learn = vision.create_cnn(empty_data, vision.models.resnet18, pretrained=False).load('model')
    return learn

def get_prediction():
    dt = vision.open_image(e.get())
    predict_class,predict_idx,predict_values = learn.predict(dt)
    textvar = f"The object is a {str(predict_class)}"
    t1.delete(0.0, tkinter.END)
    t1.insert('insert', textvar+'\n')
    t1.update()

def show_image():
    File = askopenfilename(title='Open Image') 
    e.set(File)
    
    load = Image.open(e.get())
    w, h = load.size
    load = load.resize((250, 250))
    print(w, h)
    imgfile = ImageTk.PhotoImage(load )
    
    canvas.image = imgfile  # <--- keep reference of your image
    canvas.create_image(2,2,anchor='nw',image=imgfile)
    get_prediction()

 
learn = get_model('../model_data')


window = Tk()
# window = ThemedTk("arc")
window.title = 'Chest X-ray classifier'
window.geometry('280x350')
canvas = Canvas(window, width=250,height=250, bd=0,bg='white')
canvas.grid(row=1, column=0)


e = StringVar()

submit_button = Button(window, text ='Open', command = show_image)
submit_button.grid(row=2, column=0)

t1=Text(window,bd=0, width=35,height=2,font='Fixdsys -14')
t1.grid(row=3, column=0)

window.mainloop()