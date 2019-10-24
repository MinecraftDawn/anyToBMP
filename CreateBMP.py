# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:28:42 2019

@author: Eric
"""

#with open("sample.bmp","br") as file:
#    print(file.read(2))
#    print(int.from_bytes(file.read(4),"little"))
#    print(file.read(4))
#    print(int.from_bytes(file.read(4),"little"))
#    print()
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(2),"little"))
#    print(int.from_bytes(file.read(2),"little"))
#    print(file.read(4))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print()
#    file.read(1000)
#    print(file.read(1))
#    print(file.read(1))
#    print(file.read(1))
#    print(file.read(1))
    

#with open("custom.bmp","br") as file:
#    print(file.read(2))
#    print(int.from_bytes(file.read(4),"little"))
#    print(file.read(4))
#    print(int.from_bytes(file.read(4),"little"))
#    print()
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(2),"little"))
#    print(int.from_bytes(file.read(2),"little"))
#    print(file.read(4))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print(int.from_bytes(file.read(4),"little"))
#    print(file.read(1))
#    print(file.read(1))
#    print(file.read(1))
#    print(file.read(1))
    
import random
with open("custom.bmp","bw") as file:
    # File header
    file.write(bytes('BM', encoding="ascii"))
    file.write((57).to_bytes(4, byteorder="little"))
    file.write(bytes(4))
    file.write((54).to_bytes(4, byteorder="little"))
    
    #Info Header
    file.write((40).to_bytes(4, byteorder="little"))
    file.write((100).to_bytes(4, byteorder="little"))
    file.write((100).to_bytes(4, byteorder="little"))
    file.write((1).to_bytes(2, byteorder="little"))
    file.write((24).to_bytes(2, byteorder="little"))
    file.write((0).to_bytes(4, byteorder="little"))
    file.write((3).to_bytes(4, byteorder="little"))
    file.write((0).to_bytes(4, byteorder="little"))
    file.write((0).to_bytes(4, byteorder="little"))
    file.write((0).to_bytes(4, byteorder="little"))
    file.write((0).to_bytes(4, byteorder="little"))
    
    #Palette
    for i in range(100):
        for j in range(100):
            file.write(random.randrange(256).to_bytes(1, byteorder="little"))
            file.write(random.randrange(256).to_bytes(1, byteorder="little"))
            file.write(random.randrange(256).to_bytes(1, byteorder="little"))
            file.write(random.randrange(256).to_bytes(1, byteorder="little"))
    
class BMP_Image():
    def __init__(self, filePath:str):
        self.filePath = filePath
        self.inputSize = 0
        
    def createImg(self):
        with open(self.filePath, "bw") as file:
            """
            BMP Header
            """
            # ID field
            file.write(bytes('BM', encoding="ascii"))
            # Size of the BMP file (bytes)
            file.write((57).to_bytes(4, byteorder="little"))
            # Reserved bytes
            file.write(bytes(4))
            # Offset where the pixel array (bitmap data) can be found (static)
            file.write((54).to_bytes(4, byteorder="little"))
            
            """
            DIB Header (Device Independent Bitmap / Bitmap Information Header)
            """
            # Number of bytes in the DIB header (from this point)
            file.write((40).to_bytes(4, byteorder="little"))
            # Width of the bitmap in pixels
            #file.write((100).to_bytes(4, byteorder="little"))
            # Height of the bitmap in pixels
            #file.write((100).to_bytes(4, byteorder="little"))
            # Number of color planes being used
            file.write((1).to_bytes(2, byteorder="little"))
            # Number of bits per pixel
            file.write((24).to_bytes(2, byteorder="little"))
            # No pixel array compression used
            file.write((0).to_bytes(4, byteorder="little"))
            # Size of the raw bitmap data(including padding)
            file.write((3).to_bytes(4, byteorder="little"))
            # Horizontal resolution of the image.
            file.write((0).to_bytes(4, byteorder="little"))
            # Vertical resolution of the image
            file.write((0).to_bytes(4, byteorder="little"))
            # Number of colors in the color palette
            file.write((0).to_bytes(4, byteorder="little"))
            # Number of important colors used, or 0 when every color is important
            file.write((0).to_bytes(4, byteorder="little"))
            
            
    