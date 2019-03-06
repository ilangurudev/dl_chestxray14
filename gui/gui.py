import tkinter

from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

import fastai
import fastai.vision as vision
from pathlib import Path

import numpy as np
# from ttkthemes import ThemedTk

def get_model(model_dir):
    path = Path(model_dir)
    empty_data = vision.ImageDataBunch.load_empty(path)
    learn = vision.create_cnn(empty_data, vision.models.vgg16_bn, pretrained=False).load('stage1')
    return learn

def get_prediction():
    dt = vision.open_image(e.get())
    predict_class,predict_idx,predict_values = learn.predict(dt)
    predict_class = learn.data.classes # str(predict_class).split(';')
    predict_values = predict_values.tolist()
    diagnoses = zip(predict_class, predict_values)
    # print([(i,j) for i,j in diagnoses])
    diagnoses = sorted(diagnoses, key = lambda t: t[1], reverse=True)
    textvar = "The xray shows signs of "
    for d,p in diagnoses:
        print(d)
        textvar += '\n' + f'{d} with probability {p*100}%'
    print(textvar)
    t1.delete(0.0, tkinter.END)
    t1.insert('insert', textvar+'\n')
    t1.update()

def show_image():
    File = askopenfilename(title='Open Image') 
    e.set(File)
    
    load = Image.open(e.get())
    w, h = load.size
    load = load.resize((375, 375))
    # print(w, h)
    imgfile = ImageTk.PhotoImage(load )
    
    canvas.image = imgfile  # <--- keep reference of your image
    canvas.create_image(2,2,anchor='nw',image=imgfile)
    get_prediction()

 
learn = get_model('../model_data')


window = Tk()
# window = ThemedTk("arc")
window.title = 'Chest X-ray classifier'
window.geometry('400x680')
canvas = Canvas(window, width=375,height=375, bd=0,bg='white')
canvas.grid(row=1, column=1, padx=10, pady=10)


e = StringVar()

submit_button = Button(window, text ='Open', command = show_image)
submit_button.grid(row=2, column=1)

t1=Text(window,bd=0, width=53, height=16, font='Fixdsys -14')
t1.grid(row=3, column=1, padx=10, pady=10)

window.mainloop()