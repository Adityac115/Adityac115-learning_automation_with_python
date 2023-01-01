import os
dir=input("enter the absolute path of the directory: ")
for name in os.listdir(dir):
    fullname=os.path.join(dir,name)
    if os.path.isdir(fullname):
        print(f'{fullname} is a directory')
    else:
        print(f'{fullname} is a file')