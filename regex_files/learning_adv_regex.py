import re
result=re.search(r"^(\w*), (\w*)$","Kushwaha, Aditya")
print(result[0])



def rearrange_name(name):
    result=re.search(r"^([\w* \.-]*), ([\w* \.-]*)$",name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"

print(rearrange_name("Kushwaha, Aditya K."))

'''can use sub here also'''
def rearrang_name(name):
    result=re.sub(r"^([\w* \.-]*), ([\w* \.-]*)$",r"\2 \1",name)                   #here r"\2 \1" represents 2 and 1 capture groups respectively
    if len(result)==0:
        return name
    return result

print(rearrang_name("kushwaha, Aditya k."))







#more repetition Qualifiers

result=re.search(r"[a-zA-Z]{5}","a ghost")                         #matches the string of lenth 5
a=re.search(r"[a-zA-Z]{5}","a scary ghost")                        #returns the first match  only,use finadall here to get matches
b=re.findall(r"[a-zA-Z]{5}","a scary ghost appear")                #gets extra match as appea remove this using \b
c=re.findall(r"\b[a-zA-Z]{5}\b","a scary ghost appear")
d=re.findall(r"\b[a-zA-Z]{5,10}\b","i really like strawberries")     #if we want to get length of string to be between 5 and 10 both values included 
e=re.findall(r"[a-zA-Z]{5,}","i really like strawberries")       #this means atleast 5 and no upper bpundary for match


g=re.split(r"[,?!]","ONe sentence. Another one? And the last one! ")         #spilitted by chaarcter but didnt included them in ouput
h=re.split(r"([,?!])","ONe sentence. Another one? And the last one! ")         #spiltted by charchter and used capture groups to capture to include them as well 

# sub function
i=re.sub(r"[\w.%+-]+@[\w.-]+","[Redacted]","Recieved an email from go_haity76@my.example.com")

print(type(i))