import sys
import os
import subprocess                  #runs the child process ,parent waits for the child process to complete first before proceeding
# print(sys.argv)    #args uses the command line arguments for more automation
# print("PATH: "+os.environ.get("PATH",""))              #gives the path if set in env variables
# print("SHELL: "+os.environ.get("SHELL",""))             #gives the shell from env varaibles
# print("USER: "+os.environ.get("NAME",""))             # name not in env varaiable to prints "" instead

# sys.exit(0)                                #uses this to provide status , 0 if ru successfully and non 0 if failed


'''these command used when we just want to run the command to make a change and doesnt need output from them example: ping , chmod etc'''
# subprocess.run("date")                               #runs "date" command in linux shell
# subprocess.run(["sleep","2"])                       # runs "sleep 2" in linux shell
# subprocess.run(["ping","<3c","www.google.com"])             # runs ping www.google.com in linux shell

'''to use the outputs of child processes we need to use them as follows:'''
# result=subprocess.run(["host","8.8.8.8"],capture_output=True)                  #capture_ouput=True let us use the output of the child process
# print(result.returncode)                                                     #check exit status
# print(result.stdout.decode().split())                                   #use decode to decode the array of bytes in the string using UTF-8 by default

#when there is error in child process it comes in stderr

# res=subprocess.run(["rm","this_file_does_not_exist"],capture_output=True)
# print(res.stdout)                       #stdout containes empty string becuase child process failed
# print(res.stderr)                       #stderr conatines error child process generated




my_env = os.environ.copy()               #copying the environment variables as dictionary 
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])    #adding /opt/add in PATH variable
result=subprocess.run("myapp",env=my_env)
print(result.stdout)


