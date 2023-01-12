#!/usr/bin/env python3
import re
import csv
def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain = r'[\w\.-]+@'+domain+'$'
  if re.match(domain,address):
    return True
  return False
def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address
def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'                                                          #specifieng old domain and new domain
  csv_file_location = '/home/aditya/python/csv_files/user_emails.csv'                                    #giving the file location currently having old data
  report_file = '/home/aditya/python/csv_files' + '/updated_user_emails.csv'                             #where we want to genrate the file
  user_email_list = []                                                                                  #collect all email addresses in this list
  old_domain_email_list = []                                                                              #collect all old email addresses
  new_domain_email_list = []                                                                             #collect all new email addresses
  with open(csv_file_location, 'r') as f:                                         
    user_data_list = list(csv.reader(f))                                                              #collect data like this : [[Name, Email],[blosyy,blossy@abc.edu]]
    user_email_list = [data[1].strip() for data in user_data_list[1:]]                                #as email is at index 1 of all indexes ,so iterating over data list[1:] becuase 0th element is header 
    for email_address in user_email_list:                                                        #now operating on each email address
      if contains_domain(email_address, old_domain):                                              #calling conatins_domain to check if the email is the old or not, it returns the value as true or false
        old_domain_email_list.append(email_address)                                               #if its old email add it in old_email_list
        replaced_email = replace_domain(email_address,old_domain,new_domain)                      #call replace function to replace old email with new email
        new_domain_email_list.append(replaced_email)                                              #above function return new address , so add it in new_email_list
    email_key = ' ' + 'Email Address'                                                             #doing this to know the index of every email address in user_data_list
    email_index = user_data_list[0].index(email_key)                                              #this will give index of email address 
    for user in user_data_list[1:]:                                                               #iterator user contains data od user as ['blosson', 'bloosam@abc.edu']
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):           #after zip it comes as ((old_domain_of current user,new_domain of current user))
        if user[email_index] == ' ' + old_domain:                                               #checks the index 1 of every user becuase that where is email address and checking if the email is old
          user[email_index] = ' ' + new_domain                                                   #and if the email is old domain change it with new domain
  f.close()
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()
main()