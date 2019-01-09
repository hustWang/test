# -*- coding:utf-8 -*-

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

#devstack实例展示部分
encoder.FLOAT_REPR = lambda o: format(o, '.3f')

data_instance = []
with open("e:/20181221.json") as f:
    for line in f.readlines():
        dic = json.loads(line)
        data_instance.append(dic)
        
def instance_update(self,context):
    scene = bpy.context.scene
    data1 = []
    if scene.MyEnum == '0':

        with open("e:/20181221.json") as in_file:
            for line in in_file.readlines():     
                edges1 = json.loads(line)        
                data1.append(edges1)
                edges1 = data1      
        available_nodes = set(e["memory_mb"] for e in edges1) | set(e["display_name"] for e in edges1)
       
        labels = list(available_nodes)
    
        Edges = []
        def generate_edges(*args, **kw):
            if kw['memory_mb'] in args:
                i = args.index(kw["memory_mb"])
            if kw['display_name'] in args:
                j = args.index(kw["display_name"])
            tup = (i, j)
            Edges.append(tup)
        for k in range(len(edges1)):
            generate_edges(*labels, **edges1[k])
        G = ig.Graph(Edges, directed = False)
        
        layt = G.layout("kk", dim = 3)
        layt.center()
        master_nodes = {}
        for i in range(len(labels)):
            master_nodes[labels[i]] = {"location":[j*10 for j in layt[i]]}

        json_str = dumps({"edges": edges1, "nodes": master_nodes})
        network = json.loads(json_str)

        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all()
        bpy.ops.object.delete()

        draw_network(network)
    elif scene.MyEnum == '1':
        with open("e:/20190107.json") as in_file:
            for line in in_file.readlines():
                edges = json.loads(line)
            
                data1.append(edges)
                edges = data1
                
        available_nodes = set(e["memory_mb"] for e in edges) | set(e["display_name"] for e in edges)
        labels = list(available_nodes)
    
        Edges = []
        def generate_edges(*args, **kw):
            if kw['memory_mb'] in args:
                i = args.index(kw["memory_mb"])
            if kw['display_name'] in args:
                j = args.index(kw["display_name"])
            tup = (i, j)
            Edges.append(tup)
            
        for k in range(len(edges)):
            generate_edges(*labels, **edges[k])
        G = ig.Graph(Edges, directed = False)
        layt = G.layout("kk", dim = 3)
        layt.center()
        master_nodes = {}
        for i in range(len(labels)):
            master_nodes[labels[i]] = {"location":[j*10 for j in layt[i]]}

        json_str = dumps({"edges": edges, "nodes": master_nodes})
        network = json.loads(json_str)

        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all()
        bpy.ops.object.delete()

        draw_network(network)
    else:
        with open("e:/20190106.json") as in_file:
            for line in in_file.readlines():
                edges = json.loads(line)
      
                data1.append(edges)
                edges = data1

        available_nodes = set(e["memory_mb"] for e in edges) | set(e["display_name"] for e in edges)
        labels = list(available_nodes)
    
        Edges = []
        def generate_edges(*args, **kw):
            if kw['memory_mb'] in args:
                i = args.index(kw["memory_mb"])
            if kw['display_name'] in args:
                j = args.index(kw["display_name"])
            tup = (i, j)
            Edges.append(tup)
            
        for k in range(len(edges)):
            generate_edges(*labels, **edges[k])
        G = ig.Graph(Edges, directed = False)
        layt = G.layout("kk", dim = 3)
        layt.center()
        master_nodes = {}
        for i in range(len(labels)):
            master_nodes[labels[i]] = {"location":[j*10 for j in layt[i]]}

        json_str = dumps({"edges": edges, "nodes": master_nodes})
        network = json.loads(json_str)

        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all()
        bpy.ops.object.delete()

        draw_network(network)
        
def RL_instance(self,context):
    scene = bpy.context.scene
    if scene.MyBool_Ins == True:
        scene.MyBool_RL = False
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all()
        bpy.ops.object.delete()
        # bpy.ops.mesh.select_all(action='DESELECT')
        # bpy.ops.mesh.select_all()
        # bpy.ops.mesh.delete()

