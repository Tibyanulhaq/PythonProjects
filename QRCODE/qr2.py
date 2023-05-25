import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=10)
input=input("Enter URL here : ")
qr.add_data(input)
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="yellow")
img.save("youtube.png")