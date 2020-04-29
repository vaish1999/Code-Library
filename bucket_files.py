import os
import shutil

folders = { 'video'        : ['mp4', 'mkv', 'webm', 'avi', 'mpg', 'mpe', 'mpeg', 'asf', 'wmv', 'mov', 'qt', 'rm', 'flv', 'm4v', 'ogv', 'ogg', 'srt'],
            'pictures'     : ['jpg', 'jpeg', 'png', 'gif'],
            'audio'        : ['mp3', 'wav', 'wma', 'mpa', 'ram', 'ra', 'aac', 'aif', 'm4a'],
            'pdf'          : ['pdf'],
            'python_files' : ['py'],
            'compressed'   : ['zip', 'rar', 'r0*', 'r1*', 'arj', 'gz', 'sit', 'sitx', 'sea', 'ace', 'bz2', '7z'],
            'HTML'         : ['html', 'htm'],
            'ppt'          : ['ppt', 'pptx'],
            'softwares'    : ['exe'],
            'docs'         : ['doc', 'docx', 'csv'] }

path = input("input path : ")
out_path = input("output path : ")
y_n = input("reorganize[y/n] : ")

if y_n == 'y':

    for fldr in folders:
        if not os.path.isdir(path + '/' + fldr):
            os.mkdir(path + '/' + fldr)

    fies_fldr = os.listdir(path)
    
    print("reorganizing")

    for file in fies_fldr:
        if os.path.isfile(path + '/' + file):
            ext = file.split('.')[-1]
            for fldr in folders:
                if (ext in folders[fldr]):
                    if not os.path.isfile(path + '/' + fldr + '/' + file):
                        shutil.move(path + '/' + file, path + '/' + fldr)
                        print('.', end = '')


print("\ndone")