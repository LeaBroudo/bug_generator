body = "body_mesh"

### Head ###
neck_latt = [(0,0,0),(3,3,3)]
neck_str = "neck_latt"
neck_scale = [.75,1.5]

face_latt = [(0,0,0),(5,3,3)]
face_str = "face_latt"
face_len = [1,5]
face_rad = [.3,1]
face_tilt = [1,30]

eye_latt = [(0,0,0),(3,3,3)]
eye_r_str = "eye_r_latt"
eye_r_joint = "eye_joint_R"
eye_l_str = "eye_l_latt"
eye_l_joint = "eye_joint_L"
eye_dist = [.9, 1.5]
eye_scale = [.5,2]

man_latt = [(0,0,0),(3,3,5)]
man_str = "mandible_latt"
man_width = [1,3]
man_len = [1,2]
man_height = [1,5]

ant_latt = [(0,0,0),(3,3,3)]
ant_str = "antenna_latt"
ant_len = [1,4]
ant_width = [.1,6]

### Thorax ###
thorax_latt = [(0,0,0),(20,20,20)]
mid_thx_latt = [(6,0,0),(12,20,20)]
front_thx_latt = [(0,0,0),(6,20,20)]
back_thx_latt = [(12,0,0),(20,20,20)]

thx_front = "thorax_1_joint"
thx_mid = "thorax_2_joint"
thx_back = "thorax_3_joint"

thx_scale = [.5,2]
thx_len = [0,10]
#PATTERN


### Abdomen ### 
abdomen_latt = [(0,0,0),(20,20,20)]
mid_abd_latt = [(6,0,0),(12,20,20)]
front_abd_latt = [(0,0,0),(6,20,20)]
back_abd_latt = [(12,0,0),(20,20,20)]

abd_front = "abdomen_1_joint"
abd_mid = "abdomen_2_joint"
abd_back = "abdomen_3_joint"

abd_scale = [.5,2]
abd_len = [0,20]
abd_tilt = [0,5]
#PATTERN

### Wings ###
wing_rot = (36,-15,50)
wing_locs = [(-12,8.5,3), (-4.5,8.5,3)] 

wing_mesh = "wing_mesh_"
wing = "wing_joint_"
wing_base = "wing_base_joint_"
wing_low = "wing_low_joint_"
wing_top = "wing_top_joint_"

wing_scale = [.75,2]
wing_top_scale = [0,20]
wing_low_scale = [0,5]

body_wing_joints = {
    wing_locs[0][0] : thx_front,
    wing_locs[1][0] : thx_mid
}

### Arms ###
arm_mesh = "arm_mesh_"
arm = "arm_joint_"
shoulder = "shoulder_joint_"
femur = "femur_joint_"
knee = "knee_joint_"
tibia = "tibia_joint_"
tarsus = "tarsus_joint_"
hand = "hand_joint_"

spread_dist = [1, 4]
knee_height = [-2, 20]

tibia_len = [0,10]
tibia_rad = [1,2]

tarsus_len = [0,10]
tarsus_rad = [1,2]

femur_len = [1,10]
femur_rad = [1,2]

shoulder_len = [.5,10]
shoulder_rad = [1,1.5]

thorax_arms = [(-12,3,5), (-6,3,5), (0,3,5)]
abdomen_arms = [(10,3,5), (16,3,5), (22,3,5)]

body_arm_joints = {
    thorax_arms[0][0] : thx_front,
    thorax_arms[1][0] : thx_mid,
    thorax_arms[2][0] : thx_back,
    abdomen_arms[0][0] : abd_front,
    abdomen_arms[1][0] : abd_mid,
    abdomen_arms[2][0] : abd_back,
}

### Colors/Materials ###
bodyMat = None
wingMat = None
armMat = None
color_range = [(0,0,0),(1,1,1)]