cmds.group(n='hr_ctrls', em=True)

for bone in cmds.listRelatives('root', ad=True):
    cmds.select( d=True )
    cmds.group(n=bone + '_o', em=True)
    cmds.circle(n=bone + '_ctrl', nr=(0, 1, 0), c=(0, 0, 0), r=2)
    cmds.parent(bone + '_ctrl', bone + '_o')
    cmds.pointConstraint( bone, bone + '_o' )
    cmds.pointConstraint( bone, bone + '_o', e=True, rm=True)
