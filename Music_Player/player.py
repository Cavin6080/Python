import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#Creating a window for player
music_player = tkr.Tk()

#Title of the window
music_player.title("Music player")

#Setting up the dimensions of the window
music_player.geometry('450x350')

#For choosing your music directory
directory = askdirectory()

#Setting that directory to default directory
os.chdir(directory)

#os.listdir will give the list of the entries given in that directory
songlist = os.listdir()
playlist = tkr.Listbox(music_player, font = 'Cambria 14 bold', bg = 'cyan2', selectmode = tkr.SINGLE)


#Getting the songs in playlist
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

#Play button function
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

#Creating the buttons
Button_Play = tkr.Button(music_player, height = 3, width = 5, text = 'Play Music', font = 'Cambia 14 bold', command = play, bg = 'lime green', fg = 'black')
Button_Stop = tkr.Button(music_player, height = 3, width = 5, text = 'Stop Music', font = 'Cambia 14 bold', command = stop, bg = 'red', fg = 'black')
Button_Pause = tkr.Button(music_player, height = 3, width = 5, text = 'Pause Music', font = 'Cambia 14 bold', command = pause, bg = 'yellow', fg = 'black')
Button_Resume = tkr.Button(music_player, height = 3, width = 5, text = 'Resume Music', font = 'Cambia 14 bold', command = resume, bg = 'pink', fg = 'black')

#to show the button
Button_Play.pack(fill = 'x')
Button_Stop.pack(fill = 'x')
Button_Pause.pack(fill = 'x')
Button_Resume.pack(fill = 'x')

playlist.pack(fill = 'both', expand = 'yes')

var = tkr.StringVar()
songTitile = tkr.Label(music_player, font = 'Cambria 12 bold', textvariable = var)
songTitile.pack()

music_player.mainloop()