import re
# def check_sentence(text):
#   result = re.search(r"^[A-Z][a-z ]*[.?!]$", text)
#   return result != None

# print(check_sentence("Is this is a sentence?")) # True
# print(check_sentence("is this is a sentence?")) # False
# print(check_sentence("Hello")) # False
# print(check_sentence("1-2-3-GO!")) # False
# print(check_sentence("A star is born.")) # True










def valid_var(check_it):
    pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"     
    #can use pattern=r"^[a-zA-Z_]\w*$"     it will work too     
    result = re.search(pattern,check_it)
    if result!= None:
        return True
    else:
        return False

print(valid_var("_This is_valid_9"))



import re
def check_web_address(text):
  pattern = r"[a-zA-Z+-._]*\.[a-zA-Z]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True



import re
def check_time(text):
  pattern = r"^[0-9]*:[0-5][0-9] *[ampmAMPM]+$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False




import re
def contains_acronym(text):
  pattern = r"\([0-9]*[A-Z]\w+\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True






import re
def check_zip_code (text):
  result = re.search(r"[0-9][0-9][0-9][0-9][0-9].*[0-9][0-9][0-9][0-9]", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False