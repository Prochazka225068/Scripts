import maya.cmds as cmds

cmds.polyTorus(r=3, n= 'SM_Torus_01')
cmds.polySphere(r= 3, n= 'SM_Sphere_01')
cmds.move(1.5,0,0, 'SM_Sphere_01')
cmds.polyCBoolOp('SM_Torus_01', 'SM_Sphere_01', op = 2, n= 'SM_Difference_01')

cmds.polySphere(r= 3, n= 'SM_Sphere_02')
cmds.move(0,1.5,0, 'SM_Sphere_02')
cmds.polyCBoolOp('SM_Difference_01', 'SM_Sphere_02', op = 2, n= 'SM_Difference_02')
