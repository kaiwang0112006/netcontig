# -*- coding: utf-8 -*-
import networkx as nx
import time
import argparse
import csv

##########################################
## Options and defaults
##########################################
def getOptions():
    parser = argparse.ArgumentParser(description='python *.py [option]"')
    requiredgroup = parser.add_argument_group('required arguments')
    requiredgroup.add_argument('--input', dest='input', help='input file to insert into NET', default='', required=True)
    requiredgroup.add_argument('--start', dest='start', help='start nodes file', default='', required=True)
    requiredgroup.add_argument('--end', dest='end', help='end nodes file', default='', required=True)
    parser.add_argument('--out',dest='output',help='output file', default='output.out')
    args = parser.parse_args()

    return args

class CONTIGGRAPH(object):
    def __init__(self):
        self.G = nx.Graph()
        
    def buildGraph(self, input):
        '''
        Fetch all the source and tartget id from input file to build a net
        '''
        with open(input) as fin:
            for eachline in fin:
                line = eachline.split()
                if line[0] == '0' or line[1] == '0':
                    print "abnormal line:",eachline
                self.G.add_node(line[0])
                self.G.add_node(line[1])           
                self.G.add_edge(line[0],line[1])
                
    def shortCal(self,start, end):
        self.allspath = nx.all_shortest_paths(self.G,source=start,target=end)
        
    def allshortpath(self,startlist,endlist):
        '''
        For each start and end pair in the list, calculate all shortest paths and formate dict to store them.
        i,j are list index and s,e are ids.
        '''
        
        self.allspath = {}
        for i, s in enumerate(startlist):
            for j,e in enumerate(endlist):
                 self.allspath[(s,e)] = nx.all_shortest_paths(self.G,source=s,target=e)
                 
        
    def shortestpath(self,startlist,endlist):
        '''
        For each start and end pair in the list, calculate shortest paths and formate dict to store them.
        i,j are list index and s,e are ids.
        '''
        
        self.allspath = {}
        for i, s in enumerate(startlist):
            for j,e in enumerate(endlist):
                try:
                    self.allspath[(s,e)] = nx.shortest_path(self.G,source=s,target=e)
                except:
                    print "Shorest path error for:",(s,e)
                    print "But continue..."
        
    def formateOutput_list(self, output):
        '''
        With the dict that have id pairs and their shortest paths, an output will be generated.
        eachline as a csv format and return allshortest paths:
        startid,endid,path
        
        path is formate as id1|id2|....|idn
        '''  
        fout = open(output,'w')
        for pair in self.allspath:
            s = pair[0]
            t = pair[1]
            try:
                for p in self.allspath[pair]:
                    pstr = '|'.join(p)
                    fout.write("%s,%s,%s\n" % (s,t,pstr))
            except:
                fout.write("%s,%s,nopath\n" % (s,t))
                
    def formateOutput_str(self, output):
        '''
        With the dict that have id pairs and their shortest paths, an output will be generated.
        eachline as a csv format and return shortest paths:
        startid,endid,path
        
        path is formate as id1|id2|....|idn
        '''  
        fout = open(output,'w')
        for pair in self.allspath:
            s = pair[0]
            t = pair[1]
            try:
                path = self.allspath[pair]
                pstr = '|'.join(path)
                fout.write("%s,%s,%s\n" % (s,t,pstr))
            except:
                fout.write("%s,%s,nopath\n" % (s,t))
                
def readids(file):
    '''
    a file contain start or end id will be parsed.
    file like:
    ...
    R498_5022013_1/1833_21834
    R498_4314669_1/8_17103
    ...
    
    will be stored in a list:
    [...,'R498_5022013_1/1833_21834','R498_4314669_1/8_17103',....]
    '''
    idlist = []
    with open(file) as fin:
        for eachline in fin:
            id = eachline.strip()
            idlist.append(id)
    return idlist
            

##########################################
## Master function
##########################################           
def main():
    options = getOptions()
    print "parsing start/end nodes file..."
    startlist = readids(options.start)
    endlist = readids(options.end)

    contiggraph = CONTIGGRAPH()
    print "building graph..."
    contiggraph.buildGraph(options.input)
    print "complete graph"
    print "cal short path..."
    contiggraph.shortestpath(startlist, endlist)
    print "Formating output...."
    contiggraph.formateOutput_str(options.output)




    
if __name__ == "__main__":
    main()