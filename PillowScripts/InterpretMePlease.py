from PIL import Image
from io import BytesIO
import requests

def main():
    url = getImg()
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()













































if __name__ == '__main__':
    def getImg():
        return 'https://cs14.pikabu.ru/post_img/2023/04/16/4/1681620907163827612.webp'


main()

















