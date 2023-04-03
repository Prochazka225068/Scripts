import maya.cmds as cmds
import maya.api.OpenMaya as om

# Get the selected object
sel = cmds.ls(selection=True)
if not sel:
    raise ValueError('Please select an object!')
    
# Create a selection list with the object
sel_list = om.MSelectionList()
sel_list.add(sel[1])

# Get the MDagPath for the object
dag_path = sel_list.getDagPath(0)
obj_mfn = om.MFnMesh(dag_path)


# Get the x and z coordinates
num_points= cmds.getAttr(sel[0]+".spans")

for i in range(num_points):

    pos= cmds.pointPosition(sel[0]+".ep[{}]".format(i),w=True)
     
    x_pos = pos[0]
    z_pos = pos[2]

    # Create an MFloatPoint for the point
    float_point = om.MPoint(x_pos, 0, z_pos)

    # Get the closest point on the surface of the object to the point
    hit_point, face_index = obj_mfn.getClosestPoint(float_point, space=om.MSpace.kWorld)

    # Get the y coordinate of the hit point
    y_pos = hit_point.y
    
    print(str(x_pos)+ " " +str(y_pos)+ " "+ str(z_pos))
    cmds.xform(sel[0]+".ep[{}]".format(i), t=[x_pos, y_pos,z_pos],ws=True)