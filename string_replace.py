# str1="hello world"
# print(str1.replace("ell","***"))

fin = open("practice.txt","r")
data=fin.read()
rword=input("enter word to replace:")

# data=data.replace("scored","shoot")
data=data.replace(rword,'*'*len(rword))
fout = open("practice2.txt","w")

fout.write(data)

fout.close()
fin.close()