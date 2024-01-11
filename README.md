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
- CRF28, if checked, run FFMPEG command to rewrite movie to 28 CRF   
- SRT/SUB, if checked run diacritics removal commands in Python
- MOVIE+SRT, if checked run FFMPEG command to add subtitle to movie (not burn)
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
