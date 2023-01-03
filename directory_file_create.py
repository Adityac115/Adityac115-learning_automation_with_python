import os
def new_dir(directory,file):
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
        
        os.chdir(directory)
        with open(file,'w'):
            pass
        print (os.listdir())


dir=input('Enter the directory: ')
file=input('Enter the file name: ')
new_dir(dir,file)
