import os
totalSize = 0

currpath = os.getcwd()
for filename in os.listdir(currpath):
    if not os.path.isfile(os.path.join(currpath, filename)):
        continue
    totalSize += os.path.getsize(os.path.join(currpath, filename))

print(totalSize)
