import bpy

selected = bpy.context.selected_objects

for i in selected:

    a = i.location
    b = i.matrix_world.translation

    i.delta_location = (a[0],a[1],a[2])
    i.location = (b[0],b[1],b[2])