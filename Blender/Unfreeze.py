import bpy

class UnfreezeLocationOperator(bpy.types.Operator):

    bl_idname = "unfreeze.operator_location"
    bl_label = "Unfreeze Location"
    bl_description = "Changes delta location back to global location"

    def execute(self, context):

        for i in bpy.context.selected_objects:

            worldPos = i.matrix_world.translation

            i.delta_location = (0,0,0)
            i.location = (worldPos[0],worldPos[1],worldPos[2])
            
        return {'FINISHED'}

class UnfreezeRotationOperator(bpy.types.Operator):

    bl_idname = "unfreeze.operator_rotation"
    bl_label = "Unfreeze Rotation"
    bl_description = "Changes delta rotation back to global rotation"

    def execute(self, context):

        for i in bpy.context.selected_objects:

            worldRot = i.matrix_world.to_euler()

            i.delta_rotation_euler = (0,0,0)
            i.rotation_euler = (worldRot[0], worldRot[1], worldRot[2])

        return {'FINISHED'}

class UnfreezeScaleOperator(bpy.types.Operator):

    bl_idname = "unfreeze.operator_scale"
    bl_label = "Unfreeze Scale"
    bl_description = "Changes delta scale back to global scale"

    def execute(self, context):

        for i in bpy.context.selected_objects:

            worldSca = i.matrix_world.to_scale()

            i.delta_scale = (1,1,1)
            i.scale = (worldSca[0], worldSca[1], worldSca[2])
       
        return {'FINISHED'}

class UnfreezeAllOperator(bpy.types.Operator):

    bl_idname = "unfreeze.operator_all"
    bl_label = "Unfreeze All"
    bl_description = "Changes all delta transforms back to global transforms"

    def execute(self, context):

        for i in bpy.context.selected_objects:
            
            worldPos = i.matrix_world.translation

            i.delta_location = (0,0,0)
            i.location = (worldPos[0],worldPos[1],worldPos[2])

            worldRot = i.matrix_world.to_euler()

            i.delta_rotation_euler = (0,0,0)
            i.rotation_euler = (worldRot[0], worldRot[1], worldRot[2])
        
            worldSca = i.matrix_world.to_scale()

            i.delta_scale = (1,1,1)
            i.scale = (worldSca[0], worldSca[1], worldSca[2])
       
        return {'FINISHED'}
    

def button_func(self, context):
    self.layout.separator()
    self.layout.operator("unfreeze.operator_location", text="Delta Location to World")
    self.layout.operator("unfreeze.operator_rotation", text="Delta Rotation to World")
    self.layout.operator("unfreeze.operator_scale", text="Delta Scale to World")
    self.layout.operator("unfreeze.operator_all",  text="Delta All Transforms to World")

def register():
    bpy.utils.register_class(UnfreezeLocationOperator)
    bpy.utils.register_class(UnfreezeRotationOperator)
    bpy.utils.register_class(UnfreezeScaleOperator)
    bpy.utils.register_class(UnfreezeAllOperator)
    bpy.types.VIEW3D_MT_object_apply.append(button_func)

def unregister():
    bpy.utils.unregister_class(UnfreezeLocationOperator)
    bpy.utils.unregister_class(UnfreezeRotationOperator)
    bpy.utils.unregister_class(UnfreezeScaleOperator)
    bpy.utils.unregister_class(UnfreezeAllOperator)
    bpy.types.VIEW3D_MT_object_apply.remove(button_func)

register()