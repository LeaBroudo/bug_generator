
### Head ###
neck_latt = [(0,0,0),(3,3,3)]
neck_str = "neck_latt"
neck_scale = [.75,1.5]

face_latt = [(0,0,0),(5,3,3)]
face_str = "face_latt"
face_len = [1,125]
face_rad = [.3,1]
face_tilt = [1,30]

eye_latt = [(0,0,0),(3,3,3)]
eye_r_str = "eye_r_latt"
eye_l_str = "eye_l_latt"
eye_scale = [.5, 2]

man_latt = [(0,0,0),(3,3,5)]
man_str = "mandible_latt"
man_width = [1,3]
man_len = [1,6]
man_height = [1,3]

ant_latt = [(0,0,0),(3,3,3)]
ant_str = "antenna_latt"
ant_len = [1,5]
ant_width = [.1,6]



### Thorax ###
thorax_latt = [(0,0,0),(20,20,20)]
mid_thx_latt = [(6,0,0),(12,20,20)]
front_thx_latt = [(0,0,0),(6,20,20)]
back_thx_latt = [(12,0,0),(20,20,20)]
#PATTERN

### Abdomen ### 
abdomen_latt = [(0,0,0),(20,20,20)]
mid_abd_latt = [(6,0,0),(12,20,20)]
front_abd_latt = [(0,0,0),(6,20,20)]
back_abd_latt = [(12,0,0),(20,20,20)]
#PATTERN

### Wings ###
wing_rot = (36,-15,33)
wing_locs = [(4,8,3), (16,8,3)] 

wing_mesh = "wing_mesh_"
wing_base = "wing_base_joint_"
wing = "wing_joint_"
wing_latt = "wing_latt_"

body_wing_joints = {
    wing_locs[0][0] : "thorax_1_joint",
    wing_locs[1][0] : "thorax_2_joint"
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
right_diff = -2.5  

body_arm_joints = {
    thorax_arms[0][0] : "thorax_1_joint",
    thorax_arms[1][0] : "thorax_2_joint",
    thorax_arms[2][0] : "thorax_3_joint",
    abdomen_arms[0][0] : "abdomen_1_joint",
    abdomen_arms[1][0] : "abdomen_2_joint",
    abdomen_arms[2][0] : "abdomen_3_joint",
}



### Colors/Materials ###