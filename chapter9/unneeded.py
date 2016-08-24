import os

size_100MB = 100*1000*1000

def find_unneeded(folder):
    folder = os.path.abspath(folder)
    foldersize = 0

    for foldername, subfolders, filenames in os.walk(folder):

        for subfolder in subfolders:
            foldersize += find_unneeded(subfolder)

        for filename in filenames:
            filepath = os.path.join(foldername, filename)

            try:
                filesize = os.path.getsize(filepath)
                foldersize += filesize

                if filesize > size_100MB:
                    print(filepath)
            except FileNotFoundError:
                print("not found {}".format(filepath))

        if foldersize > size_100MB:
            print(foldername)

    return foldersize

find_unneeded('/home/danhuynh/Development')
