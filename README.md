# ffmpeg-python-beginner-testing
tests for using ffmpeg and python commands

as a beginner, i try to make some applications

for the moment, i just try to make an application
with an interface for some ffmpeg commands,
personal use

Resource:
Python Tkinter GUI Design Using ttkbootstrap - Complete Course
https://youtu.be/0tM-l_ZsxjU

python3 -m pip install ttkbootstrap
https://ttkbootstrap.readthedocs.io/en/latest/

GUI with 
* 1 spinbox and a checkbox for CRF, if checked, run FFMPEG command to rewrite movie CRF to crf_value
    ffmpeg -i {input_file} -vcodec libx264 -crf {crf_value} {output_file}
* 2 checkboxes
     1. SRT/SUB, if checked run diacritics removal commands in Python
    see srtsubNoDiac-encod.py file
     2. MOVIE+SRT, if checked run FFMPEG command to add subtitle to movie (not burn)
     maybe one of these commands
        - ffmpeg -i in.mp4 -i in.srt -c copy -disposition:s:0 default out.mkv
        - ffmpeg -i myMovie.mkv -vcodec copy -acodec copy -map 0:v:0 -map 0:a:1 -map 0:s:1 -c:s mov_text -metadata:s:s:0 language=rum test.mp4

* and an OK button.

On click OK, depending checkboxes checked, app will run different Python commands
- If CRF checked, app will open a window to choose the movie and remind moviePath and movieName, run ffmpeg and save new movie with movieName=movieName+CRF
- If SRT/SUB checked, app will open a window to choose the srt/sub file, remind srtName/subName, replace characters and save srt file as srtName=srtName+ok in same folder (for ass files, convert to srt)
- If MOVIE+SRT checked, get the movieName and add subtitle file to the movie and save as movieName+ok


Possible variables
1. moviePath
2. movieName
-   srtPath - same as moviePath
3. srtName
4. srtEncod

... but there are many other factors:
    - movie format - ex. vob
    - sometimes must remove all subtitles, then add subtitle...
