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
'''crf_value = input("Enter CRF value (default is 28): ")
if not crf_value:
    crf_value = "28"'''

# Get the new file name, mkv preffered
output_file = filedialog.asksaveasfilename(defaultextension='.mkv')

# Specify the output file name - modified because
# the output_file will be saved in script's directory
#output_file = "output.mp4"

# Construct the ffmpeg command
#command = f"ffmpeg -i {input_file} -vcodec libx264 -crf {crf_value} {output_file}"

command = f"ffmpeg -i {input_file} -vcodec libx264 -crf 28 {output_file}"

# Execute the ffmpeg command
subprocess.call(command, shell=True)
