def buildPyramid():
    height = int(input('Enter height of pyramid: '))
    while 1 > height > 8:
        print('Pyramid height shuold be 1-8')
        height = input('Enter height of pyramid: ')
    for i in range(1,height+1):
        print((height-i) * ' ',end='')
        print((i) * '#',end=' ')
        print((i) * '#',end='')
        print((height-i) * ' ')


def main():
    buildPyramid()


if __name__ == '__main__':
    main()