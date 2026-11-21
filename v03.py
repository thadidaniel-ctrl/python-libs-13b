import pyfiglet
import qrcode
from PIL import Image, ImageDraw, ImageFont

banner = pyfiglet.figlet_format("DANIEL", font="standard")
lines = banner.rstrip().split("\n")

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data("https://github.com/thadidaniel-ctrl")
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

try:
    font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 16)
except OSError:
    font = ImageFont.load_default()

line_h = 20
text_w = int(max(font.getlength(line) for line in lines)) + 20
width = max(qr_img.width, text_w)
height = qr_img.height + line_h * len(lines) + 20

canvas = Image.new("RGB", (width, height), "white")
canvas.paste(qr_img, ((width - qr_img.width) // 2, 0))

draw = ImageDraw.Draw(canvas)
y = qr_img.height + 10
for line in lines:
    draw.text((10, y), line, font=font, fill="black")
    y += line_h

canvas.save("qr_banner.png")