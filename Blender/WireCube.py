import bpy


class CreateCubeOperator(bpy.types.Operator):
    bl_idname = "object.createcube"
    bl_label = "createCube"
    bl_description = "Creates Wire cube which can be used as controller"

    def execute(self, context):



        return {'FINISHED'}

class AlignOperator(bpy.types.Operator):
    bl_idname = "object.align"
    bl_label = "Align"
    bl_description = "Alignes selected to active"

    def execute(self, context):



        return {'FINISHED'}
    


def register():
    bpy.utils.register_class(CreateCubeOperator)
    bpy.utils.register_class(AlignOperator)

def unregister():
    bpy.utils.unregister_class(CreateCubeOperator)
    bpy.utils.unregister_class(AlignOperator)

register()
