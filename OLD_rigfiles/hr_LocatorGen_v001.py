cmds.group(n='hr_locators', em=True)
cmds.group(n='head_Ls', em=True, p='hr_locators')
cmds.group(n='body_Ls', em=True, p='hr_locators')
cmds.group(n='arm_Ls', em=True, p='hr_locators')
cmds.group(n='leg_Ls', em=True, p='hr_locators')

arm_joints=['L_clavicle_loc','L_shoulder_loc','L_elbow_loc','L_wrist_loc']
leg_joints=['waist_loc','L_hip_loc','L_knee_loc','L_ankle_loc','L_heel_loc','L_ball_loc','L_tippytoe_loc']
head_joints=['neck01_loc','neck02_loc','head_loc']
body_joints=['root_loc','spine01_loc','spine02_loc','spine03_loc','spine04_loc','spine05_loc']

for loc in arm_joints:
    cmds.spaceLocator(n=loc)
    cmds.parent(loc, 'arm_Ls')
for loc in leg_joints:
    cmds.spaceLocator(n=loc)
    cmds.parent(loc, 'leg_Ls')
for loc in head_joints:
    cmds.spaceLocator(n=loc)
    cmds.parent(loc, 'head_Ls')
for loc in body_joints:
    cmds.spaceLocator(n=loc)
    cmds.parent(loc, 'body_Ls')