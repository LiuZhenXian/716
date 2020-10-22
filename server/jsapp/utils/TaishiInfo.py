import random
import math
# class DynamicInfo():
    # def __init__(self, uID,time):  # get Taishi info from 716
        # PlantName, fuel, damageper, OpsStatus, Alliance,\
        # Operating_medium, Icontype, Speed, Bearing, Lat, Lng, Alt, Cw, pitch,\
        # roll, BaseplatName, HullName, cStandBy, iIconLib, iVisible, maxSpeed = self.getDynamicInfo(uID,time)

        # info["ID"] = row[0]
        # info["Name"] = row[1]
        # info["Comments"] = row[2]
        # info["Length"] = row[3]
        # info["Span"] = row[4]
        # info["Height"] = row[5]
        # info["YearCommissioned"] = row[6]
        # info["YearDecommissioned"] = row[7]
        # info["WeightEmpty"] = row[8]
        # info["WeightMax"] = row[9]
        # info["WeightPayload"] = row[10]
        # info["Crew"] = row[11]
        # info["Agility"] = row[12]
        # info["DamagePoints"] = row[13]
        # info["Category"] = row[14]
        # info["Type"] = row[15]
        # info["Country"] = row[16]
        # info["Service"] = row[17]
        # info["PhysicalSize"] = row[18]
        # info["RunwayLength"] = row[19]
        # info["CockpitVisibility"] = row[20]
        # info["EngineArmor"] = row[21]
        # info["FuselageArmor"] = row[22]
        # info["CockpitArmor"] = row[23]

        # self.PlantName = PlantName
        # self.fuel = fuel
        # self.damageper = damageper
        # self.OpsStatus = OpsStatus
        # self.Alliance = Alliance
        # self.Operating_medium = Operating_medium
        # self.Icontype = Icontype
        # self.Speed = Speed
        # self.Bearing = Bearing #航向
        # self.Lat = Lat #纬度
        # self.Lng = Lng #经度
        # self.Alt = Alt
        # self.Cw = Cw
        # self.pitch = pitch
        # self.roll = roll
        # self.BaseplatName = BaseplatName
        # self.HullName = HullName
        # self.cStandBy = cStandBy
        # self.iIconLib = iIconLib
        # self.iVisible = iVisible
        # self.maxSpeed = maxSpeed 改成上面形式


