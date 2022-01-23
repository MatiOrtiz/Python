import re

print(re.search(r"aza", "plaza")) #span=(2,5)

print(re.search(r"aza", "maze")) #none

print(re.search(r"^x", "xenon")) #span=(0,1)

print(re.search(r"p.ng", "ping")) #span=(0,4)
print(re.search(r"p.ng", "pong")) #span=(0,4)

print(re.search(r"i.la", "Island", re.IGNORECASE)) #span=(0,4)

print(re.search(r"[Pp]ython", "Python")) #span=(0,6)

print(re.search(r"[a-z]way", "The end of the highway")) #span=(18,22)

print(re.search(r"sun[a-zA-Z0-9]", "sunny")) #span=(0,4)

print(re.search(r"cat|dog", "I like cats.")) #span=(7,10)
print(re.search(r"cat|dog", "I like dogs.")) #span=(7,10)
print(re.findall(r"cat|dog", "I like both dogs and cats")) #['dog','cat']

print(re.search(r"Py.*n", "Pygmalion")) #span=(0,9)
print(re.search(r"Py.*n", "PythonProgramming")) #span=(0,16)

print(re.search(r"o+l+", "goldfish")) #span=(1,3)
print(re.search(r"o+l+", "woolly")) #span=(1,5)
print(re.search(r"o+l+", "boil")) #none

print(re.search(r"p?each", "To each their own")) #span=(3,7)
print(re.search(r"p?each", "I like peaches")) #span=(7,12)

print(re.search(r".com", "welcome")) #span=(2,6)
print(re.search(r"\.com", "mydomain.com")) #span=(8,12)

print(re.search(r"\w*", "This is an example")) #span=(0,4)
print(re.search(r"\w*", "This_is_another_example")) #span=(0,23)

pattern= r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name")) #span=(0,30)
print(re.search(pattern, "this isn't a valid variable name")) #none
print(re.search(pattern, "my_variable1")) #span=(0,12)
print(re.search(pattern, "2my_variable1")) #none


#FUNCTIONS:

#1:
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


#2:
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False


#3:
def repeating_letter_a(text):
  result = re.search(r"a.*a", text, re.IGNORECASE)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True


#4:
def check_character_groups(text):
  result = re.search(r"[0-9]\w*", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


#5:
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z| ]*[.?!]", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True