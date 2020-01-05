# -*- coding: utf-8 -*-


"""
We have a reference graph with summits, archhes between summits, each archh having a weight.
The goal is to determine which path is the longest shortest one.
The results are presented in a generated HTML web page with a graph showing the longest shortest one
"""

#-------------Generation of the webpage-------------

import webbrowser
url="result.html"
webbrowser.open(url,new=0,autoraise=True)

#-------------Import of the GraphViz module to draw the final graph containing the longest shortest path-------------

import os
os.environ["PATH"] += os.pathsep + "#Insert your path to the bin directory using / and not \"

ReferenceGraph=('Graph1', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
         [('A', 'A', 2), ('A', 'B', 5), ('A', 'C', 8), ('B', 'C', 6),
          ('B', 'D', 8), ('B', 'E', 6), ('C', 'B', 2), ('C', 'D', 1),
          ('C', 'E', 2), ('D', 'E', 3), ('D', 'F', 1), ('E', 'A', 5),
          ('E', 'D', 1), ('E', 'G', 5), ('F', 'D', 4), ('F', 'E', 1),
          ('F', 'G', 3), ('F', 'H', 6), ('E', 'I', 3), ('G', 'H', 2),
          ('H', 'B', 6), ('H', 'B', 7), ('I', 'J', 4), ('J', 'I', 5)])

#------------------------------------------------------------------------------
#Definition of the summits of the Graph
class Summit():
    def __init__(self,givenName):
        self.Name = givenName
        self.Arch_out = [] #Arch_out represents the arch leaving one summit
        self.CumulatedLengthTowards={} #Dictionary that enables knowing the distance between a summit(self) and another summit
        self.predecessor={} # Enables to know which arch is taken to go to the considered summit (self)



    def Dijkstra(self): #algorithm to find the shortest path
        #Initialization
        ReachedSummits = [self]
        self.CumulatedLengthTowards[self]=0 #le shortest path between self and self is 0
        AttainableSummits = [] #list of the attainable summits from self
        for element in self.Arch_out:
            if element.edge!=self: 
                if element.edge not in AttainableSummits or element.weight < self.CumulatedLengthTowards[element.edge]: 
                    AttainableSummits.append(element.edge) #adding all the summits directly attainable from self
                    self.CumulatedLengthTowards[element.edge]=element.weight#adding the weight of every summit nearby self
                    self.predecessor[element.edge]=element #the path to go to every nearby summits of self is the considered Arch_out
        #Fin de l'initialisation
        while len(AttainableSummits) != 0:
            #looking for the Summit linked to self with a minimal weight
            weightMinimal=self.CumulatedLengthTowards[AttainableSummits[0]] #initialization of weightMinimal
            SummitMinimal=AttainableSummits[0]# initialization of the Summit with minimal weight
            for Summit in AttainableSummits: 
                if self.CumulatedLengthTowards[Summit]<weightMinimal:
                    weightMinimal=self.CumulatedLengthTowards[Summit]
                    SummitMinimal=Summit
            ReachedSummits.append(SummitMinimal)#the Summit with minimal weight is saved
            AttainableSummits.remove(SummitMinimal)#the Summit with minimal weight is removed from the attainable summits
            for arch in SummitMinimal.Arch_out:#Starting from the summit with minimal weight, we look for the shortest path from self to the edeges of the outgoing arches
                if arch.edge in ReachedSummits:
                    pass
                elif arch.edge in AttainableSummits:
                    #looking if it's shorter to go directly from self to the considered summit or if it's better to take the Summit with minimal weight linked to self
                    if self.CumulatedLengthTowards[SummitMinimal] + arch.weight < self.CumulatedLengthTowards[arch.edge]:
                        #if so, adding the new shortest distance as a path between self and summit
                        self.CumulatedLengthTowards[arch.edge] = self.CumulatedLengthTowards[SummitMinimal] + arch.weight
                        #if so, the predecessor of this summit will become the outgoing arch linked to the summit with minimal weight nearby self
                        self.predecessor[arch.edge] = arch
                else: #if the considered summit was not nearby from self
                    AttainableSummits.append(arch.edge)
                    self.CumulatedLengthTowards[arch.edge] = self.CumulatedLengthTowards[SummitMinimal] + arch.weight
                    self.predecessor[arch.edge] = arch
                            
        
    #str
    def __str__(self):
        return self.Name
    #repr
    def __repr__(self):
        return 'Summit: '+str(self.Name)#Displaying the Summit in the Console
    
#------------------------------------------------------------------------------
#Definition of the arches of the Graph
class arch():
    
    def __init__(self,originarch,edgearch,weightarch):
        self.origin = originarch
        self.edge = edgearch
        self.weight = weightarch

    def __str__(self):
        return "origin:{}, edge:{}, weight:{}".format(self.origin,self.edge,self.weight)
    
    def __repr__(self):
        return "origin:{}, edge:{}, weight:{}".format(self.origin,self.edge,self.weight)
    
#------------------------------------------------------------------------------
#Creation of the Graph
class Graph():
    def __init__(self,givenTuple):
        # save the name
        self.Name=givenTuple[0]
        self.Summit = []
        self.arch=""
        
        #creation of the Summits
        Summits_Index={}#dictionary associating a "Summit" to the corresponding class object
        list_summitsName=givenTuple[1]
        for element in list_summitsName:
            Name=element
            newSummit = Summit(Name)
            self.Summit.append(newSummit)
            Summits_Index[Name]=newSummit
                             
        #creation of the arches
        listTriplearch = givenTuple[2]
        for triplet in listTriplearch:
            #the origin and the edge of the arch are coded as strings
            originCaract=triplet[0]
            edgeCaract=triplet[1]
            weight=triplet[2]
            #converting origin and edge into the corresponding class object using Summits_Index
            origin=Summits_Index[originCaract]
            edge=Summits_Index[edgeCaract]
            newarch = arch(origin, edge, weight)
            self.arch+="\n" + str(arch(origin, edge, weight))
            origin.Arch_out.append(newarch)
            

    def display(self):
        return """Name of the Graph: {}\nSummits of the Graph: {}\nArches of the Graph:{}""".format(self.Name,self.Summit,self.arch)

