import qrcode
img = qrcode.make('Some data here')
img.save("some_file.png")



import qrcode

qr = qrcode.QRCode(box_size=20, border=8)
qr.add_data("https://github.com/thadidaniel-ctrl")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("github_qr.png")