def RL_resourse(self,context):
    scene = bpy.context.scene
    if scene.MyBool_RL == True:
        scene.MyBool_Ins = False
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all()
        bpy.ops.object.delete()
        
    

def initSceneProperties(scn):
 
    bpy.types.Scene.MyBool_RL = BoolProperty(
        name = "Boolean", 
        description = "True or False?",
        update = RL_resourse)
    
    bpy.types.Scene.MyBool_Ins = BoolProperty(
        name = "Boolean", 
        description = "True or False?",
        update = RL_instance)
     
        
    bpy.types.Scene.MyBool_NT = BoolProperty(
        name = "Boolean", 
        description = "True or False?")
        
    bpy.types.Scene.MyBool_Gra = BoolProperty(
        name = "Boolean", 
        description = "True or False?")
    
 
    bpy.types.Scene.MyEnum = EnumProperty(
        items = [("0","全部实例","All instances"),
                 ("1","运行实例","running instances"),
                 ("2","错误实例","error instances")],
        name = "实例选项",
        update = instance_update)
    scn['MyEnum'] = 0
 
initSceneProperties(bpy.context.scene)

# blender add-on部分——tool shelf中的Drawing Line部分
bl_info = {
    "name": "Simple Line Drawing",
    "author": "lwm",
    "location": "View3D > Tools > Drawing",
    "version": (1, 0, 0),
    "blender": (2, 7, 9),
    "description": "Minimal add-on for line drawing"
}

#color and font
rgb_label = (1, 0.8, 0.1, 1.0)
font_size = 16
font_id = 0

def gl_pts(context, v):
    return view3d_utils.location_3d_to_region_2d(context.region, context.space_data.region_3d, v)

def draw_name(context, ob, rgb_label, fsize):
    a = gl_pts(context, ob.location)
    bgl.glColor4f(rgb_label[0], rgb_label[1], rgb_label[2], rgb_label[3])
    draw_text(a, ob.name, fsize)

def draw_text(v, display_text, fsize, font_id=0):
    if v:
        blf.size(font_id, font_size, 72)
        blf.position(font_id, v[0], v[1], 0)
        blf.draw(font_id, display_text)

    return

def draw_line(v1, v2):
    if v1 and v2:
        bgl.glBegin(bgl.GL_LINES)
        bgl.glVertex2f(*v1)
        bgl.glVertex2f(*v2)
        bgl.glEnd()

def generate_edges(*args, **kw):
        if kw['memory_mb'] in args:
            i = args.index(kw["memory_mb"])
        if kw['display_name'] in args:
            j = args.index(kw["display_name"])
        tup = (i, j)
        Edges.append(tup)        
        
def draw_main(context):
    scene = context.scene

    rgb_line = (0.173, 0.545, 1.0, 1.0)
    rgb_label = (0.1, 0.1, 0.1, 1.0)
    fsize = 16

    bgl.glEnable(bgl.GL_BLEND)
    bgl.glLineWidth(1)
    bgl.glColor4f(*rgb_line)

    for edge in network["edges"]:
        # 通过遍历获取源和目标的位置
        source_name = edge["memory_mb"]
        target_name = edge["display_name"]
        source_obj = bpy.data.objects[source_name]
        target_obj = bpy.data.objects[target_name]
        # source_obj = target_obj.parent
        v1 = gl_pts(context, source_obj.matrix_world.to_translation())
        v2 = gl_pts(context, target_obj.matrix_world.to_translation())
        draw_line(v1, v2)

    # Store reference to active object
    ob = context.object
    #print(ob)
    
    if scene.gl_display_names:
        draw_name(context, ob, rgb_label, fsize)

    bgl.glLineWidth(1)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)

