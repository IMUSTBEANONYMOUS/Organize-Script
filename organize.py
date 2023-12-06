import os
import shutil

path = os.getcwd()

ext_files = {
    '.txt' : 'TEXT FILES',
    '.pdf' : 'PDFS',
    '.png' : 'IMAGES',
    '.jpg' : 'IMAGES',
    '.mp4' : 'VIDEOS',
    '.mp3' : 'AUDIOS',
    '.xlsx' :'EXCEL SHEETS',
    '.svg' : 'SVGS',
    '.ppt' :'POWERPOINTS',
    '.xls' : 'EXCEL SHEETS'
}

def making_files(path):
    for i in os.listdir(path):
        for j in ext_files:
            if str(j) in i and (str(ext_files[j]) not in os.listdir(path)):
                os.mkdir(ext_files[j])
    
def moving_files(path):
    for i in os.listdir(path):
        for j in ext_files:
            if str(j) in i:
                shutil.move(i,ext_files[j])

making_files(path)
moving_files(path)


