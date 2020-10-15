import os


#pass the path to a root folder
os.walk("")

#os.walk returns three things, foldername, subfolders, filenames

#this loops runs through a tree of all the folders
for folderName, subfolders, filenames in os.walk(""):
    print("The folder we are at is: " + folderName)
    print("The subfolders are     : " + str(subfolders))
    print("The files in folder are: " + str(filenames))

    
