import qrcode


data = input("Enter text or URL: ").strip
filename = ("Enter your filename: ").strip
qr = qrcode.QRCode(box_size=10, border=4)

qr.add_data(data)
qr.make_image(fill_color="black", back_color="blue")
img = qrcode.make('https://main.d3vianaxlv4x9d.amplifyapp.com/')
type(img) 
img.save("some_file.png")