def generate_random_gps(base_log=None, base_lat=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    longitude = y + base_log
    latitude = x + base_lat
    # 这里是想保留10位小数
    loga = '%.10f' % longitude
    lata = '%.10f' % latitude
    return loga, lata


def getDynamicInfo(uID, time):
    # to do
    # 通过uID和time获得time时刻该实体的动态信息
    Info = {}
    PH = 0.
    Lng, Lat = 0, 0
    PlantName = ""
    Mission = ""
    status = ""
    if time == 0:  # 第0时刻初始化
        Icontype = 'AIRCRAFT'
        if uID == 'H1':
            PlantName = "J-20 Mighty Dragon"  # 2463
            Lng, Lat = 121.555512, 29.874471
            Mission = "护航"
            status = "起飞"
            PH = 90.0
        elif uID=='H2':
            PlantName = "J-20 Mighty Dragon"  # 2463
            Lng, Lat = 121.555512, 29.874471
            Mission = "打击"
            status = "起飞"
            PH = 90.0
        elif uID == 'H3':
            PlantName = "J-10C Vigorous Dragon"
            Lng, Lat = 121.555512, 29.874471                        # 2057
            Mission = "护航"
            status = "起飞"
            PH = 90.0
        elif uID == 'H4':
            PlantName = "Type 052D Luyang III [173 Changsha]"       # 2296
            Icontype = 'MINE_SWEEPER'
            Lng, Lat = 119.375145, 25.347994
            Mission = "打击"
            status = "启航"
            PH = 180.0
        elif uID == 'L1':
            PlantName = "CVN 72 Abraham Lincoln [Nimitz Class]"     # 2588
            Icontype = 'MINE_SWEEPER'
            Lng, Lat = 120.430186, 24.139915
            Mission = "打击"
            status = "启航"
            PH = 200.0
        elif uID == 'L2':
            PlantName = "CG 52 Bunker Hill [Ticonderoga Baseline 2, VLS]"  # 2859
            Icontype = 'MINE_SWEEPER'
            Lng, Lat = 120.417538, 24.16451
            Mission = "护航"
            status = "启航"
            PH = 180.0
        elif uID == 'L3':
            PlantName = "F-16V Blk 70/72 Falcon"                    # 4739
            Lng, Lat = 120.26497, 24.221274
            Mission = "打击"
            status = "起飞"
            PH = 90.0
        # Speed = 10*random.random()  #单位 m/s
        # i = random.randint(1,10)
        # Bearing = random.uniform(0,360) #math.sin(2*math.pi/i)
        # Lat ,Lng= generate_random_gps(base_log=120.7, base_lat=30, radius=1000000)

        Info['uID'] = uID
        Info['PlantName'] = PlantName
        Info['Icontype'] = Icontype
        # Info['Speed'] =Speed
        # Info['Bearing'] =Bearing
        Info['Lat'] = Lat
        Info['Lng'] = Lng
        Info['Mission'] = Mission
        Info['status'] = status
        Info['PH'] = PH
    elif time == 1:
        Icontype = 'AIRCRAFT'
        if uID == 'H1':
            PlantName = "J-20 Mighty Dragon"  # 2463
            Lng, Lat = 120.042513, 24.339065
            Mission = "护航"
            status = "伴随出动"
            PH = 90.0
        elif uID == 'H2':
            PlantName = "J-20 Mighty Dragon"  # 2463
            Lng, Lat = 120.029578, 24.343806
            Mission = "打击"
            status = "到达指定区域"
            PH = 90.0
        elif uID == 'H3':
            PlantName = "J-10C Vigorous Dragon"                # 2057
            Lng, Lat = 121.555512, 29.874471
            Mission = "护航"
            status = "到达指定区域"
            PH = 90.0
        elif uID == 'H4':
            PlantName = "Type 052D Luyang III [173 Changsha]"  # 2296
            Icontype = 'MINE_SWEEPER'
            Lng, Lat = 119.533678, 25.237705
            Mission = "打击"
            status = "到达指定区域"
            PH = 180.0
        elif uID == 'L1':
            PlantName = "CVN 72 Abraham Lincoln [Nimitz Class]"  # 2588
            Icontype = 'MINE_SWEEPER'
            Lng, Lat = 120.290985, 24.217583
            Mission = "打击"
            status = "到达指定区域"
            PH = 200.0
        elif uID == 'L2':
            PlantName = "CG 52 Bunker Hill [Ticonderoga Baseline 2, VLS]"  # 2859
            Icontype = 'MINE_SWEEPER'
            Lng, Lat = 120.288757, 24.241375
            Mission = "护航"
            status = "护航"
            PH = 180.0
        elif uID == 'L3':
            PlantName = "F-16V Blk 70/72 Falcon"  # 4739
            Lng, Lat = 120.043232, 24.331031
            Mission = "打击"
            status = "到达指定区域"
            PH = 90.0

        Info['uID'] = uID
        Info['PlantName'] = PlantName
        Info['Icontype'] = Icontype
        Info['Lat'] = Lat
        Info['Lng'] = Lng
        Info['Mission'] = Mission
        Info['status'] = status
        Info['PH'] = PH
    elif time == 2:
        Icontype = 'AIRCRAFT'
        if uID == 'H1':
            PlantName = "J-20 Mighty Dragon"  # 2463
            Lng, Lat = 120.042513, 24.339065
            Mission = "护航"
            status = "伴随出动"
            PH = 0.0
        elif uID == 'H2':
            PlantName = "J-20 Mighty Dragon"  # 2463
            Lng, Lat = 120.019085, 24.354801
            Mission = "打击"
            status = "开火"
            PH = 90.0
        elif uID == 'H3':
            PlantName = "J-10C Vigorous Dragon"
            Lng, Lat = 121.555512, 29.874471   # 2057
            Mission = "护航"
            status = "开火"
            PH = 90.0
        elif uID == 'H4':
            PlantName = "Type 052D Luyang III [173 Changsha]"  # 2296
            Icontype = 'MINE_SWEEPER'
            Lng, Lat = 119.690055, 25.103758
            Mission = "打击"
            status = "开火"
            PH = 180.0
        elif uID == 'L1':
            PlantName = "CVN 72 Abraham Lincoln [Nimitz Class]"  # 2588
            Icontype = 'MINE_SWEEPER'
            Lng, Lat = 120.172121, 24.297179
            Mission = "打击"
            status = "开火"
            PH = 200.0
        elif uID == 'L2':
            PlantName = "CG 52 Bunker Hill [Ticonderoga Baseline 2, VLS]"  # 2859
            Icontype = 'MINE_SWEEPER'
            Mission = "护航"
            Lng, Lat = 120.170756, 24.318782
            status = "到达指定区域"
            PH = 180.0
        elif uID == 'L3':
            PlantName = "F-16V Blk 70/72 Falcon"  # 4739
            Lng, Lat = 120.024978, 24.348941
            Mission = "打击"
            status = "开火"
            PH = 90.0
        Info['uID'] = uID
        Info['PlantName'] = PlantName
        Info['Icontype'] = Icontype
        Info['Lat'] = Lat
        Info['Lng'] = Lng
        Info['Mission'] = Mission
        Info['status'] = status
        Info['PH'] = PH
    elif time == 3:
        Icontype = 'AIRCRAFT'
        if uID == 'H1':
            PlantName = "J-20 Mighty Dragon"  # 2463
            Lng, Lat = 120.042513, 24.339065
            Mission = "护航"
            status = "伴随出动"
            PH = 0.0
        elif uID == 'H2':
            PlantName = "J-20 Mighty Dragon"  # 2463
            Lng, Lat = 120.022319, 24.354143
            Mission = "打击"
            status = "返航"
            PH = 90.0
        elif uID == 'H3':
            PlantName = "J-10C Vigorous Dragon"
            Lng, Lat = 121.555512, 29.874471   # 2057
            Mission = "护航"
            status = "返航"
            PH = 90.0
        elif uID == 'H4':
            PlantName = "Type 052D Luyang III [173 Changsha]"  # 2296
            Icontype = 'MINE_SWEEPER'
            Lng, Lat = 119.809637, 24.986433
            Mission = "打击"
            status = "返航"
            PH = 180.0
        elif uID == 'L1':
            PlantName = "CVN 72 Abraham Lincoln [Nimitz Class]"  # 2588
            Icontype = 'MINE_SWEEPER'
            Lng, Lat = 120.067594, 24.327409
            Mission = "打击"
            status = "返航"
            PH = 200.0
        elif uID == 'L2':
            PlantName = "CG 52 Bunker Hill [Ticonderoga Baseline 2, VLS]"  # 2859
            Icontype = 'MINE_SWEEPER'
            Lng, Lat = 120.070253, 24.357369
            Mission = "护航"
            status = "返航"
            PH = 180.0
        elif uID == 'L3':
            PlantName = "F-16V Blk 70/72 Falcon"  # 4739
            Lng, Lat = 120.024978, 24.348941
            Mission = "打击"
            status = "返航"
            PH = 0.0
        Info['uID'] = uID
        Info['PlantName'] = PlantName
        Info['Icontype'] = Icontype
        Info['Lat'] = Lat
        Info['Lng'] = Lng
        Info['Mission'] = Mission
        Info['status'] = status
        Info['PH'] = PH
    return Info


# 根据时刻从ZC中获取数据
def getEntities():
    # to do
    # 获得time=0时的场景实体
    entities = {}
    entities['L'] = {
        'L1': '林肯号航母',
        'L2': '提康德罗加导弹舰',
        'L3': 'F-16'
    }
    entities['H'] = {
        'H1': 'J-20',
        'H2': 'J-20',
        'H3': 'J-10C',
        'H4': '052D'
    }
    return entities


