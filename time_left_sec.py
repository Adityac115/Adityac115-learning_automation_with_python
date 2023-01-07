def to_seconds(hours,minutes,seconds):
    return hours*3600+minutes*60+seconds

print("welcome to ths time convertor")

ans="y"
while(ans.lower()=="y"):
    hours=int(input("enter the humber if hours: "))
    minutes=int(input("enter the number of minutes: "))
    seconds=int(input("enter the seconds: "))

    print(f"Thats {to_seconds(hours,minutes,seconds)} seconds \n")
    ans=input("do you want to do naother conversio? [y to continue]")

print("Good bye!")