import zipfile
from os import listdir
from os.path import isfile, join

counter = 0


def unzip1(path, path_files):
    global counter

    unzip_file = input("Where You Want to Save the unzip file?: ")

    with zipfile.ZipFile(path + '/' + path_files[0], 'r') as zip_a:
        zip_a.extractall(unzip_file)

    return "done"


def zip1(path, path_files):
    global counter

    zip_file = input("Where You Want to Save the zip file?: ")
    # "test.zip" name of zip file
    with zipfile.ZipFile(zip_file + "/test.zip", "w") as make_zip:
        while counter != len(path_files):
            make_zip.write(path + '/' + path_files[counter])
            counter += 1
    return "done"
