import sys
sys.path.append('..')
sys.path.append('/usr/lib/graphviz/python/')
sys.path.append('/usr/lib64/graphviz/python/')
import gv

from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import breadth_first_search
from pygraph.readwrite.dot import write

gr = digraph()

f = open('../../java/category_cooking.txt', 'r')

line = f.readline()
category = line.split(":")
children = category[1]
childarray = children.split(" ")
gr.add_nodes([category[0]])
gr.add_nodes(childarray)

for singlechild in childarray:
	gr.add_edge((category[0], singlechild))

dot = write(gr)
gvv = gv.readstring(dot)
gv.layout(gvv, 'dot')
gv.render(gvv, 'png', 'cooking.png') 	


