import maya.cmds as cmds

# Select hirearchy of the root if root is not selected >> ValueError 
cmds.select(hi=1)
rigMain = cmds.ls(sl=1)
if not rigMain:
    raise ValueError('Select root joint of a rig')

#Duplicate Root and children + rename
cmds.duplicate(rigMain[0], rc=1)

cmds.select(hi=1)
rigCtrl = cmds.ls(sl=1)

for (iCtrl, iMain) in zip(rigCtrl, rigMain):
    #duplicates joint + renames to _grp
    igrp = cmds.duplicate(iCtrl, po=1, n=iCtrl[:-1] + "_grp")
    
    #locks and makes unkeyable
    cmds.setAttr(igrp[0] + '.translate', k=0, cb=0, l=1)
    cmds.setAttr(igrp[0] + '.rotate', k=0, cb=0, l=1)
    cmds.setAttr(igrp[0] + '.scale', k=0, cb=0, l=1)

    #parents _grp joint to ctrl and adds constraints
    cmds.parent(iCtrl,igrp)
    cmds.pointConstraint(iCtrl,iMain)
    cmds.orientConstraint(iCtrl,iMain)

    #unlocks and makes keyable if locked
    cmds.setAttr(iMain + ".translate", l=0, k=1, cb=1)
    cmds.setAttr(iMain + ".rotate", l=0, k=1, cb=1)
    cmds.setAttr(iMain + ".scale", l=0, k=1, cb=1)

    #renames copied bones from line 5 to _Ctrl
    cmds.rename(iCtrl, iCtrl[:-1] + "_Ctrl")
