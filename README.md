# ffmpeg-python-beginner-testing
tests for using ffmpeg and python commands

as a beginner, i try to make some applications

for the moment, i just try to make an application
with an interface and buttons for some ffmpeg commands,
for personal use

GUI with tkinter 
https://youtu.be/0tM-l_ZsxjU

python3 -m pip install ttkbootstrap
https://ttkbootstrap.readthedocs.io/en/latest/

GUI has 
3 checkboxes
1. CRF28, if checked, run FFMPEG command to rewrite movie to 28 CRF
    ffmpeg -i {input_file} -vcodec libx264 -crf {crf_value} {output_file}
2. SRT/SUB, if checked run diacritics removal commands in Python
    see srtsubNoDiac-encod.py file
3. MOVIE+SRT, if checked run FFMPEG command to add subtitle to movie (not burn)
     maybe one of these
       - ffmpeg -i in.mp4 -i in.srt -c copy -disposition:s:0 default out.mkv
       - ffmpeg -i myMovie.mkv -vcodec copy -acodec copy -map 0:v:0 -map 0:a:1 -map 0:s:1 -c:s mov_text -metadata:s:s:0 language=rum test.mp4
   

and an OK button

8 variables, maybe less - without ?
1. moviePath
2. movieName
3. movieNameCRF ?
4. srtPath
5. srtName
6. srtEncod
7. srtNameNoDiac ?
8. movieSrtName ?
