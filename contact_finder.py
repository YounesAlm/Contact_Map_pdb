#!/usr/bin/python3
import argparse
from os.path import isfile
from pprint import pprint
from math import sqrt
parser = argparse.ArgumentParser(description='Search contacts between all residues in a protein given in pdb format')
parser.add_argument('--pdb', required=True, help='PDB file')
param = parser.parse_args()


prot = {}

#load all alpha carbons coordinates in a dictionnary

with open( param.pdb ) as f:
    content = f.read()
    lines= content.split('\n')
    for l in lines:
        words = l.split()
        if len(words)>1 and words[0]=='ATOM':
            prot[words[5]]={ 'resname' : words[3] , 'xca' : float(words[6]), 'yca' : float(words[7]), 'zca' : float(words[8]) }

#search for close contacts, defined as a distance inferior or equal to 8 angstrom

for u in prot:
    for v in prot:
        if int(u) != int(v) and int(u) != (int(v)+1) and int(u) !=(int(v)-1) and int(u) != (int(v)+2) and int(u) !=(int(v)-2):
            dx = prot[v]['xca']-prot[u]['xca']
            dy = prot[v]['yca']-prot[u]['yca']
            dz = prot[v]['zca']-prot[u]['zca']
            distance = sqrt(pow(dx,2)+pow(dy,2)+pow(dz,2))
            if distance <= 8 and distance > 7:
                print( prot[u]['resname'],u,distance,prot[v]['resname'],v )
                #print(distance)
            
#pprint(prot)
