with open("26.txt") as file:
    data=file.readline()
    x = list(map(int,data.split()))
    count,time = x
    vizitors=[]
    priem=[]
    total_vizitors=0
    for i in range(1,1001):
        time1=file.readline()
        y = list(map(str,time1.split()))
        begin,dur,gender=y
        begin=int(begin)
        dur=int(dur)
        end=begin+dur
        if begin>time:
            continue
        vizitors.append((begin,dur,gender))
    vizitors.sort(key=lambda x:(x[0],x[2]!='G',x[2]!='W'))
    #vizitors.sort(key=lambda x: (x[2] != 'G', x[2] != 'W', x[0]))



    for i in range(1,len(vizitors)):
        if (vizitors[i-1][0] + vizitors[i-1][1]) <= vizitors[i][0] and vizitors[i][2] == 'G':
            priem.append(vizitors[i])
        
for i in range(len(vizitors)):
    print(f'{i} {vizitors[i]}')
print(len(vizitors))


    

