import segno
#this makes small qr codes
outputDirectory = '/Users/kemalozyon/Downloads/QRCodeMaker/'
qrCode = segno.make_qr("Hello, world!")

fileName = input("Enter your file name = ")
qrCode.save(f"{outputDirectory}{fileName}.png")


#Changing the size of qr code

outputDirectory = '/Users/kemalozyon/Downloads/QRCodeMaker/'
qrCode = segno.make_qr("Hello, world!")

fileName = input("Enter your file name = ")
qrCode.save(f"{outputDirectory}{fileName}.png",scale = 5)

#formatting the border of a qr code:

outputDirectory = '/Users/kemalozyon/Downloads/QRCodeMaker/'
qrCode = segno.make_qr("Hello, world!")

fileName = input("Enter your file name = ")
qrCode.save(f"{outputDirectory}{fileName}.png",scale = 5,border = 10,light = "lightblue")

