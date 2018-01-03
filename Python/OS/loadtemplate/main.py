#!/usr/bin/python3

import sys
from subprocess import call

fichier = open('/home/meliodas/Labô/template/raccourci','r')

lines=fichier.readlines()
dico = {}
for line in lines:
    etiq, way = line.split(':')
    dico[etiq] = way[:-1]


for arg in sys.argv[1:]:
    if(arg in dico):
        call(["cp", "-r","/home/meliodas/Labô/template/"+dico[arg], "."])
    else:
        print("Wait! Wait! Wait! {} doesn't have a raccourci".format(arg))
