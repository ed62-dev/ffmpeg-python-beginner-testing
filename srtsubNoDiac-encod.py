
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import chardet

from tkinter import messagebox

def replace_characters(srt_file_path, encoding):
    with open(srt_file_path, 'r', encoding=encoding) as file:
        srt_content = file.read()

    # Perform replacements
    #srt_content = srt_content.replace('ș', 's')
    
            # Înlocuiește caracterele
    srt_content = srt_content.replace('º', 's')
    srt_content = srt_content.replace('ș', 's')
    srt_content = srt_content.replace('ş', 's')

    srt_content = srt_content.replace('ª', 'S')
    srt_content = srt_content.replace('Ș', 'S')        
    srt_content = srt_content.replace('Ş', 'S')   
                
    srt_content = srt_content.replace('þ', 't')
    srt_content = srt_content.replace('ț', 't')        
    srt_content = srt_content.replace('ţ', 't')        
        
    srt_content = srt_content.replace('Þ', 'T')
    srt_content = srt_content.replace('Ț', 'T')
    srt_content = srt_content.replace('Ţ', 'T')

    srt_content = srt_content.replace('ã', 'a')
    srt_content = srt_content.replace('ă', 'a')
    srt_content = srt_content.replace('â', 'a')

    srt_content = srt_content.replace('Ã', 'A')
    srt_content = srt_content.replace('Ă', 'A')
    srt_content = srt_content.replace('Â', 'A')

    srt_content = srt_content.replace('Î', 'I')
    srt_content = srt_content.replace('î', 'i')    

    # Get the new file name
    new_file_path = asksaveasfilename(defaultextension='.srt')

    # Save the modified content to the new file
    with open(new_file_path, 'w', encoding=encoding) as file:
        file.write(srt_content)

# Create a Tkinter root window
root = Tk()
root.withdraw()

# Use the file dialog to select the SRT file
srt_file_path = askopenfilename(filetypes=[('SRT Files', '*.srt *.sub')])

messagebox.showinfo(title="Am deschis", message="fisierul"+srt_file_path)


# Detect the encoding of the file
with open(srt_file_path, 'rb') as file:
    raw_data = file.read()
    encoding = chardet.detect(raw_data)['encoding']

# Call the function to replace characters and save the file
replace_characters(srt_file_path, encoding)
