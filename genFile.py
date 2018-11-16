#!/usr/bin/env python

def genFile():
    count = 0
    
    for count in range(64):
        count = count + 1
        tmptest = str(count)
        fileh = open("tmp/" + tmptest, "w")
        fileh.write(str(count))

if __name__ == '__main__':
    genFile()
