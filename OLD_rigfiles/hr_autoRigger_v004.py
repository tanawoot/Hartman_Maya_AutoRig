import maya.cmds as cmds
cmds.select( d=True )

def encodeList(list):
    for index, item in enumerate(list):
        item.encode('ascii')
        list[index]=item[:-4]
    return list

def createJoint(joint_name):
    joint_Pos = cmds.pointPosition( joint_name + '_loc', w=True)
    cmds.joint( p=joint_Pos, n=joint_name)

def buildArms():
    arm_List = encodeList(cmds.listRelatives('arm_Ls'))
    for item in arm_List:
        createJoint(item)
    cmds.parent('L_pinky01', 'L_wrist')
    cmds.parent('L_index01', 'L_wrist')
    cmds.parent('L_pointer01', 'L_wrist')
    cmds.parent('L_thumb01', 'L_wrist')
    cmds.mirrorJoint('L_clavicle',searchReplace=('L_', 'R_'))
    
def buildLegs():
    leg_List = encodeList(cmds.listRelatives('leg_Ls'))
    for item in leg_List:
        if item != 'L_heel': 
            createJoint(item)
        elif item == 'L_hip':
            cmds.joint( 'waist', e=True, o=(0,0,0))
    cmds.mirrorJoint('L_hip',searchReplace=('L_', 'R_'))
    
def buildHead():
    head_List = encodeList(cmds.listRelatives('head_Ls'))
    for item in head_List:
        createJoint(item)

def buildBody():
    body_List = encodeList(cmds.listRelatives('body_Ls'))
    for item in body_List:
        createJoint(item)
    
def connectBodyParts():
    cmds.parent('neck01', 'spine05')
    cmds.parent('L_clavicle', 'spine05')
    cmds.parent('R_clavicle', 'spine05')
    
buildArms()
cmds.select( d=True )
buildLegs()
cmds.select( d=True )
buildHead()
cmds.select( d=True )
buildBody()
cmds.select( d=True )
connectBodyParts()

# Orient All Joints

cmds.joint( 'root', ch=True, e=True, zso=True, oj='yxz', sao='xup')
cmds.joint( 'waist', ch=True, e=True, zso=True, oj='yxz', sao='xup')