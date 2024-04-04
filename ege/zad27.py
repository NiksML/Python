import sys


def zapis_na_priem():
    with open(sys.argv[1]) as file:
        count_of_priem = file.readline()
        priem = []
        for i in range(1,int(count_of_priem)+1):
            zayavka = file.readline()
            if zayavka == '':
                print("end of file")
                break 
            time = list(map(int, zayavka.split()))
            start, end = time
            if i == 1:
                priem.append(time)
                continue
            l = len(priem)
            for k in range(0,l):
                if  priem[k][0] < start < priem[k][1] or priem[k][0] < end < priem[k][1] or (priem[k][0] > start and end > priem[k][1]):
                    break
                if k == l-1:
                    priem.append(time)

        print(priem,end='\n')
        print(f"Записей на прием: {len(priem)}")


def main():
    zapis_na_priem()


if __name__ == "__main__":
    main()
