#!/usr/bin/python3
import argparse
from os.path import isfile
from pprint import pprint
from math import sqrt
parser = argparse.ArgumentParser(description='Search contacts between all residues in a protein given in pdb format')
parser.add_argument('--pdb', required=True, help='PDB file')
parser.add_argument('--start1', required=True, help='Residue number where the first domain begins')
parser.add_argument('--start2', required=True, help='Residue number where the second domain begins')
parser.add_argument('--end1', required=True, help='Residue number where the first domain ends')
parser.add_argument('--end2', required=True, help='Residue number where the first domain ends')

param = parser.parse_args()


prot = {}

#load all alpha carbons coordinates in a dictionnary
begin_1=int(param.start1)
begin_2=int(param.start2)
end_1=int(param.end1)
end_2=int(param.end2)

with open( param.pdb ) as f:
    content = f.read()
    lines= content.split('\n')
    for l in lines:
        words = l.split()
        if len(words)>1 and words[0]=='ATOM' and words[3]!='WAT':
            if int(words[5])>=begin_1 and int(words[5])<=end_1:
                prot[words[5]]={ 'resname' : words[3] , 'domain' : 1 , 'xca' : float(words[6]), 'yca' : float(words[7]), 'zca' : float(words[8]) }
            elif int(words[5])>=begin_2 and int(words[5])<=end_2:
                prot[words[5]]={ 'resname' : words[3] , 'domain' : 2 , 'xca' : float(words[6]), 'yca' : float(words[7]), 'zca' : float(words[8]) }
            else:
                prot[words[5]]={ 'resname' : words[3] , 'domain' : 0 , 'xca' : float(words[6]), 'yca' : float(words[7]), 'zca' : float(words[8]) }
#search for close contacts, defined as a distance inferior or equal to 8 angstrom
already_visited=[] #save the tuple of the visited contact relationship to avoid duplicates in final output
for u in prot:
    for v in prot:
        if prot[u]['domain']!=0 and prot[v]['domain']!=0 and prot[v]['domain']!=prot[u]['domain'] :
            dx = prot[v]['xca']-prot[u]['xca']
            dy = prot[v]['yca']-prot[u]['yca']
            dz = prot[v]['zca']-prot[u]['zca']
            if (u,v) not in already_visited and (v,u) not in already_visited:
                distance = sqrt(pow(dx,2)+pow(dy,2)+pow(dz,2))
                if distance <= 8:
                    print( prot[u]['resname'],u,distance,prot[v]['resname'],v )
                    already_visited.append((u,v))
                    already_visited.append((v,u))
