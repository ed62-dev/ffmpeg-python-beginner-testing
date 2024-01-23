#https://www.youtube.com/watch?v=0tM-l_ZsxjU
#pip install ttkbootstrap

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import chardet
from tkinter import messagebox

root = tb.Window(themename="superhero")
#root=Tk()
root.title("FFMPEG TTK Bootstrap")
root.geometry('300x350')


def ffmpegcrf():
    if varcrf.get()==1:
        label.config(text="crf")

def ffmpegsubsrt():
    if varsubsrt.get()==1:
        # Use the file dialog to select the SRT file
        srt_file_path = askopenfilename(filetypes=[('SRT Files', '*.srt *.sub')])
       # messagebox.showinfo(title="Am deschis fisierul", message=srt_file_path)
# Detect the encoding of the file
    with open(srt_file_path, 'rb') as file:
        raw_data = file.read()
        encoding = chardet.detect(raw_data)['encoding']
       # messagebox.showinfo(title="tip", message="fisierul e "+encoding)
       

def ffmpegmovsub():
	pass



#title
label = tb.Label(text="FFMPEG",font=("Helvetica,20"),bootstyle="default")
label.pack(pady=5)

#checkboxes
varcrf=IntVar() 
crf=tb.Checkbutton(text="CRF", 
                   variable=varcrf,
                   onvalue=1,
                   offvalue=0)
crf.pack(pady=15)

varsubsrt=IntVar()
subsrt=tb.Checkbutton(text="SUB/SRT", 
                   variable=varsubsrt,
                   onvalue=1,
                   offvalue=0)
subsrt.pack(pady=15)

movsub=IntVar() 
movsub=tb.Checkbutton(text="MOVIE+SUBTITLE", 
                   variable=movsub,
                   onvalue=1,
                   offvalue=0)
movsub.pack(pady=15)


#Define the function for btn:
def btn_clicked():
    if varcrf.get()==1:
        ffmpegcrf()
    if varsubsrt.get()==1:
        ffmpegsubsrt()
    if movsub.get()==1:
        ffmpegmovsub()        
''' if srt_sub_checkbox.instate(['selected']):
        srt_sub_checked()
    if movie_srt_checkbox.instate(['selected']):
        movie_srt_checked()
    messagebox.showinfo("OK", "Tasks completed successfully!")'''


#button
btn=tb.Button(text="Let's go!",
              bootstyle="danger, outline",
              command=btn_clicked)
btn.pack(pady=15)

root.mainloop()
