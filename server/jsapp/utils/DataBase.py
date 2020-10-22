#coding=utf-8
import sqlite3

def Merge(dict1, dict2):
    return(dict2.update(dict1))

class DataBase():
    def __init__(self,dbname):#connectdb
        self.dbname = dbname
        self.openConn()

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def openConn(self):
        conn = sqlite3.connect(self.dbname)
        conn.row_factory = self.dict_factory
        print('sqlite open')
        self.conn = conn

    def closeConn(self):
        self.conn.close()

        # check all tables
    # def getAllTables(self):
    #     cur = self.conn.cursor()
    #     cur.execute("select name from sqlite_master where type='table' order by name")
    #     print(cur.fetchall())

    def getID(self,tablename,entityname):
        c = self.conn.cursor()
        #"SELECT * FROM DataShip WHERE Name='Type 054A Jiangkai II [530 Xuzhou]' ORDER BY YearCommissioned desc limit 1;"
        querysql = "SELECT ID FROM {tablename} WHERE Name='{entityname}' ORDER BY YearCommissioned desc limit 1".format(tablename=tablename,entityname=entityname)
        # querysql = "SELECT ID FROM ? WHERE Name='?' ORDER BY YearCommissioned desc limit 1".format(tablename=tablename,entityname=entityname)
        cursor = c.execute(querysql)
        for row in cursor:
            id = row['ID']
        return id

    def getEntityInfo(self,id,tablename):
        c = self.conn.cursor()
        info1 = {}
        info2 = {}
        querysql_quan = "SELECT \
                    a.ID, \
                    a.Name,\
                    a.Comments,\
                    a.Length,\
                    a.Span,\
                    a.Height,\
                    a.YearCommissioned,\
                    a.YearDecommissioned,\
                    a.WeightEmpty,\
                    a.WeightMax,\
                    a.WeightPayload,\
                    a.Crew,\
                    a.Agility,\
                    a.DamagePoints,\
                    b.Description AS Category,\
                    c.Description AS Type,\
                    d.Description AS Country,\
                    e.Description AS Service,\
                    f.Description AS PhysicalSize, \
                    g.Description AS RunwayLength, \
                    h.Description AS CockpitVisibility, \
                    i.Description AS EngineArmor,\
                    j.Description AS FuselageArmor,\
                    k.Description AS CockpitArmor,\
                    ( \
                    SELECT GROUP_CONCAT( EnumAircraftCode.Description ) AS Codes \
                    FROM \
                        DataAircraftCodes \
                        LEFT JOIN DataAircraft\
                        LEFT JOIN EnumAircraftCode \
                    WHERE \
                        DataAircraft.ID = {id}\
                        AND DataAircraft.ID = DataAircraftCodes.ID \
                        AND DataAircraftCodes.CodeID = EnumAircraftCode.ID\
                    ) AS Codes,\
                    (\
                    SELECT \
                       GROUP_CONCAT( DataAircraftComms.ComponentID ) AS ID\
                    FROM\
                       DataAircraft\
                       LEFT JOIN DataAircraftComms\
                    WHERE\
                        DataAircraft.ID = {id}\
                        AND DataAircraft.ID = DataAircraftComms.ID\
                    ) AS CommIDs,\
                    (\
                    SELECT\
                        GROUP_CONCAT( DataFuel.ID ) AS ID\
                    FROM\
                        DataAircraft\
                        LEFT JOIN DataAircraftFuel\
                        LEFT JOIN DataFuel\
                    WHERE\
                        DataAircraft.ID = {id} \
                        AND DataAircraft.ID = DataAircraftFuel.ID\
                        AND DataAircraftFuel.ComponentID = DataFuel.ID\
                    ) AS FuelIDs,\
                    (\
                    SELECT\
                        GROUP_CONCAT( DataLoadout.ID ) AS ID\
                    FROM\
                        DataAircraft\
                        LEFT JOIN DataAircraftLoadouts\
                        LEFT JOIN DataLoadout\
                    WHERE\
                        DataAircraft.ID = {id} \
                        AND DataAircraft.ID = DataAircraftLoadouts.ID\
                        AND DataAircraftLoadouts.ComponentID = DataLoadout.ID\
                    ) AS LoadoutIDs,\
                    (\
                    SELECT\
                        GROUP_CONCAT( DataMount.ID ) AS ID\
                    FROM\
                        DataAircraft\
                        LEFT JOIN DataAircraftMounts\
                        LEFT JOIN DataMount\
                    WHERE\
                        DataAircraft.ID = {id}\
                        AND DataAircraft.ID = DataAircraftMounts.ID\
                        AND DataAircraftMounts.ComponentID = DataMount.ID\
                    ) AS MountIDs,\
                    (\
                    SELECT\
                        GROUP_CONCAT( DataPropulsion.ID ) AS ID\
                    FROM\
                        DataAircraft\
                        LEFT JOIN DataAircraftPropulsion\
                        LEFT JOIN DataPropulsion\
                    WHERE\
                        DataAircraft.ID = {id}\
                        AND DataAircraft.ID = DataAircraftPropulsion.ID\
                        AND DataAircraftPropulsion.ComponentID = DataPropulsion.ID\
                    ) AS PropulsionIDs,\
                    (\
                    SELECT\
                        GROUP_CONCAT( DataSensor.ID ) AS ID\
                    FROM\
                        DataAircraft\
                        LEFT JOIN DataAircraftSensors\
                        LEFT JOIN DataSensor\
                    WHERE\
                        DataAircraft.ID = {id}\
                        AND DataAircraft.ID = DataAircraftSensors.ID\
                        AND DataAircraftSensors.ComponentID = DataSensor.ID\
                    ) AS SensorIDs,\
                    (\
                    SELECT\
                        GROUP_CONCAT( EnumSignatureType.Description )\
                    FROM\
                        DataAircraft\
                        LEFT JOIN DataAircraftSignatures\
                        LEFT JOIN EnumSignatureType\
                    WHERE\
                        DataAircraft.ID = {id}\
                        AND DataAircraft.ID = DataAircraftSignatures.ID\
                        AND DataAircraftSignatures.Type = EnumSignatureType.ID\
                    ) AS Signatures\
                FROM\
                    DataAircraft AS a\
                    LEFT JOIN EnumAircraftCategory AS b\
                    LEFT JOIN EnumAircraftType AS c\
                    LEFT JOIN EnumOperatorCountry AS d\
                    LEFT JOIN EnumOperatorService AS e\
                    LEFT JOIN EnumAircraftPhysicalSize AS f\
                    LEFT JOIN EnumAircraftRunwayLength AS g\
                LEFT JOIN EnumAircraftCockpitVisibility AS h\
                    LEFT JOIN EnumArmorType AS i\
                    LEFT JOIN EnumArmorType AS j\
                    LEFT JOIN EnumArmorType AS k\
                WHERE\
                    a.ID = {id}\
                    AND a.Category = b.ID\
                    AND a.Type = c.ID\
                    AND a.OperatorCountry = d.ID\
                    AND a.OperatorService = e.ID\
                    AND a.PhysicalSizeCode = f.ID\
                    AND a.RunwayLengthCode = g.ID\
                    AND a.Visibility = h.ID\
                    AND a.AircraftEngineArmor = i.ID\
                    AND a.AircraftFuselageArmor = j.ID\
                    AND a.AircraftCockpitArmor = k.ID".format(id=id)
        if tablename == 'DataAirCraft':
            querysql_Mount="SELECT a.ID,a.Name,a.Comments,a.Length,a.Span,a.Height,a.YearCommissioned,a.YearDecommissioned,a.WeightEmpty,a.WeightMax,\
                    a.WeightPayload,a.Crew,a.Agility,a.DamagePoints, \
                    b.Description AS Category, \
                    c.Description AS Type, \
                    d.Description AS PhysicalSize, \
                    e.Description AS RunwayLength, \
                    f.Description AS CockpitVisibility \
                  FROM \
                    DataAircraft AS a\
                    LEFT JOIN EnumAircraftCategory AS b\
                    LEFT JOIN EnumAircraftType AS c\
                    LEFT JOIN EnumAircraftPhysicalSize AS d\
                    LEFT JOIN EnumAircraftRunwayLength AS e\
                    LEFT JOIN EnumAircraftCockpitVisibility AS f\
                  WHERE \
                    a.ID = {id}\
                    AND a.Category = b.ID\
                    AND a.Type = c.ID\
                    AND a.PhysicalSizeCode = d.ID\
                    AND a.RunwayLengthCode = e.ID\
                    AND a.Visibility = f.ID ".format(id=id)
            querysql_Pok = "SELECT	DataWeapon.AirPoK AS AirPoK,\
                                DataWeapon.SurfacePoK AS SurfacePoK,\
                                DataWeapon.LandPoK AS LandPoK,\
                                DataWeapon.SubsurfacePoK AS SubsurfacePoK,\
                                DataWeapon.AirRangeMax AS AirRangeMax,\
                                DataWeapon.AirRangeMin AS AirRangeMin,\
                                DataWeapon.SurfaceRangeMax AS SurfaceRangeMax,\
                                DataWeapon.SurfaceRangeMin AS SurfaceRangeMin,\
                                DataWeapon.LandRangeMax AS LandRangeMax,\
                                DataWeapon.LandRangeMin AS LandRangeMin,\
                                DataWeapon.SubsurfaceRangeMax AS SubsurfaceRangeMax,\
                                DataWeapon.SubsurfaceRangeMin AS SubsurfaceRangeMin\
                            FROM\
                                DataAircraft\
                                LEFT JOIN DataAircraftMounts\
                                LEFT JOIN DataMount \
                                LEFT JOIN DataMountWeapons\
                                LEFT JOIN DataWeaponRecord\
                                LEFT JOIN DataWeapon\
                            WHERE\
                                DataAircraft.ID = {id} \
                                AND DataAircraft.ID = DataAircraftMounts.ID \
                                AND DataAircraftMounts.ComponentID = DataMount.ID \
                                AND DataMount.ID = DataMountWeapons.ID \
                                AND DataMountWeapons.ComponentID = DataWeaponRecord.ID \
                                AND DataWeaponRecord.ComponentID = DataWeapon.ID\
                            ORDER BY DataWeapon.ID desc limit 1".format(id=id)
            cursor_Mount = c.execute(querysql_Mount)

            for row in cursor_Mount:
                info1 = row
                break
            cursor_Pok = c.execute(querysql_Pok)

            for row in cursor_Pok:
                info2 = row
                break

        elif tablename=="DataShip":
            querysql_Mount ="SELECT \
                                a.ID,\
                                a.Name,\
                                a.Comments,\
                                a.Length,\
                                a.Beam,\
                                a.Height,\
                                a.YearCommissioned,\
                                a.YearDecommissioned,\
                                a.DisplacementEmpty,\
                                a.DisplacementStandard,\
                                a.DisplacementFull,\
                                a.Crew,\
                                a.DamagePoints,\
                                b.Description AS Category,\
                                c.Description AS Type,\
                                d.Description AS PhysicalSize\
                            FROM\
                                DataShip	AS a\
                                LEFT JOIN EnumShipCategory AS b\
                                LEFT JOIN EnumShipType AS c\
                                LEFT JOIN EnumShipPhysicalSize AS d\
                            WHERE\
                                a.ID = {id} \
                                AND a.Category = b.ID \
                                AND a.Type = c.ID \
                                AND a.PhysicalSizeCode = d.ID;".format(id=id)
            querysql_Pok = "SELECT DataWeapon.AirPoK AS AirPoK,\
                            DataWeapon.SurfacePoK AS SurfacePoK,\
                            DataWeapon.LandPoK AS LandPoK,\
                            DataWeapon.SubsurfacePoK AS SubsurfacePoK,\
                            DataWeapon.AirRangeMax AS AirRangeMax,\
                            DataWeapon.AirRangeMin AS AirRangeMin,\
                            DataWeapon.SurfaceRangeMax AS SurfaceRangeMax,\
                            DataWeapon.SurfaceRangeMin AS SurfaceRangeMin,\
                            DataWeapon.LandRangeMax AS LandRangeMax,\
                            DataWeapon.LandRangeMin AS LandRangeMin,\
                            DataWeapon.SubsurfaceRangeMax AS SubsurfaceRangeMax,\
                            DataWeapon.SubsurfaceRangeMin AS SubsurfaceRangeMin\
                        FROM\
                            DataShip\
                            LEFT JOIN DataShipMounts\
                            LEFT JOIN DataMount \
                            LEFT JOIN DataMountWeapons\
                            LEFT JOIN DataWeaponRecord\
                            LEFT JOIN DataWeapon\
                        WHERE\
                            DataShip.ID = {id} \
                            AND DataShip.ID = DataShipMounts.ID \
                            AND DataShipMounts.ComponentID = DataMount.ID \
                            AND DataMount.ID = DataMountWeapons.ID \
                            AND DataMountWeapons.ComponentID = DataWeaponRecord.ID \
                            AND DataWeaponRecord.ComponentID = DataWeapon.ID\
                        ORDER BY DataWeapon.ID desc limit 1;".format(id=id)
            cursor_Mount = c.execute(querysql_Mount)
            for row in cursor_Mount:
                info1 = row
                break

            cursor_Pok = c.execute(querysql_Pok)
            for row in cursor_Pok:
                info2 = row
                break

        else:
            pass
        info1.update(info2)
        list =['AirPoK', 'SurfacePoK', 'LandPoK', 'SubsurfacePoK', 'AirRangeMax','AirRangeMin', 'SurfaceRangeMax', 'SurfaceRangeMin',
               'LandRangeMax', 'LandRangeMin','SubsurfaceRangeMax', 'SubsurfaceRangeMin']
        alllist =['uID', 'PlantName','Icontype', 'Speed', 'Bearing','Lat', 'Lng', 'ID','Name', 'Comments','Length', 'Beam', 'Height',
                  'YearCommissioned', 'YearDecommissioned','DisplacementEmpty', 'DisplacementStandard', 'DisplacementFull', 'Crew',
                  'DamagePoints', 'Category', 'Type', 'PhysicalSize','AirPoK', 'SurfacePoK', 'LandPoK', 'SubsurfacePoK', 'AirRangeMax',
                  'AirRangeMin', 'SurfaceRangeMax', 'SurfaceRangeMin', 'LandRangeMax', 'LandRangeMin','SubsurfaceRangeMax', 'SubsurfaceRangeMin']
        # {'uID': 'L8', 'PlantName': 'DDG 124 Harvey C. Barnum Jr. [Arleigh Burke Flight III]',
        #  'Icontype': 'MINE_SWEEPER', 'Speed': 3.3891035365416555, 'Bearing': 0.8660254037844387,
        #  'Lat': '118.9202166816', 'Lng': '36.2019260977', 'ID': 2718,
        #  'Name': 'DDG 124 Harvey C. Barnum Jr. [Arleigh Burke Flight III]', 'Comments': 'Exact weapons fit unknown',
        #  'Length': 155.2, 'Beam': 20.4, 'Height': 0.0, 'YearCommissioned': 2022, 'YearDecommissioned': 0,
        #  'DisplacementEmpty': 0, 'DisplacementStandard': 8500, 'DisplacementFull': 9217, 'Crew': 315,
        #  'DamagePoints': 1270, 'Category': 'ˮ��ս����ͧ', 'Type': 'DDG - ��������', 'PhysicalSize': '������ͻ��ͷ (45.1-200m)',
        #  'AirPoK': 90.0, 'SurfacePoK': 95.0, 'LandPoK': 0.0, 'SubsurfacePoK': 0.0, 'AirRangeMax': 130.0,
        #  'AirRangeMin': 4.0, 'SurfaceRangeMax': 130.0, 'SurfaceRangeMin': 4.0, 'LandRangeMax': 0.0, 'LandRangeMin': 0.0,
        #  'SubsurfaceRangeMax': 0.0, 'SubsurfaceRangeMin': 0.0}
        for label in list:
            if label not in info1:
                info1[label]= 0.0
        return info1

