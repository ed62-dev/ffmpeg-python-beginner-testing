from tkinter import Tk, Button, filedialog
import subprocess

# Function to select a movie and extract subtitles using FFmpeg
def extract_subtitles():
    # Use the file dialog to select the movie file
    movie_path = filedialog.askopenfilename(filetypes=[('Video Files', '*.mp4'), ('All Files', '*.*')])

    # Extract subtitles using FFmpeg
    subprocess.run(['ffmpeg', '-i', movie_path, '-map', '0:s:0', 'subtitles.srt'])

# Function to modify subtitles
def modify_subtitles():
    # Open the subtitles file
    subtitles_path = filedialog.askopenfilename(filetypes=[('Subtitles Files', '*.srt'), ('All Files', '*.*')])

    # Perform modifications on the subtitles file
    # Modify the subtitles as per your requirements

# Function to modify CRF (Constant Rate Factor) using FFmpeg
def modify_crf():
    # Use the file dialog to select the movie file
    movie_path = filedialog.askopenfilename(filetypes=[('Video Files', '*.mp4'), ('All Files', '*.*')])

    # Modify CRF using FFmpeg
    subprocess.run(['ffmpeg', '-i', movie_path, '-c:v', 'libx264', '-crf', '18', 'output.mp4'])

# Function to add subtitles using FFmpeg
def add_subtitles():
    # Use the file dialog to select the movie file
    movie_path = filedialog.askopenfilename(filetypes=[('Video Files', '*.mp4'), ('All Files', '*.*')])

    # Use the file dialog to select the subtitles file
    subtitles_path = filedialog.askopenfilename(filetypes=[('Subtitles Files', '*.srt'), ('All Files', '*.*')])

    # Add subtitles using FFmpeg
    subprocess.run(['ffmpeg', '-i', movie_path, '-vf', f'subtitles={subtitles_path}', 'output.mp4'])

# Create a Tkinter root window
root = Tk()

# Create buttons with names and associated actions/functions
button1 = Button(root, text="Extract Subtitles", command=extract_subtitles)
button1.pack()

button2 = Button(root, text="Modify Subtitles", command=modify_subtitles)
button2.pack()

button3 = Button(root, text="Modify CRF", command=modify_crf)
button3.pack()

button4 = Button(root, text="Add Subtitles", command=add_subtitles)
button4.pack()

# Start the Tkinter event loop
root.mainloop()
