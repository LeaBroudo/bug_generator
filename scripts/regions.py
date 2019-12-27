
### Head ###
full_head = [".f[1680:2099]", ".f[2130:2159]"] #THIS WILL BE MORE
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
#Put in class
"""
def get_vert_stripes: 
    """
    """

def get_horiz_stripes: 
    """
    """
"""
#thorax
#mid_thorax
#front_thorax
#back_thorax

### Abdomen ###
#Put in class
"""
def get_vert_stripes: 
    """
    """

def get_horiz_stripes: 
    """
    """
"""
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
    "thorax": [(".f[1456:1461]", ".f[1486:1491]", ".f[1516:1521]"), (".f[1336:1341]", ".f[1366:1371]", ".f[1396:1401]"), (".f[1216:1221]", ".f[1246:1251]", ".f[1276:1281]"),(".f[1096:1101]", ".f[1126:1131]", ".f[1156:1161]"), (".f[976:981]", ".f[1006:1011]", ".f[1036:1041]")],
    "abdomen": [(".f[976:981]", ".f[1006:1011]", ".f[1036:1041]"), (".f[556:561]", ".f[586:591]", ".f[616:621]"), (".f[436:441]", ".f[466:471]", ".f[496:501]"), (".f[316:321]", ".f[346:351]", ".f[376:381]"), (".f[196:201]", ".f[226:231]", ".f[256:261]")]
}

### Colors/Materials ###