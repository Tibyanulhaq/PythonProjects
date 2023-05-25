import qrcode as qr
img=qr.make("hello world")
img.save("helloworld.png")