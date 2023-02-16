# WARNING: This script is a complete dumpster fire. I have no idea of blender scripting and it is very weird.
# but it works.
import math
import bpy

def make_icon_extrusion(fp):
    bpy.ops.import_curve.svg(filepath=fp)

    for ob in bpy.data.objects:
        if ob.type != "CURVE":
            continue
        ob.data.extrude = .009  # the thickness that you want

    # convert the extruded curve to mesh
    for obj in bpy.data.objects:
        if obj.type == "CURVE":
            mesh = bpy.data.meshes.new_from_object(obj)
            new_obj = bpy.data.objects.new(obj.name, mesh)
            new_obj.matrix_world = obj.matrix_world
            bpy.context.collection.objects.link(new_obj)
            bpy.ops.object.delete(use_global=False, confirm=False)
            bpy.ops.object.delete(use_global=False, confirm=False)
            bpy.data.curves.remove(obj.data)

    bpy.ops.object.select_all(action="SELECT")

    obs = []
    for ob in bpy.context.scene.objects:
        # whatever objects you want to join...
        if ob.type == 'MESH':
            obs.append(ob)

    ctx = bpy.context.copy()

    ctx['active_object'] = obs[0]
    ctx['selected_objects'] = obs

    bpy.ops.object.join(ctx)

    extrusion = bpy.context.selected_objects[0]
    extrusion.name = "icon"

    bpy.context.view_layer.objects.active = extrusion

    # center icon on the key
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')

    oldX, oldY, oldZ = extrusion.dimensions
    newY = 9
    scaleFactor = newY / oldY
    newX = oldX * scaleFactor

    if newX > 9:
        newX = 9
        scaleFactor = newX / oldX
        newY = oldY * scaleFactor

    extrusion.dimensions = (newX, newY, 1)
    extrusion.location = (6.5, 7, 9)
    return extrusion

def make_keycap(stl_fp: str, svg_fb: str, target_fp: str):
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False, confirm=False)

    for collection in bpy.data.collections:
        bpy.data.collections.remove(collection)

    # generate icon extrusion
    icon = make_icon_extrusion(svg_fb)

    # import base keycap
    bpy.ops.import_mesh.stl(filepath=stl_fp)

    # delete collections
    for collection in bpy.data.collections:
        bpy.data.collections.remove(collection)

    bpy.ops.export_mesh.stl(filepath=target_fp)

