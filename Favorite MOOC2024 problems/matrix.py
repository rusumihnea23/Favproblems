def matrix_sum():
    lista=[]
    matrice=[]
    with open("matrix.txt") as fisier:
        for line in fisier:
            line=line.replace("\n","")
            lista=line.split(",")
            matrice.append(lista)
    suma=0
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            suma=suma+int(matrice[i][j])
    return suma
def matrix_max():
    lista=[]
    matrice=[]
    with open("matrix.txt") as fisier:
        for line in fisier:
            line=line.replace("\n","")
            lista=line.split(",")
            matrice.append(lista)
    maxi=int(matrice[0][0])
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if maxi< int(matrice[i][j]):
                maxi=int(matrice[i][j])
    return maxi
def row_sums():
    lista=[]
    matrice=[]
    with open("matrix.txt") as fisier:
        for line in fisier:
            line=line.replace("\n","")
            lista=line.split(",")
            matrice.append(lista)
    sume=[]
    for i in range(len(matrice)):
        sum=0
        for j in range(len(matrice[i])):
            sum=sum+int(matrice[i][j])
        sume.append(sum)
    return sume