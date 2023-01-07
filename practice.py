import re
import csv
import os


def check_if_old_email(old_pattern,email):
    old_email_pattern=r'[\w\.-]*@'+ old_pattern +'$'
    if(re.match(old_email_pattern,email)):
        return True
    return False

def replace_old_domain(old_pattern,new_pattern,email):
    email=re.sub(old_pattern,new_pattern,email)
    return email


def main():
    old_domain="abc.edu"
    new_domain="xyz.edu"
    csv_file_location="/home/aditya/python/csv_files/user_emails.csv"
    report_file="/home/aditya/python/csv_files"+"/seld_Tried_emails.txt"
    user_emails_list=[]
    new_emails_list=[]
    old_emails_list=[]
    with open(csv_file_location) as f:
        user_data_list=list(csv.reader(f))
        user_emails_list=[user_email[1].strip() for user_email in user_data_list[1:]]
        for user_email in user_emails_list:
            if(check_if_old_email(old_domain,user_email)):
                old_emails_list.append(user_email)
                changed_email=replace_old_domain(old_domain,new_domain,user_email)
                new_emails_list.append(changed_email)
        
        for user in user_data_list[1:]:
            for old_email,new_email in zip(old_emails_list,new_emails_list):
                if user[1]== ' '+old_email:
                    user[1]=' '+new_email
                    
        with open(report_file,'w') as f:
            writer=csv.writer(f)
            writer.writerows(user_data_list)
main()