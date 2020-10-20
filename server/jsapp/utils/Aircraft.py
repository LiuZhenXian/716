# import AircraftFuel, AircraftLoadouts, AircraftMounts

class Aircraft(): # 飞行器信息表
    def __init__(self, ID, Category, Type, Tag, Name, Length, Span, Height, DamagePoints,
                 FuelComponentID, FuelComponentNumber, LoadoutsComponentID, MountsComponentID, MountsComponentNumber):
        # FuelComponentID, FuelComponentNumber, LoadoutsComponentID, MountsComponentID, MountsComponentNumber(无)

        self.id = ID
        self.enumAircraftCategory = Category
        self.enumAircraftType = Type
        self.tag = Tag
        self.name = Name
        self.length = Length
        self.span = Span
        self.height = Height
        self.damagePoints = DamagePoints
        # self.fuel = AircraftFuel(self.id, FuelComponentID, FuelComponentNumber)
        # self.loadouts = AircraftLoadouts(self.id, LoadoutsComponentID)
        # self.mounts = AircraftMounts(self.id, MountsComponentID, MountsComponentNumber)


