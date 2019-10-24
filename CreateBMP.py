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
    
    