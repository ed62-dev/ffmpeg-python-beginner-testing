import tkinter as tk
from tkinter import filedialog
import subprocess

# Create a Tkinter window
window = tk.Tk()

# Hide the main window
window.withdraw()

# Prompt the user to select a movie file using a dialog window
input_file = filedialog.askopenfilename(title="Select a movie file")

# Show the main window again
window.deiconify()

# Prompt the user to enter the desired CRF value
crf_value = input("Enter CRF value (default is 28): ")
if not crf_value:
    crf_value = "28"

# Specify the output file name
output_file = "output.mp4"

# Construct the ffmpeg command
command = f"ffmpeg -i {input_file} -vcodec libx264 -crf {crf_value} {output_file}"

# Execute the ffmpeg command
subprocess.call(command, shell=True)
