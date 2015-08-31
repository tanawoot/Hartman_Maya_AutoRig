cmds.select( d=True)
cmds.group(n='hr_ctrls', em=True)

root_ctrls=['master', 'root', 'waist']

# Be able to choose the curve type for the controller
ctrl_type=['circle', 'box', 'ball']

# Iterate through base joints
# Build offets & control curves
for ctrl in root_ctrls:
    cmds.select( d=True )
    cmds.group(n=ctrl + '_o', em=True)
    cmds.circle(n=ctrl + '_ctrl', nr=(0, 1, 0), c=(0, 0, 0), r=2)
    cmds.parent(ctrl + '_ctrl', ctrl + '_o')
    if ctrl != 'master':
        cmds.pointConstraint( 'root', ctrl + '_o' )
        cmds.pointConstraint( 'root', ctrl + '_o', e=True, rm=True)
        
        # Build Controllers
        for bone in cmds.listRelatives(ctrl, ad=True):
            cmds.select( d=True )
            cmds.group(n=bone + '_o', em=True)
            cmds.circle(n=bone + '_ctrl', nr=(0, 1, 0), c=(0, 0, 0), r=2)
            cmds.parent(bone + '_ctrl', bone + '_o')
            if bone == 'L_wrist' or bone == 'R_wrist':
                cmds.circle(n=bone[0:2]+'hand_ctrl', nr=(0,1,0), c=(0,0,0), r=3)
                print(bone)
                cmds.pointConstraint(bone + '_ctrl', bone[0:2]+'hand_ctrl')
                cmds.pointConstraint(bone + '_ctrl', bone[0:2]+'hand_ctrl', e=True, rm=True)
                cmds.select(bone[0:2]+'hand_ctrl')
                cmds.move(2, y=True)
                cmds.select(d=True)
                cmds.parentConstraint(bone + '_ctrl', bone[0:2]+'hand_ctrl', mo=True)
            cmds.parentConstraint( bone, bone + '_o' )
            cmds.parentConstraint( bone, bone + '_o', e=True, rm=True)
            
        # Parent Controllers
        for bone in cmds.listRelatives(ctrl, ad=True):
            parent_joint = cmds.listRelatives(bone, p=True)[0]
            cmds.parent(bone + '_o', parent_joint + '_ctrl')
    else:
        cmds.pointConstraint( 'hr_ctrls', ctrl + '_o' )
        cmds.pointConstraint( 'hr_ctrls', ctrl + '_o', e=True, rm=True)

# Clean up structure
cmds.parent('root_o', 'master_ctrl')
cmds.parent('waist_o', 'master_ctrl')
cmds.parent('master_o', 'hr_ctrls')

