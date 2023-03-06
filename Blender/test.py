import bpy

class MY_OT_my_operator(bpy.types.Operator):
    bl_idname = "my.operator"
    bl_label = "My Operator"

    def execute(self, context):
        # Your code here
        selected = bpy.context.selected_objects

        for i in selected:

            a = i.location
            b = i.matrix_world.translation

            i.delta_location = (a[0],a[1],a[2])
            i.location = (b[0],b[1],b[2])
        return {'FINISHED'}

class MY_Apply_Button(bpy.types.UI_MT_button_context_menu):
    bl_label = "My Panel"
    bl_idname = "OBJECT_PT_my_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My Addon"
    

    def draw(self, context):
        layout = self.layout
        layout.operator("my.operator", text="My Button")


def register():
    bpy.utils.register_class(MY_OT_my_operator)
    bpy.utils.register_class(MY_Apply_Button)
    bpy.types.VIEW3D_MT_object_apply.append(MY_Apply_Button)

def unregister():
    bpy.utils.unregister_class(MY_OT_my_operator)
    bpy.utils.unregister_class(MY_Apply_Button)
    bpy.types.VIEW3D_MT_object_apply.remove(MY_Apply_Button)

if __name__ == "__main__":
    register()