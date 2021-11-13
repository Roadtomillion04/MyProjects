# Here we are going to duplicate an Image multiple times
from PIL import Image

dir_path = r'C://Users/Admin/Desktop/IndividualSprites/Image-0.png'

def duplicate_files():
    for i in range(1, 20):
        with Image.open('Image-0.png', 'r') as img:
            img.save(f'C://Users/Admin/Desktop/IndividualSprites/Image{i}.png', 'png')


duplicate_files()