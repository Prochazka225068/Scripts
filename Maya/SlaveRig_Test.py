import maya.cmds as cmds

cmds.select(hi=1)
selection = cmds.ls(sl=1)

for i in selection:
    cmds.select(cl=1)

    cmds.setAttr(i + ".translate", lock=0, keyable=1, channelBox=1)
    cmds.setAttr(i + ".rotate", lock=0, keyable=1, channelBox=1)
    cmds.setAttr(i + ".scale", lock=0, keyable=1, channelBox=1)

    rigGrp = cmds.joint(n=i + '_grp')
    parentGrp = cmds.parentConstraint(i, rigGrp)
    cmds.delete(parentGrp, cn=1)

    rigCtrl = cmds.joint(n=i + '_Ctrl')
    parentCtrl = cmds.parentConstraint(i, rigCtrl)
    cmds.delete(parentCtrl, cn=1)

    parent = cmds.listRelatives(i, p=1)
    if parent:
        cmds.parent(rigCtrl, parent[0]+ '_Ctrl')

    cmds.FreezeTransformations()

    cmds.pointConstraint(rigCtrl, i)
    cmds.orientConstraint(rigCtrl, i)

    cmds.setAttr(rigGrp + '.translate', lock=1, keyable=0, channelBox=0)
    cmds.setAttr(rigGrp + '.rotate', lock=1, keyable=0, channelBox=0)
    cmds.setAttr(rigGrp + '.scale', lock=1, keyable=0, channelBox=0)