#print the number num to the standard output
#sample input:"-1234abf&567"
#sample output:"-1234567"
####################################################
# `1) first way`
text=input("Enter the string:")
num=""
for char in text:
    if char.isdigit() or (char=='-' and len(num)==0):
        num=num+char
print(num)
# ###################################################
# #`2) second way`
text = input("Enter the string: ")
num = ""

for ch in text:
    if ch.isdigit():
        num += ch

print(num)
#####################################################
#3) third way
text = input("Enter the string: ")
num = ""

for ch in text:
    if '0' <= ch <= '9':
        num += ch

print(num)
#######################################################