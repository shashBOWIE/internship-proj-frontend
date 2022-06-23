# initialize lists

question = [1,14,13,17]
test_list2 = [1,11,13,17]

#Initialize Neighborhoods With Income
neighborhoods = {

    # North Austin & South East Austin

    "AllandaleArr": [1], 
    "NorthLoopArr": [1], 
    "CrestviewArr": [1], 
    "NorthBurnetArr": [1],
    "GracyWoodsArr": [1],
    "HollyArr" : [1],
    "ChestnutArr" : [1],
    "HighlandArr" : [1],
    "LakewayArr" : [1],

    # South Austin, Northeast Austin, Northwest Austin

    'BartonHillsArr': [2],
    'ZilkerArr': [2],
    'BouldinCreekArr': [2],
    'SouthCongressArr': [2],
    'TravisHeightsArr': [2],
    'SaintEdwardsArr': [2],
    'SouthLamarArr': [2],
    'WestCongressArr': [2],
    'BattleBendArr': [2],
    'WindsorHillsArr': [2],
    'GreatHillsArr': [2],
    'BalconesWoodsArr': [2],
    'AveryRanchArr': [2],
    'CentralEastAustinArr' : [2],

    # West, Southwest, and Central Austin

    'NorthwestHillsArr': [3],
    'CatMountainArr': [3],
    'HighlandParkWestBalconesArr': [3],
    'TarrytownArr': [3],
    'RollingwoodArr': [3],
    'WestLakeHillsArr': [3],
    'EastOakHillArr': [3],
    'BartonCreekArr': [3],
    'RobRoyArr': [3],
    'AustinLakeEstatesArr': [3],
    'SteinerRanchArr': [3],
    'RiverPlaceArr': [3],
    'JesterEstatesArr': [3],
    'OldWestAustinArr': [3],
    'OldEnFieldArr': [3],
    'BrykerWoodsArr': [3],
    'RosedaleArr': [3],
    'TriangleStateArr': [3],
    'HydeParkArr': [3],
    'HancockArr': [3],
    'UniversityofTexasArr': [3],
    'DowntownArr': [3],
    'WestOakHillArr': [3],
    'CircleCRanchArr': [3],
    'BelterraArr': [3],
    'HighpointeArr': [3],
    'MuellerArr' : [3],
    'LostCreekArr' : [3],
    'McKinneyArr' : [3],
    'EastCesarChavezArr' : [3],
    'GovalleArr' : [3],
    'BattleBendSpringsArr' : [3],
    'AngusValleyArr' : [3]
}

#update neighborhoods using script
exec(open("webscraper.py").read())


#Create Recommendations ===========================

neighboRet = []

for key, values in neighborhoods.items():

    if question[0] == 1 and values[0] == 1:
        stoVal1 = len(set(question).intersection(values))
        if stoVal1 > 2:
            neighboRet.append(key)

    if question[0] == 2 and values[0] == 2:
        stoVal1 = len(set(question).intersection(values))
        if stoVal1 > 2:
            neighboRet.append(key)

    if question[0] == 3 and values[0] == 3:
        stoVal1 = len(set(question).intersection(values))
        if stoVal1 > 2:
            neighboRet.append(key)



