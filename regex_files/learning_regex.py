import re
s="July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# index=s.index('[')
# print(index)
# outdex=s.index(']')
# print(outdex)
# print((s[index+1:outdex]))

# regex=r"\[(\d+)\]"
# result=re.search(regex,s)
# print(type(result))
# print(result)

result=re.search(r"p.ng","Pangea",re.IGNORECASE)                       #ignore case
rs=re.search(r"^x","xenon")                                   #return if line start from x
res=re.search(r"wick$",'John wick')                          #return if line ends with wick

#charachter classes are defined by []
a=re.search(r"[Pp]ython","Python")                           #check both P and p in Python
b=re.search(r"[a-z]way","the end of the highway")             #checks any lower caseletter from a to z with way
c=re.search(r"cloud[a-zA-z0-9]","cloudy")                  #checks any upper or lower case letter or any number after cloud
d=re.search(r"[.,:;!]","I'm done for today!")           #checks if the string countain any , . : ; or !

# [^a-z] means not a-z , ^ inside [] means not the thing written after ,ex:[^a-zA-z0-9]
e=re.search(r"[^a-zA-Z]","This is sentence.")           #this will find for anything that is not a-z or A-z
f=re.search(r"[^a-zA-Z ]","This is sentence.")          #works as above but also neglects spaces

#pipe for match alternative options 
g=re.search(r"cat|dog","i like dogs")               #searches for "cat" or "dog"
h=re.search(r"cat|dog","i like cats")               #searches for "cat" or "dog"
i=re.search(r"cat|dog","i like dogs and cats")      #returns which comes first
j=re.findall(r"cat|dog","i like cats and dogs")      #returns list of things matches

#repetition Qualifiers * , ? , +
#  * repeats a character zero or more times and its greedy takes maximum anount of characters it can
k=re.search(r"Py.*n","Python Programming")          #beacuse of greedy it takes maximum characters which justify match
l=re.search(r"Py.*?n","Python Programming")          #matching style same as above but its non greedy, stops as finds the minimum match
m=re.search(r"Py[a-z]*n","Python Programming")       # gives Python becuase there is space between
n=re.search(r"Py[a-z]*n","Pyn")                   #it get matched becuase * repeates zero or more , here repeated zero times
# + matches the one or more occurences of the character that comes before it
o=re.search(r"o+l+","goldfish")                   #matches the string
p=re.search(r"o+l+","woolly")                     #takes the whole string which matches
q=re.search(r"o+l+","boil")                       #there is o and l but there is a letter between them
#  ? it means either zero or one occurence of the character before it
r=re.search(r"p?each","i like peaches")                   #there is one occurence of p so included
s=re.search(r"p?each","i like each")                     #included there is 0 occurence of p

#Escaping characters when we want to match symbol in string but its also a special character
t=re.search(r".com","welcome")                      #matches wrong becuase . is a special character
u=re.search(r"\.com","welcome.com")                 #matches as we wanted due to \ character

#python defined sets  \w for aplnumeric character including numbers,letters and __ 
# \d for digits,  \s for matching whitespaces  ,\b for word boundaries
v=re.search(r"\w","This is a sentence")
w=re.search(r"\w*","This is a sentence")
x=re.search(r"\w+\s+\w+","This is a sentence")
