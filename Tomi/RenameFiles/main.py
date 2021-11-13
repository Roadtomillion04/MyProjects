# We gonna grab the folder in desktop and rename it's inside files
import os

# select a folder path
dir_path = r'C://Users/Admin/Desktop/IndividualSprites'

for idx, img in enumerate(os.listdir(dir_path)):
    source = f'{dir_path}/{img}' # exiting name
    destination = f'{dir_path}/RenamedImage{idx}.png' # new name
    os.rename(source, destination)

