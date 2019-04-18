import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

import fastai
import fastai.vision as vision
import pathlib
from pathlib import Path
import pandas as pd

import numpy as np
# from ttkthemes import ThemedTk
# from tkinter import ttk

def get_model(model_dir):
    path = Path(model_dir)
    empty_data = vision.ImageDataBunch.load_empty(path, fname='stage-5-data.pkl')
    learn = vision.cnn_learner(empty_data, vision.models.densenet121, pretrained=False).load('stage-5')
    return learn

def get_prediction():
    img_name = e.get()
    dt = vision.open_image(img_name)
    predict_class,predict_idx,predict_values = learn.predict(dt)
    predict_class = learn.data.classes # str(predict_class).split(';')
    predict_values = predict_values.tolist()
    diagnoses = zip(predict_class, predict_values)
    l = [len(i) for i in predict_class]
    diagnoses = sorted(diagnoses, key = lambda t: t[1], reverse=True)
    textvar = f"{'Condition'.ljust(max(l))} - Probability"
    for d,p in diagnoses:
        # print(d)
        textvar += '\n' + f'{d.ljust(max(l))} - {round(p*100, 2)}%'
    img_name = pathlib.ntpath.basename(img_name)
    if img_name in labels:
        textvar += '\n\nTrue Labels'
        textvar += '\n' + ','.join(labels[img_name].split('|'))
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
labels = pd.read_csv('sample_labels.csv', index_col='Image Index')['Finding Labels']


window = Tk()
# window = ThemedTk(theme="arc")
# s = ttk.Style(window)
# s.theme_use("alt")

window.title('Chest X-ray classifier')
window.geometry('400x715')
canvas = Canvas(window, width=375,height=375, bd=0,bg='white')
canvas.grid(row=1, column=1, padx=10, pady=10)


e = StringVar()

submit_button = Button(window, text ='Open and Scan', command = show_image)
submit_button.grid(row=2, column=1)

t1=Text(window,bd=0, width=53, height=19, font='Fixdsys -14')
t1.grid(row=3, column=1, padx=10, pady=10)

window.mainloop()