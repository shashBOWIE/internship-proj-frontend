question = [1,11,13,17]



#West
NorthwestHillsArr = [];
CatMountainArr = [];
WestVeiwArr = [];
HighlandParkArr = [];
TarryTownArr = [];
RollingWoodArr = [];
WestLakeHillsArr = [];
EastOakHillArr = [];
BartonCreekArr = [];
RobRoyArr = [];
AustinLakeArr = [];
SteinerRanchArr = [];
SennaHillsArr = [];
LakePointeArr = [];
LakewayArr = [];
HudsonBendArr = [];
RiverPlaceArr = [];
ComancheTrailArr = [];
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
DawsonArr = [];
GalindoArr = [];
SouthLamarArr = [];
WestgateArr = [];
SiuthManchacaArr = [];
WestCongressArr = [];
BattleBendArr = [];
SweetBriarArr = [];
GarrisonParkArr = [];
CherryCreekArr = [];
ShadyHollowArr = [];

#SouthEast

RiversideArr = [];
PleasantValleyArr = [];
MontopolisArr = [];
ParkerLaneArr = [];
McKinneyArr = [];
FranklinParkArr = [];

#Central
OldWestAustinArr = [];
OldEnFieldArr = [];
WindsorRoadArr = [];
BrykerWoodsArr = [];
RosedaleArr = [];
TriangleStateArr = [];
HydeParkArr = [];
HancockArr = [];
UniOfTexArr = [];
DownTownArr = [];

#Northwest
GrandviewHillsArr = []
CanyonCreekArr = []
AndersonMillArr = []
GreatHillsArr = []
BalconesWoodsArr = []
AngusRanchArr = []
AveryRanchArr = []

#North
AllandaleArr = []
BrentwoodArr = []
NorthLoopArr = []
HighlandArr = []
CrestviewArr = []
NorthShoalCreekArr = []
WootenArr = []
NorthBurnetArr = []
NorthAustinCivicAssociationArr = []
GeorgianAcresArr = []
NorthLamarArr = []
GracyWoodsArr = []
LamplightVillageArr = []

#Northeast
WindsorParkArr = []
PecanSprings_SpringdaleArr = []
UniversityHillsArr = []
CoronadoHillsArr = []
StJohnsArr = []
HeritageHillsArr = []
WindsorHillsArr = []
CopperfieldArr = []

if question[0] == 1:
    res = sum(x == y for x, y in zip(question, NorthwestHillsArr))
    print("Summation of Identical elements : " + str(res))
