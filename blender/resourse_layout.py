import json
import bpy
import bmesh
import time
from datetime import datetime 
from bpy.props import *

class CreateOperator01(bpy.types.Operator):
    bpy.ops.object.delete(use_global=False)
    #创建物体01
    cylinder01 = bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, 
                view_align=False, enter_editmode=False, location=(0, 0, 0), 
                layers=(True, False, False, False, False, False, False, False, 
                False, False, False, False, False, False, False, False, False, 
                False, False, False))
    bpy.ops.transform.resize(value=(0.06, 0.06, 0.06), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    bpy.ops.transform.translate(value=(-4, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.0945771, 0.8, 0.115851)
    #创建物体02
    cylinder02 = bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, 
                view_align=False, enter_editmode=False, location=(0, 0, 0), 
                layers=(True, False, False, False, False, False, False, False, 
                False, False, False, False, False, False, False, False, False, 
                False, False, False))
    bpy.ops.transform.resize(value=(0.06, 0.06, 0.06), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.0945771, 0.8, 0.115851)
    #创建物体03
    cylinder03 = bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, 
                view_align=False, enter_editmode=False, location=(0, 0, 0), 
                layers=(True, False, False, False, False, False, False, False, 
                False, False, False, False, False, False, False, False, False, 
                False, False, False))
    bpy.ops.transform.resize(value=(0.06, 0.06, 0.06), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.0945771, 0.8, 0.115851)
    
    #移动物体到相应位置01
    bpy.data.objects['Cylinder'].select=False
    bpy.data.objects['Cylinder.001'].select=True
    bpy.data.objects['Cylinder.002'].select=False
    bpy.ops.transform.translate(value=(-4, -4, 0))
    #移动物体到相应位置02
    bpy.data.objects['Cylinder.001'].select=False
    bpy.data.objects['Cylinder.002'].select=True
    bpy.ops.transform.translate(value=(-4, 4, 0))
    
    #平面01
    plane01 = bpy.ops.mesh.primitive_plane_add(radius=1)
    bpy.data.objects['Plane'].select=True
    bpy.ops.transform.resize(value=(0.5, 0.5, 1), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    bpy.ops.transform.translate(value=(-4.5, 0.5, 0.1), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

    #写成函数？    
    bpy.ops.object.mode_set(mode='EDIT') 

    bpy.ops.mesh.select_mode(type = "VERT")
    p1 = bmesh.from_edit_mesh(bpy.context.object.data)
    bpy.ops.mesh.select_all(action = "DESELECT")
    
    p1.verts.ensure_lookup_table()
    p1.verts[3].select = True
    bpy.ops.mesh.dissolve_verts()
    p1.verts.ensure_lookup_table()
    p1.verts[2].select = True
    bpy.ops.mesh.dissolve_verts()
    
    p1.verts.ensure_lookup_table()
    p1.verts[1].select = True
    
    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D': 
            ctx = bpy.context.copy() 
            ctx['area'] = area 
            ctx['region'] = area.regions[-1] 
            bpy.ops.view3d.snap_cursor_to_selected(ctx) 
            break 
      
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

    bpy.ops.object.modifier_add(type='SCREW')
    bpy.context.object.modifiers["Screw"].steps = 360
    #添加材质
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.0364558, 0.407289, 0.8)
    
    
    #读取json文件，传入blender
    with open("e:/20181213.json") as f:
        tmp = json.load(f)
    
    vcpus = tmp['vcpus']
    num = tmp['running_vms']
    memory_mb = tmp['memory_mb'] 
    memory_mb_used = tmp['memory_mb_used']
    local_gb = tmp['local_gb']
    local_gb_used = tmp['local_gb_used']
    
    bpy.context.object.modifiers["Screw"].angle = 6.28319*(memory_mb_used/memory_mb)
    
    bpy.data.objects['Plane'].select=False
    #平面00
    plane01 = bpy.ops.mesh.primitive_plane_add(radius=1)
    bpy.data.objects['Plane.001'].select=True
    bpy.ops.transform.resize(value=(0.5, 0.5, 1), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    bpy.ops.transform.translate(value=(-0.5,-3.5, 0.1), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    
    bpy.ops.object.mode_set(mode='EDIT') 

    bpy.ops.mesh.select_mode(type = "VERT")
    p1 = bmesh.from_edit_mesh(bpy.context.object.data)
    bpy.ops.mesh.select_all(action = "DESELECT")
    
    p1.verts.ensure_lookup_table()
    p1.verts[3].select = True
    bpy.ops.mesh.dissolve_verts()
    p1.verts.ensure_lookup_table()
    p1.verts[2].select = True
    bpy.ops.mesh.dissolve_verts()
    
    p1.verts.ensure_lookup_table()
    p1.verts[1].select = True
    
    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D': 
            ctx = bpy.context.copy() 
            ctx['area'] = area 
            ctx['region'] = area.regions[-1] 
            bpy.ops.view3d.snap_cursor_to_selected(ctx) 
            break 
      
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

    bpy.ops.object.modifier_add(type='SCREW')
    bpy.context.object.modifiers["Screw"].steps = 360
    #添加材质
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.0364558, 0.407289, 0.8)
    
    with open("e:/20181213.json") as f:
        tmp = json.load(f)
    
    vcpus = tmp['vcpus']
    num = tmp['running_vms']
    memory_mb = tmp['memory_mb'] 
    memory_mb_used = tmp['memory_mb_used']
    local_gb = tmp['local_gb']
    local_gb_used = tmp['local_gb_used']
    
    bpy.context.object.modifiers["Screw"].angle = 6.28319*(num/vcpus)
    bpy.data.objects['Plane.001'].select=False
    
    
    
    #平面02
    plane01 = bpy.ops.mesh.primitive_plane_add(radius=1)
    bpy.data.objects['Plane.002'].select=True
    bpy.ops.transform.resize(value=(0.5, 0.5, 1), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    bpy.ops.transform.translate(value=(-0.5, 8.5, 0.1), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    
    bpy.ops.object.mode_set(mode='EDIT') 

    bpy.ops.mesh.select_mode(type = "VERT")
    p1 = bmesh.from_edit_mesh(bpy.context.object.data)
    bpy.ops.mesh.select_all(action = "DESELECT")
    
    p1.verts.ensure_lookup_table()
    p1.verts[3].select = True
    bpy.ops.mesh.dissolve_verts()
    p1.verts.ensure_lookup_table()
    p1.verts[2].select = True
    bpy.ops.mesh.dissolve_verts()
    
    p1.verts.ensure_lookup_table()
    p1.verts[1].select = True
    
    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D': 
            ctx = bpy.context.copy() 
            ctx['area'] = area 
            ctx['region'] = area.regions[-1] 
            bpy.ops.view3d.snap_cursor_to_selected(ctx) 
            break 
      
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

    bpy.ops.object.modifier_add(type='SCREW')
    bpy.context.object.modifiers["Screw"].steps = 360
    #添加材质
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.0364558, 0.407289, 0.8)
    
    with open("e:/20181213.json") as f:
        tmp = json.load(f)
    
    vcpus = tmp['vcpus']
    num = tmp['running_vms']
    memory_mb = tmp['memory_mb'] 
    memory_mb_used = tmp['memory_mb_used']
    local_gb = tmp['local_gb']
    local_gb_used = tmp['local_gb_used']
    
    bpy.context.object.modifiers["Screw"].angle = 6.28319*(local_gb_used/local_gb)
    bpy.data.objects['Plane.002'].select=False
    # 定时器，效果不好。改成手动刷新的形式？
    # start = datetime.utcnow()
    # while True:
            # end = datetime.utcnow()
            # dt = end - start
            # if dt.seconds < 5:
                    # time.sleep(5)
            # else:
                    # print ('12345')
                    # with open("e:/20181213.json") as f:
                        # tmp = json.load(f)
    
                    # vcpus = tmp['vcpus']
                    # num = tmp['running_vms']
                    # memory_mb = tmp['memory_mb'] 
                    # memory_mb_used = tmp['memory_mb_used']
                    # local_gb = tmp['local_gb']
                    # local_gb_used = tmp['local_gb_used']
                    
                    # bpy.data.objects['Plane.002'].select=True
                    # bpy.context.object.modifiers["Screw"].angle = 6.28319*(local_gb_used/local_gb)
                    # bpy.data.objects['Plane.002'].select=False
                    
                    # bpy.data.objects['Plane.001'].select=True
                    # bpy.context.object.modifiers["Screw"].angle = 6.28319*(num/vcpus)
                    # bpy.data.objects['Plane.001'].select=False

                    # bpy.data.objects['Plane'].select=True
                    # bpy.context.object.modifiers["Screw"].angle = 6.28319*(memory_mb_used/memory_mb)
                    # bpy.data.objects['Plane'].select=False
    
# 添加刷新按钮
class Fresh_Panel(bpy.types.Panel):
    bl_idname = "fresh.button"
    bl_label = "fresh"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOL_PROPS"
    
    def draw(self,context):
    
        self.layout.operator("hello.hello",text = "刷新")
# 添加刷新操作
class Fresh_Button(bpy.types.Operator):

    bl_idname = "hello.hello"
    bl_label = "Say Hello"
    country = bpy.props.StringProperty()
    
    def execute(self, context):
        if self.country == '':
            with open("e:/20181213.json") as f:
                tmp = json.load(f)
    
            vcpus = tmp['vcpus']
            num = tmp['running_vms']
            memory_mb = tmp['memory_mb'] 
            memory_mb_used = tmp['memory_mb_used']
            local_gb = tmp['local_gb']
            local_gb_used = tmp['local_gb_used']
        
            bpy.data.objects['Plane.002'].select=True
            bpy.context.object.modifiers["Screw"].angle = 6.28319*(local_gb_used/local_gb)
            bpy.data.objects['Plane.002'].select=False
                    
            bpy.data.objects['Plane.001'].select=True
            bpy.context.object.modifiers["Screw"].angle = 6.28319*(num/vcpus)
            bpy.data.objects['Plane.001'].select=False

            bpy.data.objects['Plane'].select=True
            bpy.context.object.modifiers["Screw"].angle = 6.28319*(memory_mb_used/memory_mb)
            return{'FINISHED'} 
    
def register():
    bpy.utils.register_module(__name__)
    
    
def unregister():
    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    try:
        unregister()
    except Exception as e: 
        print(e)
        pass
    finally:
        register()