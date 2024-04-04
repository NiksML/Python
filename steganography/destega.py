from PIL import Image
from re import findall


def stega_decrypt():
    a = []
    keys = []

    with open('keys.txt','r') as f:
        y = f.read()

    img = Image.open(input('Image: '))
    pix = img.load() 
    keys = findall(r'\((\d+),\s(\d+)\)', y)

    for key in keys:
        x, y = map(int, key)
        a.append(pix[x, y][1])

    return ''.join([chr(elem) for elem in a])


def main():
    print(f'{stega_decrypt()}')


if __name__ == '__main__':
    main()