class glrun(bpy.types.Operator):
    bl_idname = 'glinfo.glrun'
    bl_label = 'Display lines'
    bl_description = 'Display lines between objs'

    _handle = None

    @staticmethod
    def handle_add(context):
        if glrun._handle is None:
            glrun._handle = bpy.types.SpaceView3D.draw_handler_add(draw_main, (context,), 'WINDOW', 'POST_PIXEL')
            context.window_manager.run_opengl = True
            
    @staticmethod
    def handle_remove(context):
        if glrun._handle is not None:
            bpy.types.SpaceView3D.draw_handler_remove(glrun._handle, 'WINDOW')
            glrun._handle = None 
            context.window_manager.run_opengl = False

    def execute(self, context):
        if context.area.type == 'VIEW_3D':
            if context.window_manager.run_opengl == False:
                self.handle_add(context)
                context.area.tag_redraw()
            else:
                self.handle_remove(context)
                context.area.tag_redraw()
            return {'FINISHED'}
        else:
            print('3D Viewport is not found')
            return {'CANCELLED'}
     
class hello_OP(bpy.types.Operator):
    bl_idname = 'hello.glpanel'
    bl_label = 'Instance_d'
    
    def execute(self,execute):
        print("1")
     
class glpanel(bpy.types.Panel):
    bl_idname = 'glinfo.glpanel'
    bl_label = 'Instance_display'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Show'

    def draw(self, context):
        lay = self.layout
        scn = context.scene
        box = lay.box()

        if context.window_manager.run_opengl is False:
            icon = 'PLAY'
            txt = 'Display'
        else:
            icon = 'PAUSE'
            txt = 'Hide'
        box.operator('glinfo.glrun', text=txt, icon=icon)
        box.prop(scn, "gl_display_names", toggle=True, icon="OUTLINER_OB_FONT")
      
        layout = self.layout
        row = lay.row()
        #根据bpy.context.scene的属性确定选项
        scn = context.scene
        layout.prop(scn, 'MyBool_RL',text = '系统资源详情')
        layout.prop(scn, 'MyBool_Ins',text = '实例详情')
        layout.prop(scn, 'MyEnum')

        row = lay.row()
        name_ob = context.object.name
        for instance in data_instance:
  
            if instance['display_name']==name_ob:
                box = lay.box()
                box.label("hostname : "+instance['hostname'])
                box.label("memory_mb : "+str(instance['memory_mb']))
                box.label("updated_at : "+instance['updated_at'])
                row = lay.row() 
        
    @classmethod
    def register(cls):
        bpy.types.Scene.gl_display_names = bpy.props.BoolProperty(
            name="Names",
            description="Display names for selected meshes.",
            default=True,
        )
        
        print('register {}'.format(cls.bl_idname))

    @classmethod
    def unregister(cls):
        #del bpy.types.Scene.gl_display_names
        del bpy.types.Scene.hello_rl
        print('unregister {}'.format(cls.bl_idname))


# blender add-on部分——tool shelf中的Dynamic display
bl_info2 = {
    "name": "Dynamic display",
    "author": "ksm",
    "location": "View3D > Tools > Dynamic",
    "version": (1, 0, 0),
    "blender": (2, 7, 9),
    "description": "Display memory changes dynamicly"
}

# class displayPanel(bpy.types.Panel):
    # bl_idname = 'process.DynamicDisplay'
    # bl_label = 'Dynamic display'
    # bl_space_type = 'VIEW_3D'
    # bl_region_type = 'TOOLS'
    # bl_category = 'Dynamic'

    # def draw(self, context):
        # col = self.layout.column(align=True)
        # col.label(text="Control:")
        # row = col.row(align=True)
        # row.operator("process.prev", text="Prev")
        # row.operator("process.next", text="Next")

    # @classmethod
    # def register(cls):
        # print('register {}'.format(cls.bl_idname))

    # @classmethod
    # def unregister(cls):
        # print('unregister {}'.format(cls.bl_idname))



# 3Dview中UI地区的菜单
class UIPanel(bpy.types.Panel):
    bl_idname = "UIPanel.process"
    bl_label = "Process Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
 
    def draw(self, context):
        # self.layout.operator("getprocess.name", text='Process Name')
        self.layout.label(text = "Process name:")
        #txt = bpy.context.selected_objects[0].name
        #self.layout.label(text = txt)
        ob = context.active_object
        row = self.layout.row()
        row.prop(ob, "name", text="")
    
    @classmethod
    def register(cls):
        print('register {}'.format(cls.bl_idname))

    @classmethod
    def unregister(cls):
        print('unregister {}'.format(cls.bl_idname))
 
