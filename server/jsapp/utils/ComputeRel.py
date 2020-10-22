from jsapp.utils.DataBase import DataBase
from jsapp.utils.TaishiInfo import getDynamicInfo, getEntities
import jsapp.utils.EntityType as et
from math import radians, cos, sin, asin, sqrt
from geopy.distance import geodesic
from jsapp.utils import AppConfig

#根据经纬度计算两点之间的距离 或者使用geodesic
def distance(lng1,lat1,lng2,lat2):
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    distance = round(distance / 1000, 3)
    return distance

#协同
def computeCoordinationRel(sceneEntity):
    #射程、损伤指数、命中概率、速度、航向、打击目标的运动介质
    coo = {}
    for uID1,entity1 in sceneEntity.items():
        type1 = entity1['Icontype']
        DamagePoints1 = entity1['DamagePoints']
        Lat1 = entity1['Lat']
        Lng1 = entity1['Lng']
        for uID2, entity2 in sceneEntity.items():
            if not uID1 == uID2:
                type2 = entity2['Icontype']
                DamagePoints2 = entity2['DamagePoints']

                Pok1 = entity1[et.entityType(type1,'Pok')]  # 命中概率/100
                Pok2 = entity2[et.entityType(type2,'Pok')]
                Rangename1 = et.entityType(type1, 'Range')
                RangeMax1 = entity1[Rangename1+'Max'] * 1.852       # 单位nm 海里 =1.852km   最大打击范围
                RangeAvg1 = (entity1[Rangename1+'Max'] + entity1[Rangename1+'Min']) / 2 * 1.852  # 单位nm 海里 =1.852km  平均打击范围
                Rangename2 = et.entityType(type2, 'Range')
                RangeMax2 = entity2[Rangename2 + 'Max'] * 1.852
                RangeAvg2 = (entity2[Rangename2 + 'Max'] + entity2[Rangename2 + 'Min']) / 2 * 1.852
                Lat2 = entity2['Lat']
                Lng2 = entity2['Lng']

                dis = geodesic((Lat1,Lng1),(Lat2,Lng2)).km   # 单位km

                # if (dis < RangeAvg1 + RangeAvg2):
                if (dis < RangeMax1 + RangeMax2):
                    # coov = (RangeAvg1 + RangeAvg2 - dis)/dis * (DamagePoints1*Pok1/100) * (DamagePoints2*Pok2/100)
                    coov = (RangeMax1 + RangeMax2 - dis)/(RangeMax1 + RangeMax2) * (Pok1/100) * (Pok2/100)
                    if coov>0:
                        if uID1 not in coo:
                            coo[uID1]=[]
                        coo[uID1].append((uID2,coov))
                else:
                    continue
    return coo

# 威胁
def computeThreatenRel(sceneEntity):  # 站在L方角度看H方对L的威胁程度
    # 射程、损伤指数、命中概率、速度、航向、打击目标的运动介质
    coo = {}
    for uID1, entity1 in sceneEntity['H'].items():
        type1 = entity1['Icontype']
        DamagePoints1 = entity1['DamagePoints']
        Lat1 = entity1['Lat']
        Lng1 = entity1['Lng']
        # Bearing1 = entity1['Bearing']
        for uID2, entity2 in sceneEntity['L'].items():
            if not uID1 == uID2:
                type2 = entity2['Icontype']
                DamagePoints2 = entity2['DamagePoints']
                Lat2 = entity2['Lat']
                Lng2 = entity2['Lng']
                # Bearing2 = entity2['Bearing']

                Pok1 = entity1[et.entityType(type1, 'Pok')]  # 命中概率/100
                Pok2 = entity2[et.entityType(type2, 'Pok')]
                Rangename1 = et.entityType(type1, 'Range')
                RangeMax1 = entity1[Rangename1 + 'Max'] * 1.852  # 单位nm 海里 =1.852km   最大打击范围
                # RangeAvg1 = (entity1[Rangename1 + 'Max'] + entity1[Rangename1 + 'Min']) / 2 * 1.852  # 单位nm 海里 =1.852km  平均打击范围
                Rangename2 = et.entityType(type2, 'Range')
                RangeMax2 = entity2[Rangename2 + 'Max'] * 1.852
                # RangeAvg2 = (entity2[Rangename2 + 'Max'] + entity2[Rangename2 + 'Min']) / 2 * 1.852

                dis = geodesic((Lat1, Lng1), (Lat2, Lng2)).km  # 单位km

                # if (dis < RangeAvg1 + RangeAvg2):
                if (dis < RangeMax1 + RangeMax2):
                    #打击范围与距离重合度 * 打击能力比 * 相对速度
                    # a = atan((Lng1-Lng2)/(Lat1-Lat2))
                    coov = ((RangeMax1 + RangeMax2 - dis)/dis) * (Pok2 / Pok1)
                    if coov > 0:
                        if uID1 not in coo:
                            coo[uID1] = []
                        coo[uID1].append((uID2, coov))
                else:
                    continue
    return coo


