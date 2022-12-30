import datetime
import os
os.remove("first.txt")
os.rename("first_2.txt", "abc.txt")
print(os.path.exists("first.txt"))
print(os.path.exists("abc.txt"))
print(os.path.getsize("hello.txt"))
timestamp=os.path.getmtime("hello.txt")                      #give output as unix date
print(datetime.datetime.fromtimestamp(timestamp))            #covert unix output into readable output
print(datetime.datetime.fromtimestamp(timestamp).strftime("%d-%m-%y %H:%M:%S"))  #prints according to format we give
print(os.path.abspath("hello.txt"))                      #gives total path of file    
print(os.getcwd())                                       #pwd of linux
print(os.listdir())                                     #ls -a of linux   
print(os.mkdir('hello'))    
print(os.chdir("hello"))                              
os.rmdir('hello')
