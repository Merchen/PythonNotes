# -*- coding: utf-8 -*-
""""""

"""
GUI发布exe

pip install pyinstaller

pyinstaller yourprogram.py

可选参数，-w 屏蔽命令行窗口、-F 打包成一个文件
pyinstaller -F -w yourprogram.py
"""


from Tkinter import *
import ScrolledText

def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())

def save():
    with open(filename.get(),'w') as file:
        file.write(contents.get('1.0', END))

top = Tk()

top.title('Simple Editor')

# contents = ScrolledText()

contents = ScrolledText.ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

Button(text='Open',command=load).pack(side=LEFT)
Button(text='Save',command=save).pack(side=LEFT)

mainloop()

