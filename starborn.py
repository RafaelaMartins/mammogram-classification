# -*- coding: utf-8 -*-
import os
import random
from sys import argv, stdin, stdout

def parser(args):
    option = {}
    option['file'] = args[0]
    option['randomize'] = args[1]
    return option

def main(argv):
    options = parser(argv)
    arq = open(options['file'], 'r')
    width=48
    heigth=48
    i=0
    texto = arq.readlines()
    argument = []
    if options['randomize'] == '0':
        for linha in texto:
            argument.append(linha.split())
            #print(argument)
            name = str(argument[i-1][0])
            print(linha[:6])
            x = int(argument[i][4])
            y = 1024 - int(argument[i][5])
            x = x - 24
            y = y - 24
            cmd = "mogrify -crop "+str(width)+"x"+str(heigth)+"+"+str(x)+"+"+str(y)+" "+linha[:6]+".jpg"
            #os.system(cmd)
            print(y)
            i = i + 1
    else:
        print('entrou')
        for linha in texto:
            argument.append(linha.split())
            x = int(random.randint(0, 1024))
            print(x)
            y = 1024 - int(random.randint(0, 1024))
            print(y)
            x = x - 24
            y = y - 24
            cmd = "mogrify -crop "+str(width)+"x"+str(heigth)+"+"+str(x)+"+"+str(y)+" "+linha[:6]+".jpg"
            #os.system(cmd)
            print(y)
            i = i + 1

    arq.close()

if __name__ == "__main__":
    main(argv[1:])
