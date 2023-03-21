import maya.cmds as cmds

selObj= cmds.ls(sl=True)

totalTrackLen = cmds.arclen('L_Track_Guide')
singleTrackLen = cmds.arclen('singleTrackLenCurve')

totalTrack = 'L_Track_Guide'
singleTrack = 'Track'

chainStep = int(totalTrackLen/singleTrackLen) + 2

 
for i in range(chainStep):

    if(i != (chainStep -1)):

        cmds.keyTangent(itt='linear', ott='linear', g=1)
        dup = cmds.duplicate(singleTrack)
        cmds.pathAnimation (dup, fm=1, f=1, fa='z' ,ua='y', wut="object", wuo="L_TrackUP", iu=1, inverseFront=0, b=0, stu=(1+i), etu=(chainStep+i), c=totalTrack)