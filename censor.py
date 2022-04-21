# file = open("practice.txt","r")
# print(file.read())

# to write in file 
# fin = open('practice.txt','w')
# fin.write(input("Enter any word:"))


fin = open("practice.txt","r")
data=fin.read()
badwords =["Steph",'line']
for word in badwords:
 data=data.replace(word,'*'*len(word))
fout = open("practice2.txt","w")

fout.write(data)

fout.close()
fin.close()