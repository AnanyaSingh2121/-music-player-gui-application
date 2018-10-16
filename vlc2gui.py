from tkinter import*
from tkinter import filedialog
#from tkinter import askdirectory 
import os
import pygame

'''def browse():
    
    pathlabel.config(text=filename)'''

#def subFile():
   # filename=filedialog.askopenfilename(filetypes=(("SRT File",".srt")))

vlc=Tk()
vlc.geometry("400x500")
mMenu=Menu(vlc)
vlc.config(menu=mMenu)
vlc.title("vlc player")

listofsongs=[]
index=0

def direcChooser():
   filename=filedialog.askopenfilename(filetypes=(("MP3 File","*.mp3"),("All Files","*.*")))
   # filename=filedialog.askopenfilename(filetypes=(("MP3 File","*.mp3")))
   pygame.mixer.init()
   pygame.mixer.music.load(filename)
   pygame.mixer.music.play() 
    
def musicPlaylist():
    directory=filedialog.askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)
            print(files)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
    listbox=Listbox(vlc)
    listbox.pack(side=LEFT,anchor=N)
    listofsongs.reverse()
    for items in listofsongs:
        listbox.insert(0,items)
    listofsongs.reverse()       

    
def pauseplay():
    pygame.mixer.music.pause()

def play():
   # pygame.mixer.init()
   # pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.unpause()

def prev():
    global index
    index-=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def nexts():
    global index
    index+=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
        
    
p=PhotoImage(file="stop.png")
pausebutton=Button(vlc,image=p,command=pauseplay)
pausebutton.pack(side=LEFT,anchor=S)
#pausebutton.pack(side=LEFT)

playm=PhotoImage(file="playnew.png")
playbutton=Button(vlc,image=playm,command=play)
playbutton.pack(side=LEFT,anchor=S)

previous=PhotoImage(file="prevn.png")
prevbutton=Button(vlc,image=previous,command=prev)
prevbutton.pack(side=LEFT,anchor=S)

Next=PhotoImage(fil='next.png')
nextbutton=Button(vlc,image=Next,command=nexts)
nextbutton.pack(side=LEFT,anchor=S)

def changeVol(event):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(vol.get())



vol = Scale(
    vlc,
    from_ = 0,
    to = 100,
    orient = HORIZONTAL ,
    resolution = .1,
 command=changeVol)
vol.set(.3)
vol.pack(side=RIGHT,anchor=S)    

'''timeline=Scale(vlc, from_=0,to=2,length=400,orient=HORIZONTAL,resolution=.5)
timeline.pack()'''#(side=RIGHT,anchor=S)   

#pygame.quit()  
subMenu=Menu(mMenu)
mMenu.add_cascade(label="Media",menu=subMenu)
subMenu.add_command(label="Open File",command=direcChooser)
#subMenu.add_command(label="playlist",command=musicPlaylist)
'''subMenu.add_command(label="Save",command=fun1)
subMenu.add_command(label="Open...",command=browsefunc) '''                                                   
subMenu.add_separator()
subMenu.add_command(label="Exit",command=quit)


playMenu=Menu(mMenu)
mMenu.add_cascade(label="Playback",menu=playMenu)
playMenu.add_command(label="Jump Forward")#,command=browse)
playMenu.add_command(label="Jump Backward")#,command=browse)
playMenu.add_command(label="Play")#,command=browse)


audioMenu=Menu(mMenu)
mMenu.add_cascade(label="Audio",menu=audioMenu)
audioMenu.add_command(label="Increase Volume")
audioMenu.add_command(label="Decrease Volume")#,command=browse)
audioMenu.add_command(label="Mute")#,command=browse)

videoMenu=Menu(mMenu)
mMenu.add_cascade(label="Video",menu=videoMenu)
videoMenu.add_command(label="Full Screen")#,command=browse)

subtitlesMenu=Menu(mMenu)
mMenu.add_cascade(label="Subtitles",menu=subtitlesMenu)
subtitlesMenu.add_command(label="Add Subtile")#,command=subFlie)

viewMenu=Menu(mMenu)
mMenu.add_cascade(label="View",menu=viewMenu)
viewMenu.add_command(label="Playlist",command=musicPlaylist)
viewMenu.add_command(label="Docked Playlist")#,command=subFlie)



helpMenu=Menu(mMenu)
mMenu.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="Help",)#command=subFlie)
helpMenu.add_command(label="About",)#command=subFlie)

 
vlc.mainloop()






