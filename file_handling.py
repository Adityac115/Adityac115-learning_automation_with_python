# #!/usr/bin/env python3

# '''open-close approach
#  here you have to close the file after you have done your operation on it'''

# handle=open("hello.txt")        
# print(handle.readline())
# handle.close()


# '''with approach
# you can work in a block and python will close the file after you leave that block'''

# with open("hello.txt") as file:
#     print(file.readline())
    
# '''iterating over the content of the file'''

# with open("hello.txt") as file:
#     for line in file:
#         print(line.strip())                   #to remove '\n' at the end of each line



# #readllines() covert file into list consist of lines

# '''writing into the file'''

# with open("hello.txt","w") as file:
#     file.write("hello")


# '''guess coming'''
# intitial_guests=["adi","ayush","pandey","johri"]
# guests=open("guests.txt","w")
# for i in intitial_guests:
#     guests.write(i +"\n")
# guests.close()

# with open("guests.txt","r") as guests:
#     for line in guests:
#         print(line)

# '''some new guests'''
# new_guests=["dev","bhaiyaji","nikhil"]
# guests=open("guests.txt","a")
# for i in new_guests:
#     guests.write(i +"\n")
# guests.close()

# with open("guests.txt","r") as guests:
#     for line in guests:
#         print(line)

# '''some guests checked out so update list'''
# tmp_lst=[]
# chechek_out=["nikhil","dev","bhaiyaji"]
# with open("guests.txt","r") as guests:
#     for line in guests:
#         tmp_lst.append(line.strip())

# with open("guests.txt","w") as guests:
#     for name in tmp_lst:
#         if name not in chechek_out:
#             guests.write(name +"\n")

# with open("guests.txt","r") as guests:
#     for line in guests:
#         print(line)

# '''check whether given guests is checked in or not'''
# guests_to_check=["pandey","dev"]
# checked_in=[]
# with open("guests.txt","r") as guests:
#     for line in guests:
#         checked_in.append(line.strip())
#     for check in guests_to_check:
#         if check in checked_in:
#             print(f'{check} is checked in')
#         else:
#             print(f'{check} is not checked in')





