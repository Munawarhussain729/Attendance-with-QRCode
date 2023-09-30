import pandas as pd
import qrcode

def GenerateQR(url):
    img = qrcode.make(url)
    img.save("URL.png" )

url = input("Enter url to encode")
GenerateQR(url)