import os

os.getcwd()


#Deletes all files ending in .txt
for filename in os.listdir():
    if filename.endswith(".txt"):
        os.unlink(filename)
        print(filename)
