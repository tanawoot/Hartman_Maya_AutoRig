cmds.group(n='hr_locators', em=True)
cmds.group(n='head_Ls', em=True, p='hr_locators')
cmds.group(n='body_Ls', em=True, p='hr_locators')
cmds.group(n='arm_Ls', em=True, p='hr_locators')
cmds.group(n='leg_Ls', em=True, p='hr_locators')

arm_joints=['L_clavicle_loc','L_shoulder_loc','L_elbow_loc','L_wrist_loc', 'L_middle01_loc', 'L_middle02_loc', 'L_middle03_loc', 'L_middle04_loc', 'L_thumb01_loc', 'L_thumb02_loc', 'L_thumb03_loc', 'L_pointer01_loc', 'L_pointer02_loc', 'L_pointer03_loc', 'L_pointer04_loc', 'L_index01_loc', 'L_index02_loc', 'L_index03_loc', 'L_index04_loc', 'L_pinky01_loc', 'L_pinky02_loc', 'L_pinky03_loc', 'L_pinky04_loc']
leg_joints=['waist_loc','L_hip_loc','L_knee_loc','L_ankle_loc','L_heel_loc','L_ball_loc','L_tippytoe_loc']
head_joints=['neck01_loc','neck02_loc','head_loc']
body_joints=['root_loc','spine01_loc','spine02_loc','spine03_loc','spine04_loc','spine05_loc']

for loc in arm_joints:
    cmds.spaceLocator(n=loc)
    cmds.scale(5, 5, 5, loc)
    cmds.parent(loc, 'arm_Ls')
for loc in leg_joints:
    cmds.spaceLocator(n=loc)
    cmds.scale(5, 5, 5, loc)
    cmds.parent(loc, 'leg_Ls')
for loc in head_joints:
    cmds.spaceLocator(n=loc)
    cmds.scale(5, 5, 5, loc)
    cmds.parent(loc, 'head_Ls')
for loc in body_joints:
    cmds.spaceLocator(n=loc)
    cmds.scale(5, 5, 5, loc)
    cmds.parent(loc, 'body_Ls')