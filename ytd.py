import tkinter as tk
import os
import youtube_dl
import tkinter.font as tkfont


root = tk.Tk()
root.title("Youtube Downloader")
root.geometry("400x400")
root.resizable(width=True,height=True)
canvas1 = tk.Canvas(root,height = 400,width = 400,bg = "black")
canvas1.pack()
bold_font = tkfont.Font(family = "Helvetica",size = 12,weight = "bold")
label1 =tk.Label(root,text= "Enter URL",width=10,bg="white")
label1.config(font=bold_font)
canvas1.create_window(200,100,window = label1)
#text area
download_entry = tk.Entry(root)
canvas1.create_window(200,140,window = download_entry)
#video downloading func
def get_video_url():
    search_item = download_entry.get()
    ydl_opts = {'format':'best',
                'noplaylist':True,
                'extract-audio':True,}
    os.chdir('D:')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_item])


download = tk.Button(text = 'Download',padx = 5,pady= 5,fg = "white",bg='blue',command=get_video_url)
canvas1.create_window(200,230,window = download)
root.mainloop()
