
### Head ###
head = [".f[1680:2099]", ".f[2130:2159]"] #THIS WILL BE MORE
#Mouth
#face
#eyes
#nose
#mandibles
#antenae
    #base
    #mid
    #tip

### Thorax ###

#thorax
#mid_thorax
#front_thorax
#back_thorax

### Abdomen ###

#abdomen
#mid_abdomen
#front_abdomen
#back_abdomen


### Edges ###
head_thorax_ring = ".vtx[1600:1629]"
thorax_abdomen_ring = ".vtx[840:869]"

### Wings ###
wing_locs = {
    "cricket" : [(".f[774:778]")],
    "mosquito" : [(".f[774:778]")],
    "wasp" : [(".f[1262:1264]", ".f[1292:1294]", ".f[1322:1324]", ".f[1352:1354]")],
    "fly" : [(".f[1262:1264]", ".f[1292:1294]", ".f[1322:1324]", ".f[1352:1354]")],
    "dragonfly" : [(".f[1262:1264]", ".f[1292:1294]", ".f[1322:1324]", ".f[1352:1354]"), (".f[902:904]", ".f[932:934]" ".f[962:964]", ".f[992:994]")],
    "butterfly" : [(".f[934:935]", ".f[964:965]", ".f[994:995]", ".f[1024:1025]", ".f[1054:1055]", ".f[1084:1085]", ".f[1114:1115]", ".f[1144:1145]", ".f[1174:1175]", ".f[1204:1205]", ".f[1234:1235]", ".f[1264:1265]", ".f[1294:1295]", ".f[1324:1325]", ".f[1354:1355]", ".f[1384:1385]", ".f[1414:1415]", ".f[1444:1445]", ".f[1474:1475]", ".f[1504:1505]")]
}

#wing design, maybe a texture/brush?
#outside verts
#inside verts
#wing

### Arms ###
#arm
#femur verts
#tibia verts
#tarsus verts
#claw verts

arm_locs = {
    "thorax": [(-12,3,9), (-6,3,9.25), (0,3,9.5)],
    "abdomen": [(10,3,9), (16,3,9.25), (22,3,9)]
}

### Colors/Materials ###