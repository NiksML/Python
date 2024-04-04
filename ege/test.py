with open("27_A.txt","r") as file:
    countz=file.readline()
    #print(countz)
    priyom=[]
    for i in range(1,int(countz)+1):
        zayavka=file.readline()
        if zayavka == "":
            print("end of file")
            break
        time = list(map(int,zayavka.split(" ")))
        start,end = time
        if i==1:
            priyom.append(time)
            continue
        lenght = len(priyom)
        for k in range (0,lenght):
            if priyom[k][0] < start < priyom[k][1] or priyom[k][0] < end < priyom[k][1] or (priyom[k][0] > start and end < priyom[k][1]):
                break
            if k==lenght-1:
                priyom.append(zayavka)
    print(priyom)