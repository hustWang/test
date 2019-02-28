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

encoder.FLOAT_REPR = lambda o: format(o, '.3f')
#存放实例信息
data_instance = []
#存放镜像信息
data_image = []

with open("json/instance_info.json") as f:
    for line in f.readlines():
        dic = json.loads(line)
        data_instance.append(dic)
        
with open("json/image_info.json") as f1:
    for line1 in f1.readlines():
        dic1 = json.loads(line1)
        data_image.append(dic1)

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
        if kw['images_name'] in args:
            i = args.index(kw["images_name"])
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
        source_name = edge["images_name"]
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
        
def instance_update(self,context):
    #切换场景，用于多场景展示不同的内容
    bpy.context.scene.layers[0] = False
    bpy.context.scene.layers[1] = True
    scene = bpy.context.scene
    data1 = []
    if scene.MyEnum == '0':

        with open("json/instance_info.json") as in_file:
            for line in in_file.readlines():     
                edges1 = json.loads(line)        
                data1.append(edges1)
                edges1 = data1      
        available_nodes = set(e["images_name"] for e in edges1) | set(e["display_name"] for e in edges1)
       
        labels = list(available_nodes)
    
        Edges = []
        def generate_edges(*args, **kw):
            if kw['images_name'] in args:
                i = args.index(kw["images_name"])
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
        with open("json/instance_info.json") as in_file:
            for line in in_file.readlines():
                edges = json.loads(line)
            
                data1.append(edges)
                edges = data1
                
        available_nodes = set(e["images_name"] for e in edges) | set(e["display_name"] for e in edges)
        labels = list(available_nodes)
    
        Edges = []
        def generate_edges(*args, **kw):
            if kw['images_name'] in args:
                i = args.index(kw["images_name"])
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
        with open("json/instance_info.json") as in_file:
            for line in in_file.readlines():
                edges = json.loads(line)
      
                data1.append(edges)
                edges = data1

        available_nodes = set(e["images_name"] for e in edges) | set(e["display_name"] for e in edges)
        labels = list(available_nodes)
    
        Edges = []
        def generate_edges(*args, **kw):
            if kw['images_name'] in args:
                i = args.index(kw["images_name"])
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
    bpy.context.scene.layers[0] = False
    bpy.context.scene.layers[1] = True
    scene = bpy.context.scene
    if scene.MyBool_Ins == True:

        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all()
        bpy.ops.object.delete() 

def initSceneProperties(scn):

    bpy.types.Scene.cpu_rs = bpy.props.IntProperty(
            name = "CPU RS",
            description = "Sample integer property to print to user",
            default = 40,
            min = 0,
            max = 100,
            subtype = "PERCENTAGE"
            )  
            
    bpy.types.Scene.local_gb_rs = bpy.props.IntProperty(
            name = "local_gb rs",
            description = "Sample integer property to print to user",
            default = 40,
            min = 0,
            max = 100,
            subtype = "PERCENTAGE"
            ) 
            
    bpy.types.Scene.memory_rs = bpy.props.IntProperty(
            name = "memory rs",
            description = "Sample integer property to print to user",
            default = 40,
            min = 0,
            max = 100,
            subtype = "PERCENTAGE"
            ) 

    bpy.types.Scene.MyBool_RL = BoolProperty(
        name = "Boolean", 
        description = "True or False?")
    
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
                 ("1","运行的实例","running instances"),
                 ("2","停止的实例","stopped instances")],
        name = "选项",
        update = instance_update)
    scn['MyEnum'] = 0
 
initSceneProperties(bpy.context.scene)

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
    
class glpanel(bpy.types.Panel):
    bl_idname = 'glinfo.glpanel'
    bl_label = '系统实例详情'
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
        #layout.prop(scn, 'MyBool_RL',text = '系统资源详情')
        # layout.prop(scn, 'MyBool_Ins',text = '实例详情')
        layout.prop(scn, 'MyEnum')
        
        row = lay.row()
        #name_ob = context.object.name
        # name_ob = context.scene.objects.active.name
        name_ob = context.selected_objects[0].name
        # name_ob = context.active_object.name
        for instance in data_instance:
  
            if instance['display_name']==name_ob:
                lay.label("实例详情 ：")
                box = lay.box()
                box.label("display_name : "+instance['display_name'])
                box.label("images_name : "+instance['images_name'])
                box.label("vm_state : "+instance['vm_state'])
                box.label("host : "+instance['host'])
                box.label("vcpus : "+str(instance['vcpus']))
                box.label("memory_mb : "+str(instance['memory_mb'])+"MB")
                box.label("root_gb : "+str(instance['root_gb'])+"GB")
                box.label("availability_zone : "+instance['availability_zone'])
                box.label("updated_at : "+instance['updated_at'])
                box.label("launched_at : "+instance['launched_at'])
                box.label("created_at : "+instance['created_at'])
                row = lay.row()
                
        for instance1 in data_image:
            if instance1["images_name"]==name_ob:
                lay.label("实例镜像详情 ：")
                box = lay.box()
                box.label("images_name : "+instance1['images_name'])
                box.label("status : "+instance['status'])
                box.label("images_create : "+str(instance1['images_create']))
                box.label("images_update : "+str(instance1['images_update']))
                box.label("visibility : "+instance1['visibility'])
                box.label("size : "+str(instance1['size']/1024/1024)+"MB")
                box.label("disk_format : "+instance1['disk_format'])
                box.label("container_format : "+instance1['container_format'])
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

