from pytube import *
from tkinter.filedialog import *
from tkinter import messagebox
from PIL import ImageTk, Image

file_size: int = 0


# Download Function
def start_download():
    global file_size
    try:
        url = urlField.get()
        # change Button State
        btn.config(state=DISABLED)
        btn.config(text='Downloading...')
        path_to_save = askdirectory()
        if path_to_save is None:
            response = messagebox.askyesno("Message", "Do you want to quit")
            if response == 1:
                exit()
        ob = YouTube(url)
        strm = ob.streams.first()
        print(strm)
        print(strm.title)
        print(strm.filesize)
        strm.download(path_to_save)
        print('Done')
        btn.config(state=NORMAL)
        btn.config(text='Start Download')
    except Exception as e:
        print(e)
        print("Error in Downloading")


# GUI Building

main = Tk()
main.title("YouTube Downloader")
main.iconbitmap('venv//Images//icon.ico')
main.geometry("750x300+400+150")
main.resizable(width=True, height=True)

img = Image.open("download.jpg")
img = img.resize((50, 50), Image.ANTIALIAS)
img = ImageTk.PhotoImage(Image.open("download.jpg"))

panel = Label(main, image=img)
panel.pack(side=TOP)

urlField = Entry(main)
urlField.pack(side=TOP, fill=X, padx=20)

btn = Button(main, text='Start Download', relief='ridge', command=start_download)
btn.pack()


main.mainloop()
