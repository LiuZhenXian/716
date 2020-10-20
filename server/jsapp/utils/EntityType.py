#716¸øicontype Ó³Éäµ½ table
def entityType(Icontype,type='tablename'):

    tablename = ''
    Pok =''
    Range =''
    if Icontype=="AIRCRAFT":
        tablename = 'DataAirCraft'
        Pok = 'AirPoK'
        Range = 'AirRange'
    elif Icontype=='MINE_SWEEPER':
        tablename = 'DataShip'
        Pok = 'SurfacePoK'
        Range = 'SurfaceRange'
    elif Icontype == 'MISSILE':
        tablename = 'DataMount'
    #²îÂ½µØLand


    if type == 'tablename':
        return tablename
    elif type == 'Pok':
        return Pok
    elif type == 'Range':
        return Range


