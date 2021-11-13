# We gonna encode & decode qr-code
import qrcode
import random
import string

random.seed(0)
data:str = 'HI THERE I AM NEWBIE'
print(data)

# basic one
img = qrcode.make(data)
img.save('./Basicqrcode.png')

# more customized
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data = data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')
img.save('./Customizedqrcode.png')


# To decode a qrcode
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('./Customizedqrcode.png', 'r')

# to decode - It also gives properties
decoded_data = decode(image = img)
print(decoded_data)
