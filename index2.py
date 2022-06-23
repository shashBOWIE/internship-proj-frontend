
# Python3 code to demonstrate working of
# Identical element summation in lists
# using sum() + zip()

# initialize lists
question = [1,14,13,17]
test_list2 = [1,11,13,17]

# printing original lists
div1 ={"Allandale": [1,12,14,16], "North Loop": [1,13,15,17], "Crestview": [1,12,14,16], "North Burnet": [1,13,15,17], "GracyWoods": [1,12,14,16]}

div2 ={ 'BartonHillsArr' : [2],
    'ZilkerArr' : [2],
    'BouldinCreekArr' : [2],
    'SouthCongressArr' : [2],
    'TravisHeightsArr' : [2],
    'StEdwardsArr' : [2],
    'SouthLamarArr' : [2],
    'WestCongressArr' : [2],
    'BattleBendArr' : [2],
    'WindsorHillsArr' : [2],
    'GreatHillsArr' : [2],
    'BalconesWoodsArr' : [2],
    'AveryRanchArr': [2]}

div3 ={'NorthwestHillsArr' : [3],
    'CatMountainArr' : [3],
    'HighlandParkArr' : [3],
    'TarryTownArr' : [3],
    'RollingWoodArr' : [3],
    'WestLakeHillsArr' : [3],
    'EastOakHillArr' : [3],
    'BartonCreekArr' : [3],
    'RobRoyArr' : [3],
    'AustinLakeArr' : [3],
    'SteinerRanchArr' : [3],
    'RiverPlaceArr' : [3],
    'JesterEstatesArr' : [3],
    'OldWestAustinArr' : [3],
    'OldEnFieldArr' : [3],
    'BrykerWoodsArr' : [3],
    'RosedaleArr' : [3],
    'TriangleStateArr' : [3],
    'HydeParkArr' : [3],
    'HancockArr' : [3],
    'UniOfTexArr' : [3],
    'DownTownArr' : [3],
    'WestOakArr' : [3],
    'CircleCeeRanchArr' : [3],
    'BelterraArr' : [3],
    'HighpointArr' : [3]}


for arp in div3:
    print(div3[arp])

neighboRet = []

#compare arrays in list with base questionare
# if greater than 2 will add neighborhood to list

if question[0] == 1:
    for key, values in div1.items():
        stoVal1 = len(set(question).intersection(values))
        print(stoVal1)
        if stoVal1 > 2:
            print(key)
            neighboRet.append(key)

if question[0] == 2:
    for key, values in div2.items():
        stoVal1 = len(set(question).intersection(values))
        print(stoVal1);
        if stoVal1 > 2:
            print(key)
            neighboRet.append(key)

if question[0] == 3:
    for key, values in div3.items():
        stoVal1 = len(set(question).intersection(values))
        print(stoVal1);
        if stoVal1 > 2:
            print(key)
            neighboRet.append(key)
