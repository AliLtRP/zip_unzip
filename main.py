import zipfile
from os import listdir
from os.path import isfile, join
import scrr as m


choose = input("Enter zip/unzip: ")

if choose.lower() != "zip" and choose.lower() != "unzip":
    raise TypeError("only zip or unzip allowed")

# path where the files you want to zip/unzip them
path = input("/path/to/directory/ : ")

# get names of files in path to zip them
path_files = [item for item in listdir(path) if isfile(join(path, item))]

if choose.lower() == "unzip":
    m.unzip1(path, path_files)
else:
    m.zip1(path, path_files)
