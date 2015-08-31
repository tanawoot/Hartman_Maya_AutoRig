cmds.select( d=True)
cmds.group(n='hr_ctrls', em=True)

root_ctrls=['master', 'root', 'waist']

for bone in root_ctrls:
    cmds.select( d=True )
    cmds.group(n=bone + '_o', em=True)
    cmds.circle(n=bone + '_ctrl', nr=(0, 1, 0), c=(0, 0, 0), r=2)
    cmds.parent(bone + '_ctrl', bone + '_o')
    if bone != 'master':
        cmds.pointConstraint( 'root', bone + '_o' )
        cmds.pointConstraint( 'root', bone + '_o', e=True, rm=True)
    else:
        cmds.pointConstraint( 'hr_ctrls', bone + '_o' )
        cmds.pointConstraint( 'hr_ctrls', bone + '_o', e=True, rm=True)

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
    cmds.parent(bone + '_o', parent_joint + '_ctrl')

# Build Controllers
for bone in cmds.listRelatives('waist', ad=True):
    cmds.select( d=True )
    cmds.group(n=bone + '_o', em=True)
    cmds.circle(n=bone + '_ctrl', nr=(0, 1, 0), c=(0, 0, 0), r=2)
    cmds.parent(bone + '_ctrl', bone + '_o')
    cmds.pointConstraint( bone, bone + '_o' )
    cmds.pointConstraint( bone, bone + '_o', e=True, rm=True)
    
# Parent Controllers
for bone in cmds.listRelatives('waist', ad=True):
    parent_joint = cmds.listRelatives(bone, p=True)[0]
    cmds.parent(bone + '_o', parent_joint + '_ctrl')

cmds.parent('root_o', 'master_ctrl')
cmds.parent('waist_o', 'master_ctrl')
cmds.parent('master_o', 'hr_ctrls')

