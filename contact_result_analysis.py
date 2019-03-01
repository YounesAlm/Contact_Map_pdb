#!/usr/bin/python3
import argparse
from os.path import isfile
from pprint import pprint
from math import sqrt
parser = argparse.ArgumentParser(description='Computes a contact matrix in csv format of every contact observed through the dynamic')
parser.add_argument('--result', required=True, help='result file obtained from contact_finder.py script')

param = parser.parse_args()


prot = {}
nodes= {}
#load all alpha carbons coordinates in a dictionnary

visited=[]

with open( param.result ) as f:
    content = f.read()
    lines= content.split('\n')
    for l in lines:
        words = l.split(',')
        if len(words)>4 :
            if (words[1],words[4]) not in visited:
                prot[(int(words[1]),int(words[4]))]= int(1)
                prot[(int(words[4]),int(words[1]))]= int(1)
                nodes[int(words[1])]=words[0]
                nodes[int(words[4])]=words[3]
                
                visited.append((words[1],words[4]))
                visited.append((words[4],words[1]))
            else:
                prot[(int(words[1]),int(words[4]))]+=1
                prot[(int(words[4]),int(words[1]))]+=1
keylist = prot.keys()
nodelist=[]

for key in sorted(keylist):
    if key[0] not in nodelist:
        nodelist.append(key[0])
    if key[1] not in nodelist:
        nodelist.append(key[1])
nodelist=sorted(nodelist)
#print(nodelist)

print('NA', end="")
for i in nodelist:
    print(',',nodes[i],i,sep="",end="")

nodes_size=0
print()
#pprint(prot)
for i in range(len(nodelist)):
    print(nodes[nodelist[i]], nodelist[i],sep="",end="")
    for j in range(len(nodelist)):
        if (nodelist[i],nodelist[j]) in keylist:
            print(",",prot[(nodelist[i],nodelist[j])],end="")
        else:
            print(",",0,end="")
    print()
#pprint(prot)
#search for close contacts, defined as a distance inferior or equal to 8 angstrom
#already_visited=[] #save the tuple of the visited contact relationship to avoid duplicates in final output
#for u in prot:
#    for v in prot:
#        if prot[u]['domain']!=0 and prot[v]['domain']!=0 and prot[v]['domain']!=prot[u]['domain'] :
#            dx = prot[v]['xca']-prot[u]['xca']
#            dy = prot[v]['yca']-prot[u]['yca']
#            dz = prot[v]['zca']-prot[u]['zca']
#            if (u,v) not in already_visited and (v,u) not in already_visited:
#                distance = sqrt(pow(dx,2)+pow(dy,2)+pow(dz,2))
#                if distance <= 8:
#                    print( prot[u]['resname'],u,distance,prot[v]['resname'],v , sep=',')
#                    already_visited.append((u,v))
#                    already_visited.append((v,u))
