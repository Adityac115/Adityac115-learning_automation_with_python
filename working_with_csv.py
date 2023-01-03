import csv
# f=open("csv_file.csv")
# csv_f=csv.reader(f)                  #reads the data of csv and store in csv_file
# print(csv_f)                         #cant see the data because it is object 
# count=0
# for row in csv_f:                   #row contains data line by line in a list splitted by ','
#     name,phone,role=row
#     print(f"NAme: {name} , Phone: {phone} , Role: {role}")
#     count+=1
# # print(f"Total: {count}")
# f.close()






# '''cretaing a csv file'''

# hosts=[["worksration.local","192.168.25.46"],["websercer.cloud0","10.2.5.6"]]
# with open('hosts.csv','w') as file:              #always open in w or a mode when write
#     writer=csv.writer(file)                     #writer has 2 functions : writerow,writerows
#     writer.writerows(hosts)                #writerows put all data once , writerow put one by one





# '''working with dictionary'''

# #writing dict in csv
with open('./csv_files/software.csv','w') as f:
    writer=csv.DictWriter(f,fieldnames=["name","version","status","users"])
    writer.writeheader()                     #writes the header of the csv header is fieldnames
    writer.writerow({'name':"MailTree","version":5.34,'status':"production","users":324})
    writer.writerow({'name':"CalDoor","version":1.25,'status':"beta","users":22})
    writer.writerow({'name':"Chatty Chicken","version":0.34,'status':"alpha","users":4})






#reading dict in csv
with open('./csv_files/software.csv') as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} has {row['users']} users")