def get_scene(time_):
    db = DataBase("F:/716/DB3000_CMANO_CN.db3")
    entities = getEntities()
    scene = {}
    sceneH = {}
    for uID, entity in entities['H'].items():
        entityInfo = {}
        dynamicInfo = getDynamicInfo(uID, time_)
        entityname = dynamicInfo['PlantName']  # "J-20 Mighty Dragon"
        Icontype = dynamicInfo['Icontype']  # 'AIRCRAFT'
        tablename = et.entityType(Icontype)
        try:
            id = db.getID(tablename, entityname)
        except:  # 该时刻下该实体不存在
            continue
        staticInfo = db.getEntityInfo(id, tablename)
        if Icontype == "AIRCRAFT":
            staticInfo['PH'] = 90.0
        elif Icontype == "MINE_SWEEPER":
            staticInfo['PH'] = 180.0
        dynamicInfo.update(staticInfo)
        entityInfo = dynamicInfo
        sceneH[uID] = entityInfo

    sceneL = {}
    for uID, entity in entities['L'].items():
        entityInfo = {}
        dynamicInfo = getDynamicInfo(uID, time_)
        entityname = dynamicInfo['PlantName']  # "J-20 Mighty Dragon"
        Icontype = dynamicInfo['Icontype']  # 'AIRCRAFT'
        tablename = et.entityType(Icontype)
        try:
            id = db.getID(tablename, entityname)
        except:  # 该时刻下该实体不存在
            continue
        staticInfo = db.getEntityInfo(id, tablename)
        if Icontype == "AIRCRAFT":
            staticInfo['PH'] = 90.0
        elif Icontype == "MINE_SWEEPER":
            staticInfo['PH'] = 180.0
        dynamicInfo.update(staticInfo)
        entityInfo = dynamicInfo
        sceneL[uID] = entityInfo
    # 合并 sceneH和sceneL 到scene
    scene['H'] = sceneH
    scene['L'] = sceneL
    return scene


def get_taishi(scene_):
    cooH_ = computeCoordinationRel(scene_['H'])
    cooL_ = computeCoordinationRel(scene_['L'])
    thr_ = computeThreatenRel(scene_)
    return cooH_, cooL_, thr_


if __name__ == "__main__":
    db = DataBase(AppConfig.database_path)
    time = 0
    entities = getEntities()
    scene = {}
    sceneH = {}
    for uID, entity in entities['H'].items():
        entityInfo = {}
        dynamicInfo = getDynamicInfo(uID, time)
        entityname = dynamicInfo['PlantName']  # "J-20 Mighty Dragon"
        Icontype = dynamicInfo['Icontype']  # 'AIRCRAFT'
        tablename = et.entityType(Icontype)
        id = db.getID(tablename, entityname)
        staticInfo = db.getEntityInfo(id, tablename)
        if Icontype == "AIRCRAFT":
            staticInfo['status'] = 90.0
        elif Icontype == "MINE_SWEEPER":
            staticInfo['status'] = 180.0
        dynamicInfo.update(staticInfo)
        entityInfo = dynamicInfo
        sceneH[uID] = entityInfo

    sceneL = {}
    for uID, entity in entities['L'].items():
        entityInfo = {}
        dynamicInfo = getDynamicInfo(uID, time)
        entityname = dynamicInfo['PlantName']  # "J-20 Mighty Dragon"
        Icontype = dynamicInfo['Icontype']  # 'AIRCRAFT'
        tablename = et.entityType(Icontype)
        id = db.getID(tablename, entityname)
        staticInfo = db.getEntityInfo(id, tablename)
        if Icontype == "AIRCRAFT":
            staticInfo['status'] = 90.0
        elif Icontype == "MINE_SWEEPER":
            staticInfo['status'] = 180.0
        dynamicInfo.update(staticInfo)
        entityInfo = dynamicInfo
        sceneL[uID] = entityInfo

    # 计算协同关系
    cooH = computeCoordinationRel(sceneH)
    cooL = computeCoordinationRel(sceneL)
    # 合并 sceneH和sceneL 到scene
    scene['H']=sceneH
    scene['L']=sceneL
    # 计算威胁关系
    thr = computeThreatenRel(scene)
    print("hello")