class glpanel_rs(bpy.types.Panel):
    bl_idname = 'glinfo.rspanel'
    #bl_label = 'Resourse_display'
    bl_label = '系统资源使用详情'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Show'
    
    def draw(self, context):
        layout = self.layout
        
        scene = context.scene
        rd = scene.render
       
        split = layout.split()
        col = split.column()
        sub = col.column(align=True)
        sub.label(text="CPU 使用量: "+"("+"%s"%(num)+" / "+"%s"%(vcpus)+")" )
        sub.prop(context.scene, "cpu_rs", text="",slider = True)
        #print(bpy.context.scene.cpu_rs)
        #使用量变高时，颜色可以想办法来设定不同的样式
        #local_gb_rs = 0.9, 0, 0
        sub.label(text="磁盘 使用量: "+"("+"%s"%(local_gb_used)+"GB"+" / "+"%s"%(local_gb)+"GB"+")")
        sub.prop(context.scene, "local_gb_rs", text="",slider = True)
        
        sub.label(text="内存 使用量: "+"("+"%s"%(memory_mb_used)+"MB"+" / "+"%s"%(memory_mb)+"MB"+")")
        sub.prop(context.scene, "memory_rs", text="",slider = True)
        
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
    bpy.utils.register_class(glpanel)
    bpy.utils.register_class(glpanel_rs)
    bpy.utils.register_class(UIPanel)
    wm = bpy.types.WindowManager
    wm.run_opengl = bpy.props.BoolProperty(default=False)
    # print('{} register complete'.format(bl_info.get('name')))

def unregister():
  
    bpy.utils.unregister_class(glpanel)
    bpy.utils.unregister_class(glpanel_rs)
    bpy.utils.unregister_class(glrun)   
    bpy.utils.unregister_class(UIPanel)
    wm = bpy.types.WindowManager
    if 'run_opengl' in wm:
        del wm[p]
    # print('{} unregister complete'.format(bl_info.get('name')))

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
    # bpy.ops.mesh.primitive_cone_add(vertices=3, depth=1.414213)
    bpy.ops.mesh.primitive_uv_sphere_add()
    cube = bpy.context.scene.objects['Sphere']

    # 保存所有节点和边的引用
    shapes = []

    # 生成结点
    for key, node in network["nodes"].items():
     
        # 结点的颜色设定
        # col = node.get("color", choice(list(colors.keys())))

        # 复制原始网格并且生成新节点
        node_cube = cube.copy()
        node_cube.data = cube.data.copy()
        node_cube.name = key

        for name_instance in data_instance:
            if name_instance["display_name"]==key:
                node_cube.scale = (0.5,0.5,0.5)
                if name_instance["vm_state"]=="active":
                    node_cube.active_material = bpy.data.materials["green"]
                elif name_instance["vm_state"]=="stopped":
                    node_cube.active_material = bpy.data.materials["gray"]
            else:
                for name_instance in data_image:
                    if name_instance["images_name"]==key:
                        node_cube.active_material = bpy.data.materials["blue"]
                    elif name_instance["status"]=="stopped":
                        node_cube.active_material = bpy.data.materials["red"]
                
        node_cube.location = node["location"]
        # node_cube.active_material = bpy.data.materials[col]
        bpy.context.scene.objects.link(node_cube)
        shapes.append(node_cube)
    
    for edge in network["edges"]:
        # 通过遍历获取源和目标的位置
        source_name = edge["images_name"]
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
    bpy.context.scene.layers[0] = False
    bpy.context.scene.layers[1] = True

    data_s=[]
    with open("json/instance_info.json") as in_file:
            for line in in_file.readlines():     
                edges1 = json.loads(line)        
                data_s.append(edges1)
                edges1 = data_s      
    available_nodes = set(e["images_name"] for e in edges1) | set(e["display_name"] for e in edges1)       
    labels = list(available_nodes)
    
    Edges = []
    def generate_edges(*args, **kw):
        if kw['images_name'] in args:
            i = args.index(kw["images_name"])
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
        
    with open("json/20181213.json") as f:
        tmp = json.load(f)
    
    vcpus = tmp['vcpus']
    num = tmp['running_vms']
    memory_mb = tmp['memory_mb'] 
    memory_mb_used = tmp['memory_mb_used']
    local_gb = tmp['local_gb']
    local_gb_used = tmp['local_gb_used']
        
    bpy.context.scene.cpu_rs = num/vcpus*100
    bpy.context.scene.local_gb_rs = local_gb_used/local_gb*100
    bpy.context.scene.memory_rs = memory_mb_used/memory_mb*100
    
    try:
        unregister()
    except Exception as e:
        print(e)
        pass
    finally:
        register()