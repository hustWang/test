import json
import os
import re
import sys
from copy import deepcopy
from itertools import combinations, repeat, takewhile
from json import encoder
from math import sqrt
from operator import add
from random import choice, uniform

import numpy as np
import igraph as ig

import bgl
import blf
import bpy
from bpy.props import *
from bpy_extras import view3d_utils
from bpy.types import NodeTree, Node, NodeSocket

global he

def dumps(obj):
    """Outputs json with formatting edits + object handling."""
    return json.dumps(obj, indent=4, sort_keys=True, cls=CustomEncoder)
class CustomEncoder(json.JSONEncoder):

    def encode(self, obj):
        """Fired for every object."""
        s = super(CustomEncoder, self).encode(obj)
        # If uncompressed, postprocess for formatting
        if len(s.splitlines()) > 1:
            s = self.postprocess(s)
        return s

    def postprocess(self, json_string):
        """Displays each entry on its own line."""
        is_compressing, is_hash, compressed, spaces = False, False, [], 0
        for row in json_string.split("\n"):
            if is_compressing:
                if (row[:spaces + 5] == " " * (spaces + 4) +
                        ("\"" if is_hash else "{")):
                    compressed.append(row.rstrip())
                elif (len(row) > spaces and row[:spaces] == " " * spaces and
                        re.match("[\]\}],?", row[spaces:].rstrip())):
                    compressed.append(row.rstrip())
                    is_compressing = False
                else:
                    compressed[-1] += " " + row.strip()
            else:
                compressed.append(row.rstrip())
                if any(a in row for a in ["edges", "nodes"]):
                    # Fix to handle issues that arise with empty lists
                    if "[]" in row:
                        continue
                    spaces = sum(1 for _ in takewhile(str.isspace, row))
                    is_compressing, is_hash = True, "{" in row
        return "\n".join(compressed)

def generate_edges(*args, **kw):
    if kw['r_name'] in args:
        i = args.index(kw["r_name"])
    if kw['net_name'] in args:
        j = args.index(kw["net_name"])
    tup = (i, j)
    Edges.append(tup)
        
def generate_edges2(*args, **kw):
    if kw["display_name"] in args:
        j = args.index(kw["display_name"])
    if kw['net_name'] in args:
        i = args.index(kw["net_name"])
    tup = (i, j)
    Edges.append(tup)

class VadCustomTree(NodeTree):
    '''A vad node tree type that will show up in the node editor header'''
    bl_idname = 'VadTreeType'
    bl_label = 'Vad Node Tree'
    bl_icon = 'NODETREE'

# Vad socket type
class VadCustomSocket(NodeSocket):
    '''Vad node socket type'''
    bl_idname = 'VadSocketType'
    bl_label = 'Vad Node Socket'

    def draw(self, context, layout, node, text):
        layout.label(text)

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


class VadCustomTreeNode:
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'VadTreeType'


class VadCustomNode(Node, VadCustomTreeNode):
    '''A custom node'''
    bl_idname = 'VadNodeType'
    bl_label = 'Vad Node'
    bl_icon = 'SOUND'
    
    string_name = bpy.props.StringProperty()
    
    index = bpy.props.IntProperty(default = 0)
    
    def init(self, context):
        self.inputs.new('VadSocketType', " ")
      
        self.outputs.new('NodeSocketColor', " ")
    
    def copy(self, node):
        print("Copying from node ", node)
    
    def free(self):
        print("Removing node ", self, ", Goodbye!")
    
    def draw_buttons(self, context, layout):
        layout.label(self.string_name)
    
    def draw_label(self):
        return "vad node"

class OBJECT_OT_HelloButton(bpy.types.Operator):
    bl_idname = "hello.hello"
    bl_label = "Say Hello"      
    
    def execute(self, context):
        print("hhh")

import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem

class VadNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'VadTreeType'

node_categories = [
    # identifier, label, items list
    VadNodeCategory("SOMENODES", "Some Nodes", items=[
        # our basic node
        NodeItem("VadNodeType"),
        ]),
    ]

def register():
    bpy.utils.register_class(VadCustomTree)
    bpy.utils.register_class(VadCustomSocket)
    bpy.utils.register_class(VadCustomNode)
    bpy.utils.register_class(OBJECT_OT_HelloButton)

    nodeitems_utils.register_node_categories("CUSTOM_NODES", node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories("CUSTOM_NODES")

    bpy.utils.unregister_class(VadCustomTree)
    bpy.utils.unregister_class(VadCustomSocket)
    bpy.utils.unregister_class(VadCustomNode)
    bpy.utils.unregister_class(OBJECT_OT_HelloButton)

    
data0  = []
data1 = []
if __name__ == "__main__":
    register()
    Edges=[]
    with open("e:/20190116_1.json") as in_file:
        for line in in_file.readlines():
            edges1 = json.loads(line)
            data0.append(edges1)
    with open("e:/20190116_2.json") as in_file:
        for line in in_file.readlines():
            edges2 = json.loads(line)
            data1.append(edges2)
            
    edges = data0
    edges1 = data1
   
    available_nodes = set(e['r_name'] for e in edges) | set(e["net_name"] for e in edges) | set(e["display_name"] for e in data1)

    labels = list(available_nodes)
    
    
    for k in range(len(edges)):
        generate_edges(*labels, **edges[k])
    
    for k in range(len(edges1)):
        generate_edges2(*labels, **edges1[k])
    
    G = ig.Graph(Edges, directed = False)

    layt = G.layout("tree")
    layt.center()
    master_nodes = {}
    for i in range(len(labels)):
        master_nodes[labels[i]] = {"location":[j*200 for j in layt[i]]}
        tmp = master_nodes[labels[i]]["location"][0]
        master_nodes[labels[i]]["location"][0] = master_nodes[labels[i]]["location"][1]
        master_nodes[labels[i]]["location"][1] = tmp
     
    json_str = dumps({"edges": edges+edges1, "nodes": master_nodes})
    network = json.loads(json_str)
   
    bpy.context.scene.use_nodes = True
    tree = bpy.context.scene.node_tree

    # clear default nodes
    for node in tree.nodes:
        tree.nodes.remove(node)
    
    for vad_label in labels:
        vad_node = tree.nodes.new(type='VadNodeType')
        vad_node.location = tuple(network["nodes"][vad_label]["location"])
        vad_node.name = vad_label
        vad_node.label = vad_label
        vad_node.inputs[0].link_limit = 4095
        #vad_node.inputs.new('VadSocketType', " ")
     
    links = tree.links
    
    for e in edges:
        source_r = tree.nodes[e["r_name"]]
        source_net = tree.nodes[e["net_name"]]
   
        if e["net_name"]=="public":
            links.new(source_net.outputs[0], source_r.inputs[0])
        else:
            links.new(source_r.outputs[0], source_net.inputs[0])
        
    for e in edges1:
        source = tree.nodes[e["net_name"]]
        target = tree.nodes[e["display_name"]]
        links.new(source.outputs[0], target.inputs[0])
        
