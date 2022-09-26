from  tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import os
import shutil

#functions
def select_path():
    #picks file path
    path = filedialog.askdirectory()
    path_label.config(text = path)
    
def download_file1():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading . . . ")
    #Download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download Complete! Wanna download something else?")
        
def download_file2():
     get_link = link_field.get()
     user_path = path_label.cget("text")
     screen.title("Downloading . . . ")
     yt = YouTube(get_link)
     video = yt.streams.filter(only_audio=True).first()
     out_file = video.download(output_path=user_path)
     screen.title("Download Complete! Wanna download something else?")
     

screen = Tk()
title = screen.title("Youtube Downloader")
canvas = Canvas(screen, width = 500, height = 500)
canvas.pack()

#image logo
logo_img = PhotoImage(file = 'YTLogo_old_new_animation.gif')
#resize
logo_img = logo_img.subsample(2, 2)

canvas.create_image(250, 80, image = logo_img)

#link field
link_field = Entry(screen, width = 50)
link_label = Label(screen, text = "Enter video link: ", font = ('Arial, 15'))

#Select path for saving the file
path_label = Label(screen, text = "Select file download path", font = ('Arial, 18'))
select_button = Button(screen, text = "Select", font = ('Arial, 12'), command = select_path)

#Download buttons
download_button1 = Button(screen, text = "Download MP4", font = ('Arial, 15'), command = download_file1)
download_button2 = Button(screen, text = "Download MP3", font = ('Arial, 15'), command = download_file2)

#Add widgets to window
canvas.create_window(250, 170, window = link_label)
canvas.create_window(250, 220, window = link_field)
canvas.create_window(250, 330, window = path_label)
canvas.create_window(250, 360, window = select_button)
canvas.create_window(250, 420, window = download_button1)
canvas.create_window(250, 460, window = download_button2)

screen.mainloop()