#!/usr/bin/env python3
import sys
import os
import re
def error_search(log_file):
  error = input("What is the error? ")                                         #asks user which type of error he/she wants to see from thre log file
  returned_errors = []                                                         #this will store all the log that matches our requirements
  with open(log_file, mode='r',encoding='UTF-8') as file:                      
    for log in  file.readlines():                                              #we will go through log files line by line
      error_patterns = ["error"]                                               #taking "error" as default error pattern in log files
      user_input_error=error.split(' ')                                        #splitting the user inputted error to store
      for i in range(len(user_input_error)):                                   #iterate over every user input error 
        error_patterns.append(r"{}".format(user_input_error[i].lower()))       # make them lower and append in error_patterns
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):         #iterate over every error patern and check if it matches in that log line
        returned_errors.append(log)                                                              #if all pattern matches append that log line into return errors
    file.close()
  return returned_errors
  
def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/python/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()
if __name__ == "__main__":
  log_file = "log_file"
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)