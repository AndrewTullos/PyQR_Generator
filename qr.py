import qrcode
img = qrcode.make('https://main.d3vianaxlv4x9d.amplifyapp.com/')
type(img) 
img.save("some_file.png")