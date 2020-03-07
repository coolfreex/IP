#python3
# -*- coding: utf-8 -*-

import IPassign
import ipextract
import honeyscan
import fourchange


print("")
def IP():
    IPassign.run()
    try:
     ipextract.ipjudge(filepath="ip_port.txt")
    except:
        print("ERROR")

###honeyscan接口###

    fourchange.write()

if __name__ == '__main__':
    IP()

