question = [1,11,13,17]



#West
NorthwestHillsArr = [];
CatMountainArr = [];
HighlandParkArr = [];
TarryTownArr = [];
RollingWoodArr = [];
WestLakeHillsArr = [];
EastOakHillArr = [];
BartonCreekArr = [];
RobRoyArr = [];
AustinLakeArr = [];
SteinerRanchArr = [];
RiverPlaceArr = [];
JesterEstatesArr = [];

#SouthWest
WestOakArr = [];
CircleCeeRanchArr = [];
BelterraArr = [];
HighpointArr = [];

#South
BartonHillsArr = [];
ZilkerArr = [];
BouldinCreekArr = [];
SouthCongressArr = [];
TravisHeightsArr = [];
StEdwardsArr = [];
SouthLamarArr = [];
WestCongressArr = [];
BattleBendArr = [];

#SouthEast

McKinneyArr = [];

#Central
OldWestAustinArr = [];
OldEnFieldArr = [];
BrykerWoodsArr = [];
RosedaleArr = [];
TriangleStateArr = [];
HydeParkArr = [];
HancockArr = [];
UniOfTexArr = [];
DownTownArr = [];

#Northwest

GreatHillsArr = []
BalconesWoodsArr = []
AveryRanchArr = []

#North

AllandaleArr = []
NorthLoopArr = []
CrestviewArr = []
NorthBurnetArr = []
GracyWoodsArr = []


#Northeast

WindsorHillsArr = []


if question[0] == 1:
    res = sum(x == y for x, y in zip(question, test_list2))
    counting = int(str(res))
    print(counting)
    if counting > 2:
        print("hi")
