cmds.group(n='hr_ctrls', em=True)

cmds.select( d=True )
cmds.group(n='root_o', em=True)
cmds.circle(n='root_ctrl', nr=(0, 1, 0), c=(0, 0, 0), r=2)
cmds.parent('root_ctrl', 'root_o')
cmds.pointConstraint( 'root', 'root_o' )
cmds.pointConstraint( 'root', 'root_o', e=True, rm=True)

# Build Controllers
for bone in cmds.listRelatives('root', ad=True):
    cmds.select( d=True )
    cmds.group(n=bone + '_o', em=True)
    cmds.circle(n=bone + '_ctrl', nr=(0, 1, 0), c=(0, 0, 0), r=2)
    cmds.parent(bone + '_ctrl', bone + '_o')
    cmds.pointConstraint( bone, bone + '_o' )
    cmds.pointConstraint( bone, bone + '_o', e=True, rm=True)
    
# Parent Controllers
for bone in cmds.listRelatives('root', ad=True):
    parent_joint = cmds.listRelatives(bone, p=True)[0]
    # print('parent: ' + parent_joint)
    # print('child: ' + bone)
    cmds.parent(bone + '_o', parent_joint + '_ctrl')
