import os, shutil

def copy(fromFolder, desFolder, ext):
    fromFolder = os.path.abspath(fromFolder)
    desFolder = os.path.abspath(desFolder)

    for folderName, subFolders, fileNames in os.walk(fromFolder):
        for fileName in fileNames:
            if fileName.endswith('.{}'.format(ext)):
                print("Copying from {} to {}".format(fileName, desFolder))
                try:
                    shutil.copy(os.path.join(folderName, fileName), desFolder)
                except shutil.SameFileError:
                    print("File is the same name.")

        for folder in subFolders:
            copy(folder, desFolder, ext)

copy('.', './copy_des', 'txt')
