#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jul 30, 2019 01:56:26 AM

import sys
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import music_system_support
from pygame import mixer
import tinytag
import os
from tkinter.filedialog import askdirectory
import tkinter as tk
from tkinter import messagebox
mixer.init()
media_list = []
file_name = ""
index = 0
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    music_system_support.init(root, top)
    root.mainloop()


w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    music_system_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("560x330+432+170")
        top.title("Music Player")
        top.resizable(0,0)
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.index = 0
        self.progress_var = DoubleVar()

        self.menu = Menu(top)
        top.configure(menu=self.menu)
        self.subMenu = Menu(self.menu)
        self.menu.add_cascade(label='File',menu=self.subMenu)
        self.subMenu.add_command(label="Create playList",command=self.askDirectory)
        self.subMenu.add_command(label='show playList',command=self.showPlayList)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit",command=self.exitWindow)
        self.editMenu = Menu(self.menu)
        self.menu.add_cascade(label="Edit",menu=self.editMenu)
        self.editMenu.add_command(label="Add song",command=self.addSongPlaylist)
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Delete song')

        self.backward_btn = Button(top,command=self.backward_song)
        self.backward_btn.place(relx=0.04, rely=0.42, height=34, width=87)
        self.backward_btn.configure(activebackground="#d9d9d9")
        self.backward_btn.configure(activeforeground="#000000")
        self.backward_btn.configure(background="#d9d9d9")
        self.backward_btn.configure(disabledforeground="#a3a3a3")
        self.backward_btn.configure(foreground="#000000")
        self.backward_btn.configure(highlightbackground="#d9d9d9")
        self.backward_btn.configure(highlightcolor="black")
        self._img1 = PhotoImage(file="./backwards.png")
        self.backward_btn.configure(image=self._img1)
        self.backward_btn.configure(pady="0")

        self.play_btn = Button(top,command=self.play_music)
        self.play_btn.place(relx=0.43, rely=0.42, height=34, width=87)
        self.play_btn.configure(activebackground="#d9d9d9")
        self.play_btn.configure(activeforeground="#000000")
        self.play_btn.configure(background="#d9d9d9")
        self.play_btn.configure(disabledforeground="#a3a3a3")
        self.play_btn.configure(foreground="#000000")
        self.play_btn.configure(highlightbackground="#d9d9d9")
        self.play_btn.configure(highlightcolor="black")
        self._img2 = PhotoImage(file="./play.png")
        self.play_btn.configure(image=self._img2)
        self.play_btn.configure(pady="0")

        self.pause_btn = Button(top,command=self.pauseSong)
        self.pause_btn.place(relx=0.61, rely=0.42, height=34, width=87)
        self.pause_btn.configure(activebackground="#d9d9d9")
        self.pause_btn.configure(activeforeground="#000000")
        self.pause_btn.configure(background="#d9d9d9")
        self.pause_btn.configure(disabledforeground="#a3a3a3")
        self.pause_btn.configure(foreground="#000000")
        self.pause_btn.configure(highlightbackground="#d9d9d9")
        self.pause_btn.configure(highlightcolor="black")
        self._img3 = PhotoImage(file="./pause.png")
        self.pause_btn.configure(image=self._img3)
        self.pause_btn.configure(pady="0")

        self.forward_btn = Button(top,command=self.playNextSong)
        self.forward_btn.place(relx=0.79, rely=0.42, height=34, width=87)
        self.forward_btn.configure(activebackground="#d9d9d9")
        self.forward_btn.configure(activeforeground="#000000")
        self.forward_btn.configure(background="#d9d9d9")
        self.forward_btn.configure(disabledforeground="#a3a3a3")
        self.forward_btn.configure(foreground="#000000")
        self.forward_btn.configure(highlightbackground="#d9d9d9")
        self.forward_btn.configure(highlightcolor="black")
        self._img4 = PhotoImage(file="./fowards.png")
        self.forward_btn.configure(image=self._img4)
        self.forward_btn.configure(pady="0")

        self.stop_btn = Button(top,command=self.stop_music)
        self.stop_btn.place(relx=0.22, rely=0.42, height=34, width=97)
        self.stop_btn.configure(activebackground="#d9d9d9")
        self.stop_btn.configure(activeforeground="#000000")
        self.stop_btn.configure(background="#d9d9d9")
        self.stop_btn.configure(disabledforeground="#a3a3a3")
        self.stop_btn.configure(foreground="#000000")
        self.stop_btn.configure(highlightbackground="#d9d9d9")
        self.stop_btn.configure(highlightcolor="black")
        self._img5 = PhotoImage(file="./stop.png")
        self.stop_btn.configure(image=self._img5)
        self.stop_btn.configure(pady="0")

        self.showList = Text(top, wrap=WORD, padx=2, bd=2, selectbackground='red')
        s1 = Scrollbar(self.showList)
        self.showList.place(relx=0.04, rely=0.57, height=150, width=500)
        s1.pack(side=tk.RIGHT, fill=tk.Y)
        self.showList.config(yscrollcommand=s1.set)
        self.showList.configure(background="#d9d9d9")
        self.showList.configure(font=('arial', 10, 'italic'))
        self.showList.configure(foreground="#2446b5")
        self.showList.configure(state='disable')
        self.showList.configure(width=500)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.04, rely=0.09, relheight=0.21, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=515)

        self.update_song_label = Label(self.Frame2,font=('Nexa Rust',13,'italic bold'))
        self.update_song_label.place(relx=0.02, rely=0.22, height=31, width=494)
        self.update_song_label.configure(activebackground="#f9f9f9")
        self.update_song_label.configure(activeforeground="black")
        self.update_song_label.configure(background="#d9d9d9")
        self.update_song_label.configure(disabledforeground="#a3a3a3")
        self.update_song_label.configure(foreground="#000000")
        self.update_song_label.configure(highlightbackground="#d9d9d9")
        self.update_song_label.configure(highlightcolor="black")
        self.update_song_label.configure(text='''song label''')

        # self.progress_song = ttk.Progressbar(self.Frame1, variable=self.progress_var)
        # self.progress_song.place(relx=0.04, rely=0.74, relwidth=0.92, relheight=0.0, height=22)


    def addSongPlaylist(self):
        self.askDirectory()
        self.showPlayList()

    def askDirectory(self):
        dir = askdirectory()
        os.chdir(dir)
        for files in os.listdir(dir):
            if files.endswith(".mp3"):
                media_list.append(files)
        media_list.reverse()
        print(media_list)

    def showPlayList(self):
        if media_list:
            self.showList.configure(state='normal')
            for words in range(len(media_list)):
                self.showList.insert(tk.END, media_list[words])
                self.showList.insert(tk.END, "\n")
            self.showList.configure(state='disable')

        else:
            messagebox.showerror("Error","you don't have any PlayList yet!")

    def play_music(self):
            mixer.music.load(media_list[index])
            mixer.music.play()
            self.updateSongLabel()

    def stop_music(self):
        mixer.music.stop()
        self.update_song_label.configure(text="song label")

    def backward_song(self):
        global index
        index -= 1
        mixer.music.load(media_list[index])
        mixer.music.play()
        self.updateSongLabel()

    def playNextSong(self):
        global  index
        index +=1
        mixer.music.load(media_list[index])
        mixer.music.play()
        self.updateSongLabel()

    def exitWindow(self):
        os._exit(0)


    def pauseSong(self):
        mixer.music.pause()

    def updateSongLabel(self):
        global index
        self.update_song_label.configure(text=media_list[index])

if __name__ == '__main__':
    vp_start_gui()