def register():
    
    bpy.utils.register_class(glrun)
    bpy.utils.register_class(hello_OP)
    bpy.utils.register_class(glpanel)
    # bpy.utils.register_class(displayPanel)
 
    bpy.utils.register_class(UIPanel)
    wm = bpy.types.WindowManager
    wm.run_opengl = bpy.props.BoolProperty(default=False)
    print('{} register complete'.format(bl_info.get('name')))

def unregister():
  
    bpy.utils.unregister_class(glpanel)
    bpy.utils.register_class(hello_OP)
    bpy.utils.unregister_class(glrun)
    # bpy.utils.unregister_class(displayPanel)
   
    bpy.utils.unregister_class(UIPanel)
    wm = bpy.types.WindowManager
    if 'run_opengl' in wm:
        del wm[p]
    print('{} unregister complete'.format(bl_info.get('name')))

'''
输出json格式内容
'''

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


# 颜色RGB指定
colors = { "red": (255, 0, 0), "orange": (255, 108, 0),
           "yellow": (204, 255, 0), "green": (0, 255, 90),
           "blue": (36, 182, 218), "indigo": (0, 18, 255),  
           "purple": (216, 0, 255), "gray": (188, 188, 188)}
          

# 将颜色标准化为[0,1]之间，并且设定materials
for key, value in colors.items():
    value = [x / 255.0 for x in value]
    bpy.data.materials.new(name=key)
    bpy.data.materials[key].diffuse_color = value
    bpy.data.materials[key].specular_intensity = 0.5

# 画出网图的主函数
def draw_network(network):
    """ Takes assembled network/molecule data and draws to blender """
    # 增加原始网格
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.mesh.primitive_cone_add(vertices=3, depth=1.414213)
    cube = bpy.context.object

    # 保存所有节点和边的引用
    shapes = []

    # 生成结点
    for key, node in network["nodes"].items():

        # 结点的颜色设定
        col = node.get("color", choice(list(colors.keys())))

        # 复制原始网格并且生成新节点
        node_cube = cube.copy()
        node_cube.data = cube.data.copy()
        node_cube.name = key
        node_cube.location = node["location"]
        node_cube.active_material = bpy.data.materials[col]
        bpy.context.scene.objects.link(node_cube)
        shapes.append(node_cube)
    
    for edge in network["edges"]:
        # 通过遍历获取源和目标的位置
        source_name = edge["memory_mb"]
        target_name = edge["display_name"]
        source_obj = bpy.data.objects[source_name]
        target_obj = bpy.data.objects[target_name]
        # 设置父子关系
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = source_obj
        target_obj.select = True
        try:
            bpy.ops.object.parent_set()
        except:
            pass
   
    # 删除原始网格
    bpy.ops.object.select_all(action='DESELECT')
    cube.select = True

    # 删除启动时的小方块
    if "Cube" in bpy.data.objects.keys():
        bpy.data.objects.get("Cube").select = True
    bpy.ops.object.delete()

    # 将整个物体居中对齐
    bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="MEDIAN")

    # 刷新场景
    bpy.context.scene.update()

data0 = []
if __name__ == "__main__":
    try:
        with open("e:/20190107.json") as in_file:
            for line in in_file.readlines():
                edges = json.loads(line)
                data0.append(edges)
                edges = data0
    except IOError:
        with open(sys.argv[-1]) as in_file:
            for line in in_file.readlines():
                edges = json.loads(line)
                data0.append(edges)
                edges = data0

    available_nodes = set(e["memory_mb"] for e in edges) | set(e["display_name"] for e in edges)
    labels = list(available_nodes)
    
    Edges = []
    
    for k in range(len(edges)):
        generate_edges(*labels, **edges[k])
    G = ig.Graph(Edges, directed = False)
    layt = G.layout("kk", dim = 3)
    layt.center()
    master_nodes = {}
    for i in range(len(labels)):
        master_nodes[labels[i]] = {"location":[j*10 for j in layt[i]]}

    json_str = dumps({"edges": edges, "nodes": master_nodes})
    network = json.loads(json_str)

    draw_network(network)
    

    
    try:
        unregister()
    except Exception as e:
        print(e)
        pass
    finally:
        register()
