from PIL import Image, ImageDraw
from random import randint


def stega_encrypt():
    text = input('Enter text: ')
    keys = []
    img = Image.open(input('Image: '))
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    f = open('keys.txt','w')

    for elem in ([ord(elem) for elem in text]):
        key = (randint(1,width-10),randint(1,height-10))
        r,g,b = pix[key][:3]
        draw.point(key, (r,elem,b))
        f.write(str(key)+'\n')

    img.save('steganographyImage.png','PNG')
    f.close()

def main():
    stega_encrypt()


if __name__ == '__main__':
    main()