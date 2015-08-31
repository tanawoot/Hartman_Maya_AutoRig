import maya.cmds as cmds
cmds.select( d=True )

def encodeList(list):
    for index, item in enumerate(list):
        item.encode('ascii')
        list[index]=item[:-4]
    return list

def createJoint(joint_name, isSym):
    joint_Pos = cmds.pointPosition( joint_name + '_loc', w=True)
    cmds.joint( p=joint_Pos, n=joint_name, sym=isSym, sa='z')

def buildArms():
    arm_List = encodeList(cmds.listRelatives('arm_Ls'))
    for item in arm_List:
        createJoint(item, True)
    
def buildLegs():
    print('hello')
    
def buildHead():
    arm_List = encodeList(cmds.listRelatives('head_Ls'))
    for item in arm_List:
        createJoint(item, False)
    
def connectBodyParts():
    print('hello')
    
buildArms()

# Orient All Joints
#

cmds.joint( 'root', ch=True, e=True, zso=True, oj='yzx', sao='zup')

# Build appendages seperately for symmetry + parenting
    # search for top spine joint
# Auto build grouping structure