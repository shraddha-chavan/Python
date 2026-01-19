#no. of chracters,words and lines in a file
fo=open("sample.txt","r")
data=fo.read()
print("Characters:",len(data))
words=data.split()
print("Words:",len(words))
lines=data.split("\n")
print("Lines:",len(lines))
fo.close()