import qrcode

# membuat qr code
img = qrcode.make("www.mahmudsoft.com")

# menyimpan qr code
img.save("qr_mahmudsoft.png")
