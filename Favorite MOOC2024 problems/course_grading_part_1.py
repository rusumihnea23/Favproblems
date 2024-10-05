def students(dic:dict,name:str):
    with open(name) as fisier:
        for line in fisier:
            line=line.replace("\n","")
            parts=line.split(';')
            if parts[0]=="id":
                continue
            dic[parts[0]]=parts[1]+" "+parts[2]
def exercises(dic:dict,name:str):
    
    with open(name) as fisier:
        for line in fisier:
            suma=0
            line=line.replace("\n","")
            parts=line.split(';')
            if parts[0]=="id":
                continue
            for i in range(1,len(parts)):
                suma=suma+int(parts[i])
            dic[parts[0]]=dic[parts[0]]+" "+str(suma)


studenti=input("Student information ")
xercise=input("Exercises completed ")
d={}
students(d,studenti)
exercises(d,xercise)
for elements in d:
        print(d[elements])