#------------------------------------------------------------------------------

def shortest_path(Graph):
    #Lauching Dijkstra
    for element in Graph.Summit:
        Summit.Dijkstra(element)

#------------------------------------------------------------------------------

def tabular_result(Graph):
    #return the shortest path between each summit in a table
    line1=" "
    #initialization of the first line of the table
    for element in Graph.Summit:
        Summit=" {0:4s} ".format(str(element))
        line1+=Summit
    print("\nMinimal distance between the summits")
    print(line1)
    for element in Graph.Summit:
        lignes=str(element)
        for destination in Graph.Summit:
            #checking if it's possible to from a summit element to a summit destination
            if destination in element.CumulatedLengthTowards.keys():
                case=" {0:4s} ".format(str(element.CumulatedLengthTowards[destination]))
                lignes+=case
            else:
                case=" {0:4s} ".format('-')
                lignes+=case
        print(lignes)

#------------------------------------------------------------------------------

def the_longest(Graph):
    #Enables to know the departure and arrival summits, and the distance between them for the longest shortest path
    distance = 0
    start=0
    arrival=0
    for Summitstart in Graph.Summit:
        for SummitArrival in Graph.Summit:
            #looking for the longest shortest path
            if SummitArrival in Summitstart.CumulatedLengthTowards.keys(): #checking is the arrival summit is actually linked to the departure summit
                if Summitstart.CumulatedLengthTowards[SummitArrival]> distance :#taking the longest path
                    distance = Summitstart.CumulatedLengthTowards[SummitArrival]
                    start = Summitstart
                    arrival = SummitArrival
    return start,arrival,distance
        
#------------------------------------------------------------------------------

def chosen_path(Graph):
    #enables to know which path was taken for the longest shortest one
    start,arrival,distance=the_longest(Graph)    
    path=start.predecessor[arrival]
    listOfPaths=[]
    while path.origin !=start:#we start by the arrival summit and we go back to the departure summit by iterating on the predecessor
        listOfPaths.append(path)
        path=start.predecessor[path.origin]
    listOfPaths.append(path)
    return listOfPaths
    
#------------------------------------------------------------------------------

def display_the_longest(Graph):
    #Display the longest shortest path in the console
    start,arrival,distance=the_longest(Graph)    
    print("\nThe longest shortest path is bewteen {} and {} with a distance of {}".format(str(start),str(arrival),distance))        
    print("\nThe arches contained in the path are :")
    listChosenPaths=chosen_path(Graph)
    listChosenPaths.reverse()
    for element in listChosenPaths:
        print("- {}".format(element))
    
#------------------------------------------------------------------------------

result=Graph(ReferenceGraph)
print(result.display())
shortest_path(result)
print(tabular_result(result))
print(display_the_longest(result))

start,arrival,distance=the_longest(result)
listChosenPaths=chosen_path(result)
listChosenPaths.reverse()

#------------------------------------------------------------------------------

#Using GraphViz
from graphviz import Digraph
g=Digraph('Graph', format='dot')#cration of the txt file describing the Graph using the dot format
#creating all the nodes of the graph
for element in result.Summit:
    g.node(str(element))
#creating all the summits of the graphs
for element in result.Summit:
    for destination in element.Arch_out:
        if destination not in listChosenPaths:
            g.edge(str(element),str(destination.edge),label=str(destination.weight))
for element in listChosenPaths:
    g.edge(str(element.origin),str(element.edge),label=str(element.weight),color='red')#displaying in red the longest shortest path
g.graph_attr['rankdir']='LR'
g.render('dot/Graph',view=False)
g.format='png'
g.render('img/Graph',view=False)

#------------------------------------------------------------------------------

#generating the HTML web page
text="""<HTML>
<HEAD>
    <TITLE>Presentation of the results """
text+="""</TITLE>
</HEAD>
<BODY>
    <H1> Minimal distance between the summits """
text+="""</H1>
    <TABLE BORDER cell padding="10" cellspacing="0" WIDTH="40%">"""

text+='<TR>'
text+='<TH align=center>'+' '+'</TH align=center>'
for element in result.Summit:
    text+='<TH align=center>'+str(element)+'</TH align=center>'
text+='</TR>'
for element in result.Summit:
    text+='<TR>'
    text+='<TH align=center>'+str(element)+'</TH align=center>'
    for destination in result.Summit:
        if destination in element.CumulatedLengthTowards.keys():
            text+='<TD align=center>'+str(element.CumulatedLengthTowards[destination])+'</TD align=center>'
        else:
            text+='<TD align=center>'+'-'+'</TD align=center>'
    text+='</TR>'


text+=" </TABLE>"

text+="<H2> The longest shortest path: between " + str(start) + " and " + str(arrival) + " with a distance of " + str(distance)
text+="</H2>"
text+="<br> arches contained in the path: <br> <br>"
for element in listChosenPaths:
    text+="-" + str(element) + "<br>"

text+="<H2> Considered Graph:  " + str(result.Name)
text+="</H2>"
text+="""<image src="img/Graph.png" align=center> <br> <br> The longest shortest path between two summits is in red."""
text+="</BODY></HTML>"
Name='result'+'.html'
fichier=open(Name,'w')
fichier.write(text)
fichier.close()



























