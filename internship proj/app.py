from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

import json


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

data = {
'AllandaleArr': [{
    'name' : "Allandale",
    'description' : """Allandale is in Travis County and is one of the best places to live in Texas. Living in Allandale offers residents an urban suburban mix feel and most residents own their homes. In Allandale there are a lot of bars, restaurants, coffee shops, and parks good for families and seniors.""",
    'Hurl' : 'https://www.redfin.com/neighborhood/165450/TX/Austin/Allandale',
    'url' : 'https://allandaleneighbor.com/'
}],
'BattleBendSpringsArr': [{
    'name' : "Battle Bend Springs",
    'description' : """Battle Bend Springs is a family-oriented neighborhood with a diverse population. The community is close knit and there are many neighborhood activities, as well as schools, parks, and a creek. It is conveniently close to the attractions of downtown and west Austin, such as Barton Springs and Zilker Park, by car and public bus.""",
    'Hurl' : 'https://www.realtor.com/realestateandhomes-search/Battle-Bend-Springs_Austin_TX',
    'url' : 'https://tribeza.com/love-thy-neighbor-battle-bend-springs/'
}],

'BalconesWoodsArr': [{
    'name' : "Balcone Woods",
    'description' : """Balcones Woods is a small community conveniently located near the major thoroughfares and shopping centers of north Austin. The neighborhood was developed in the 1970s and early 80s and most of the homes here were built around that time. Although many people own their homes, there are also many apartments and rental properties.
The neighborhood offers amenities including a community center, pool, park, and tennis courts. The area is close to the high-tech centers and employers of north Austin and not far from downtown. The proximity to the local highways gives ready access to other parts of the city.
""",
'Hurl' : 'https://www.redfin.com/neighborhood/233238/TX/Austin/Balcones-Woods/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.maac.com/texas/austin/maa-balcones-woods/?gclid=CjwKCAjwoMSWBhAdEiwAVJ2ndpscfrzEftZSPilMLQm9hwE56_3CkQsYSPjk3qRWSmk22P6X1gx-fRoCjYQQAvD_BwE&gclsrc=aw.ds'
}],

'AveryRanchArr': [{
    'name' : "Avery Ranch",
    'description' : """Avery Ranch is a planned community in far northwest Austin, one of the fastest-growing areas of town (and the U.S.). With 1,800 acres and 4,000 homes, Avery Ranch is one of the larger neighborhoods, and has a range of houses and amenities to match. Many of the homes have views of the surrounding countryside, as well as large windows and landscaped back yards.
Neighborhood amenities include five community centers, hike and biking trails, pool, and a golf club. Avery Ranch is 20 minutes' commute from downtown Austin and close to the high-tech companies of north Austin. Residents have access to the top-rated Round Rock and Leander school districts.""",
'Hurl' : 'https://www.redfin.com/neighborhood/342192/TX/New-Fairview/Avery-Ranch/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.averyranchhoa.com/'
}],

    'NorthLoopArr': [{
    'name' : "North Loop",
    'description' : """Austin's North Loop neighborhood is a unique part of town located just northeast of the University of Texas. North Loop's proximity to the university and mix of eclectic restaurants and shops makes it a popular local hangout among students and campus staff. """,
'Hurl' : '‘https://www.redfin.com/neighborhood/165944/TX/Austin/North-Loop',
    'url' : 'https://nextdoor.com/neighborhood/northlooptx--austin--tx/'
}],

    'CrestviewArr': [{
    'name' : "Crestveiw",
        'description' : """Like Allendale, Crestview is in Travis County and is one of the best places to live in Texas. Living in Crestview offers residents an urban suburban mix feel and most residents rent their homes. In Crestview there are a lot of bars, restaurants, coffee shops, and parks.""",
'Hurl' : 'https://www.redfin.com/neighborhood/172201/TX/Austin/Crestview',
    'url' : 'https://crestviewna.com/about/'
}],

    'NorthBurnetArr': [{
    'name' : "North Burnet",
        'description' : """North Burnet is an older neighborhood with some new, upscale, urban developments. The neighborhood has lots of deluxe apartments and condos, few detached homes and little green space, but several shopping centers, and many restaurants. """,
'Hurl' : 'https://www.redfin.com/neighborhood/174521/TX/Austin/North-Burnet',
    'url' : 'https://www.niche.com/places-to-live/n/north-burnet-austin-tx/'
    }],

    'GracyWoodsArr': [{
    'name' : "Gracy Woods",
        'description' : """Gracy Woods is a quiet, suburban neighborhood in far north Austin. There are several parks and abundant green spaces in the area and the residents love being intimate with nature. Shopping centers and restaurants are just to the north, many of the Austin high tech employers are just to the west, and the neighborhood is situated between two major local highways.""",
'Hurl' : 'https://www.redfin.com/neighborhood/175705/TX/Austin/Gracy-Woods',
    'url' : 'http://www.gracywoods.org/'
    }],

    'HollyArr': [{
    'name' : "Holly",
        'description' : """Holly is a neighborhood in East Austin, Texas, that was recently ranked No. 24 in Time Out's list of the 50 coolest neighborhoods in the world. It's close to downtown Austin and borders the Colorado River, making it the ideal location for all Austin has to offer.""",
'Hurl' : 'https://www.redfin.com/neighborhood/176772/TX/Austin/Holly',
    'url' : 'https://nextdoor.com/neighborhood/hollyneighborhood--austin--tx/'
    }],

    'ChestnutArr': [{
    'name' : "Chestnut",
        'description' : """Although most of the homes are older and modest in size, some new, larger houses are being built. The neighborhood is close enough to downtown and the University of Texas that residents can bike to either location.""",
'Hurl' : 'https://www.redfin.com/neighborhood/175864/TX/Austin/Chestnut',
    'url' : 'https://nextdoor.com/neighborhood/chestnutaustin--austin--tx/'
    }],

    'HighlandArr': [{
    'name' : "Highland",
        'description' : """Highland is a quiet, working-class neighborhood with modest, single-family homes. The neighborhood is probably best known for the Highland Mall, once a prominent shopping center that has fallen into disuse in recent years.Public transportation is also highly accessible. The neighborhood has some local eateries and a cinema, and just to the west are parks, ball fields, and playgrounds.""",
'Hurl' : 'https://www.redfin.com/neighborhood/163051/TX/Austin/Highland',
'url' : 'https://www.highlandneighborhood.org/city-resources'
}],




 'LakewayArr': [{
 'name' : "Lakeway",
    'description' : """Lakeway is a suburb of Austin with a population of 15,605. Lakeway is in Travis County and is one of the best places to live in Texas. Living in Lakeway offers residents a sparse suburban feel and most residents own their homes. In Lakeway there are a lot of parks.""",
'Hurl' : 'https://www.redfin.com/city/10451/TX/Lakeway',
    'url' : ' https://www.lakeway-tx.gov/31/Community'
}],

    'BartonHillsArr': [{
    'name' : "Barton Hills",
        'description' : """The area is safe and with access to a large park and top schools is a good place for young families. Barton Hills is a favorite area for many in which to live and hang out, because of the abundance of green spaces and the proximity to some of Austin's best amenities.""",
'Hurl' : 'https://www.redfin.com/neighborhood/168010/TX/Austin/Barton-Hills',
    'url' : 'https://bartonhills.org/'
}],

    'ZilkerArr': [{
    'name' : "Zilker Park",
        'description' : """Zilker is one of the most desirable areas for many locals to settle down. There are abundant greenspaces and parks just to the west, shopping and dining are within walking distance, and downtown is just to the north. """,
'Hurl' : 'https://www.redfin.com/neighborhood/174753/TX/Austin/Zilker',
    'url' : 'https://zilkerneighborhood.org/'
}],

    'BouldinCreekArr': [{
    'name' : "Bouldin Creek",
        'description' : """Bouldin Creek is still a safe and tranquil neighborhood that allows residents to bike or walk safely in the streets. When compared to closeby neighborhoods such as Barton Hills and Zilker, there aren't many large families with children. This area became more suitable for creative, young professionals and students. """,
'Hurl' : 'https://www.redfin.com/neighborhood/166182/TX/Austin/Bouldin-Creek',
    'url' : 'https://www.bouldincreek.org/'
    }],


 'SouthCongressArr': [{
 'name' : "South Congress",

    'description' : """South Congress epitomizes the hip, trendy ambiance of south Austin. It's possibly the
best-known neighborhood in Austin for its unique, local shops and boutiques, diners, coffee shops, and
lounges that line Congress Ave.The California-style food trucks that are now ubiquitous around town
appeared here first and have been spreading out to other parts of town. Crowded with pedestrians at
almost all hours, the neighborhood is a city hub and landmark, and a walkable exhibition of Austins
one-of-a-kind, slightly offbeat local character.""",
'Hurl' : 'https://www.redfin.com/neighborhood/176804/TX/Austin/South-Congress',
    'url' : 'https://nextdoor.com/neighborhood/southcongresstx--austin--tx/'
}],

    'TravisHeightsArr': [{
    'name' : "Travis Heights",
        'description' : """Travis Heights is one of the older Austin neighborhoods and one of the more exclusive and
affluent areas of south Austin. Old mansions and other homes, with sizable yards, along with a few
apartments are here. The area is conveniently located near the trendy shopping and dining districts of
South Congress Ave. There are also several major parks. The population spans a wide range of age
groups and occupations.""",
'Hurl' : 'https://www.redfin.com/neighborhood/50237/TX/Austin/Travis-Heights',
    'url' : 'https://nextdoor.com/neighborhood/travisheights--austin--tx/'
}],

    'SaintEdwardsArr': [{
    'name' : "Saint Edwards",
        'description' : """Saint Edwards is a residential community surrounding the beautiful campus of St. Edward's
University. Although a popular location for students, a mix of other residents also live here, including
artists, single young professionals, and families. Residents tend to be friendly and close-knit. Many
homes have well-maintained gardens. There are many local shops and restaurants in and near the
neighborhood. The neighborhood is bounded on three sides by major local highways and thoroughfares,
giving easy access to the rest of the city.""",
'Hurl' : 'https://www.redfin.com/neighborhood/175207/TX/Austin/St-Edwards',
    'url' : 'https://nextdoor.com/neighborhood/stedwardstx--austin--tx/'
}],

    'SouthLamarArr': [{
    'name' : "South Lamar",
        'description' : """South Lamar is a trendy neighborhood with many local shops, restaurants, and lounges. It is also
conveniently located just five minutes from downtown and very close to the parks and hiking/biking trails
around Barton Springs to the west. Although it is close to central Austin, crime here is relatively low. The
population is of mixed ethnicity and includes singles, families, students, and seniors. The area also has
top-rated schools.""",
'Hurl' : 'https://www.redfin.com/neighborhood/166914/TX/Austin/South-Lamar',
    'url' : 'https://southlamar.org/'
    }],

    'WestCongressArr': [{
    'name' : "West Congress",
        'description' : """West Congress is a small, ethnic, residential neighborhood bordering Hwy. 71 to the north. Many
modest, ranch-style homes and apartment complexes are here. Also many casual restaurants. The
neighborhood is popular among families and college students.""",
'Hurl' : 'https://www.redfin.com/neighborhood/171971/TX/Austin/West-Congress',
    'url' : 'https://nextdoor.com/neighborhood/westcongress--austin--tx/'
    }],

    'BattleBendArr': [{
    'name' : "Battle Bend",
        'description' : """Battle Bend Springs is a family-oriented neighborhood with a diverse population. The community
is close knit and there are many neighborhood activities, as well as schools, parks, and a creek. It is
conveniently close to the attractions of downtown and west Austin, such as Barton Springs and Zilker
Park, by car and public bus.""",
'Hurl' : 'https://www.realtor.com/realestateandhomes-search/Battle-Bend-Springs_Austin_TX',
    'url' : "https://tribeza.com/love-thy-neighbor-battle-bend-springs/"
    }],

    'WindsorHillsArr': [{
    'name' : "Windsor hills",
        'description' : """Windsor Hills is in many ways a classic suburban neighborhood, quiet, family-friendly, well-tended
homes and yards, and not much in the way of entertainment or nightlife. But it is attractive to young
families, as well as students and single professionals, because housing is inexpensive and it is easy to
commute by car or public transportation to other parts of the city. Although the neighborhood is largely
residential, there is shopping and casual dining nearby.""",
'Hurl' : 'https://www.redfin.com/neighborhood/172895/TX/Austin/Windsor-Hills',
    'url' : 'https://sites.google.com/site/windsorhillsna/'
    }],

    'GreatHillsArr': [{
    'name' : "Great Hills",
        'description' : """Great Hills is a suburban neighborhood conveniently located near two major local highways and a
shopping center.Great Hills is located next to an abundance of shopping and dining options, as well as a
hotel, cinema, bookstore, and several coffee shops. There are also two parks, a country club, a pool,
playground, and hiking and bike trails in the area. Residents include young professionals and couples,
families, and students. While there are not as many families here as in other neighborhoods, there are still
highly rated schools and kids' activities in the area.""",
'Hurl' : 'https://www.redfin.com/neighborhood/73213/FL/Clermont/Greater-Hills',
    'url' : 'https://sites.google.com/site/windsorhillsna/'
    }],

    'EastOakHillArr': [{
	  'name' : 'East Oak Hills',
        'description' : """East Oak Hill is one of the larger neighborhoods in Austin and stretches across a sizeable part of the southwest area of town, from MoPac to the Barton Hills Wilderness Park. It is nestled in the hill country and has many larger, relatively new homes, some with impressive views of the Texas hills and Lady Bird Lake.""",
'Hurl' : 'https://www.redfin.com/neighborhood/172414/TX/Austin/East-Oak-Hill/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.ohan.org/'
    }],

 'BartonCreekArr': [{
	  'name' : 'Barton Creek',
        'description' : """Barton Creek is one of the larger and older neighborhoods in Austin. Some of the homes date back to the start of the 20th Century, others to the 1920s, and many are quite large as well as old. About two-thirds of the area is greenspace, and the neighborhood is surrounded by the Barton Creek Greenbelt and Zilker Park, Austin's favorite city park. Barton Creek Square Mall is nearby with its luxury stores and restaurants, and students have access to top-rated schools.
""",
'Hurl' : 'https://www.redfin.com/city/21448/TX/Barton-Creek/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://bartonhills.org/'
    }],

 'RobRoyArr': [{
	  'name' : 'Rob Roy',
        'description' : """Rob Roy is an established, private neighborhood located on Hwy. 360 (Capital of Texas Hwy.), one of the main thoroughfares in west Austin. Rob Roy is one of Austin's largest private neighborhoods with high-end homes located on large lots overlooking the hill country. The neighborhood has mature trees, abundant green spaces, and meticulously maintained landscaping.""",
'Hurl' : 'https://www.redfin.com/neighborhood/231873/TX/Austin/Rob-Roy/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://nextdoor.com/neighborhood/robroytx--austin--tx/'
    }],

 'AustinLakeEstatesArr': [{
	  'name' : 'Austin Lake Estates',
        'description' : """Austin Lake Estates is an affluent neighborhood located on the banks of Lake Austin. It is a close-knit community with friendly people in which residents know and look out for each other. Although it has grown recently, along with the rest of the city, it retains its down-to-earth, community-oriented feel.
The neighborhood is just 20 minutes' drive from downtown Austin, and is also close to the shopping and dining of the Bee Caves area of west Austin. The neighborhood itself has many amenities related to the lake and outdoors, and has a park and ample green spaces. The area neighborhood association is active in maintaining the neighborhood's environment and facilities.""",
'Hurl' : 'https://www.realtor.com/realestateandhomes-search/Austin-Lake-Estates_Austin_TX',
    'url' : 'https://hoa-community.com/austin-lake-estates-hoa-austin-tx/'
    }],



 'SteinerRanchArr': [{
	  'name' : 'Steiner Ranch',
        'description' : """Steiner Ranch is a large master-planned community located in the hills and green spaces between Lake Austin and Lake Travis. It is adjacent to a major wildlife preserve and has many amenities in and around the neighborhood.
The neighborhood also contains shopping centers, restaurants, and highly rated schools. Steiner Ranch is close to a major west Austin highway and about a half hour drive to downtown.""",
'Hurl' : 'https://www.redfin.com/neighborhood/192272/TX/Austin/Steiner-Ranch/filter/include=forsale+mlsfsbo+construction',
    'url' : 'http://www.steinerranchhoa.org/'
    }],

 'RiverPlaceArr': [{
	  'name' : 'River Place',
        'description' : """River Place is a newer neighborhood located in a scenic spot in the Texas hill country. Although River Place does not have as many shopping and dining venues as some other neighborhoods, it has abundant green space and many options for outdoor recreation. Many homes have expansive views of the hills or green spaces in the neighborhood.
Residents have access to parks, miles of hiking and bike trails, a marina on Lake Austin for water recreation, and a golf course. The neighborhood is just off a major local highway for direct access to the rest of the city.""",
'Hurl' : 'https://www.redfin.com/neighborhood/165502/TX/Austin/Riverplace/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.riverplacehoa.org/'
    }],

 'JesterEstatesArr': [{
	  'name' : 'Jester Estates',
        'description' : """Jester Estates is a scenic, conveniently located neighborhood at the intersection of two major local highways and close to major shopping centers. Jester Estates has several neighborhood amenities including a pool and ball courts. There are shopping and dining options nearby.
The area is in the hill country and many homes have excellent views of the Colorado River and even downtown. The area has abundant green space for outdoor recreation and is close to the high-tech companies and shopping in north Austin.""",
'Hurl' : '',
    'url' : 'http://www.jesterhoa.com/'
    }],

 'OldWestAustinArr': [{
	  'name' : 'Old West Austin',
        'description' : """Old West Austin is a historic, centrally located neighborhood just north of Lady Bird Lake and just west of downtown. The neighborhood’s historic district dates back to the mid-1800s, shortly after the city of Austin was incorporated. The neighborhood is one of the most sought-after to live in, because of its convenient location and access to many amenities, including the lake, local hike and bike trails, and several parks.
Along with local shops and restaurants the neighborhood is adjacent to the numerous dining, shopping, and entertainment options offered by downtown and south Austin. Parking is next to impossible here, but public transportation is readily accessible.


""",
'Hurl' : 'https://www.redfin.com/neighborhood/233627/TX/Austin/Jester-Estates/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.owana.org/'
    }],

 'OldEnFieldArr': [{
	  'name' : 'Old Enfield',
        'description' : """Old Enfield is a historic neighborhood with elegant homes, large, well-furnished parks, top-performing schools, and a convenient location. The neighborhood is just west of the University of Texas campus and north of downtown, so residents can easily access the shopping and entertainment amenities of those areas. It also borders Hwy. 1 (MoPac) and Lamar Blvd., two major local thoroughfares, offering easy access to other parts of Austin.
As one of the most desirable and expensive neighborhoods in town, Old Enfield is home to some of Austin's most distinguished residents. There are also professional singles and families here including university faculty.""",
'Hurl' : 'https://www.redfin.com/neighborhood/165052/TX/Austin/Old-Enfield/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://nextdoor.com/neighborhood/oldenfield--austin--tx/'
    }],

 'BrykerWoodsArr': [{
	  'name' : 'Bryker Woods',
        'description' : """Bryker Woods is an established neighborhood in north central Austin with mostly older, smaller single-family homes. Located just a few minutes drive from downtown and the University of Texas, and with well-known local restaurants in the area, the neighborhood is popular for its convenient location and its small-town atmosphere in the middle of the city.
Residents enjoy plenty of green space with parks and two golf courses in the area. The neighborhood has its own elementary school. Bryker Woods has some longtime residents and some younger singles and families attracted to the relaxed, natural environment and good location.""",
'Hurl' : 'https://www.redfin.com/neighborhood/48027/TX/Austin/Bryker-Woods/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.brykerwoods.org/'
    }],

 'RosedaleArr': [{
	  'name' : 'Rosedale',
        'description' : """Rosedale is an older, comfortable, residential neighborhood in the northwest section of central Austin. The central part of the neighborhood has older, modest-sized homes and some new construction, while the outer sections have restaurants and shops.
The area has several major parks with a pool, playscapes, tennis courts, and athletic fields. The community is close-knit and the residents take an active part in maintaining the charming, historic feel to their neighborhood.
The neighborhood is conveniently located next to MoPac (Hwy. 1), one of the local highways, providing access to other parts of the city. The area is also not very far from downtown and the University of Texas. Public transportation is also ample here.""",
'Hurl' : 'https://www.redfin.com/neighborhood/170326/TX/Austin/Rosedale/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://rosedaleaustin.org/'
    }],

'TriangleStateArr': [{
	  'name' : 'Triangle State',
        'description' : """Triangle State is a newer, upscale, residential/commercial neighborhood in north central Austin. The neighborhood was designed to be largely self-contained with many amenities to appeal to younger, urban professional singles and couples.
The area has consists of luxury condos, homes, and apartments interspersed with shopping centers containing many fine restaurants, stores, and supermarkets. There are also cafes, bars, and other businesses. The area is close to the University of Texas and downtown, and public transportation is readily accessible.
Within the neighborhood are several large green spaces suitable for kids and pets.""",
'Hurl' : 'https://www.realtor.com/realestateandhomes-search/Triangle-State_Austin_TX',
    'url' : 'https://nextdoor.com/city/austin--tx/'
    }],


 'HydeParkArr': [{
	  'name' : 'Hyde Park',
        'description' : """Hyde Park is an older, historic neighborhood in Austin and one of the most desirable places to live for many because of its residential atmosphere, safety, sense of community, and convenient location.
Hyde Park is located close to the University of Texas and to downtown. The neighborhood is quiet and residential, with mostly single-family homes. There are not as many shops and restaurants as in some other areas, but there are many amenities in adjacent neighborhoods just a short walk or bus ride away. Residents consist mainly of families, graduate students, and professors.
""",
'Hurl' : 'https://www.redfin.com/neighborhood/172898/TX/Austin/Hyde-Park/filter/include=forsale+mlsfsbo+construction',
    'url' : 'http://www.austinhydepark.org/'
    }],

 'HancockArr': [{
	  'name' : 'Hancock',
        'description' : """Hancock is a comfortable, safe, residential neighborhood conveniently located just west of I-35 and north of the University of Texas and downtown. Despite being close to the center of the city, the neighborhood is quiet, with many single-family homes on streets lined with mature trees.
The area also has parks, bike-friendly streets, an abundance of green space. Shopping, restaurants, fitness centers, and live music are readily available in the neighborhood, and public transportation is easily accessible.
The neighborhood is popular with families, university students and faculty, and professionals who work downtown.
""",
'Hurl' : 'https://www.redfin.com/neighborhood/171500/TX/Austin/Hancock/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.hancockna.org/www/'
    }],

 'UniversityofTexasArr': [{
	  'name' : 'University of Texas',
        'description' : """This neighborhood encompasses the area surrounding the University of Texas at Austin campus. As the university is one of the largest in the nation, students pretty much dominate this neighborhood, and many of the local businesses and restaurants cater to students, faculty, and others affiliated with the university.
The neighborhood has a youthful feel and the population is predominantly young and single. There are a few families living here. Most residents attend or work at the university. After graduation, most students who stay in the area move to other neighborhoods.
Housing is in high demand and tends to be occupied by students. About 80 percent of the university students live off-campus. The neighborhood tends to be boisterous, especially on weekends during the academic year.
""",
'Hurl' : 'https://torreatx.com/floor-plans/',
    'url' : 'https://www.mapsofaustin.com/The-University-of-Texas-at-Austin'
    }],


 'DowntownArr': [{
	  'name' : 'Downtown',
        'description' : """Downtown Austin is the hub of the city and the seat of the Texas state government. Many companies have offices here, and there are many business services available. The neighborhood also has a wide range of dining, shopping, entertainment, nightlife, recreation, and sightseeing options.
Many of Austin's well-known restaurants, lounges, live performance venues, and landmarks are in the neighborhood or very close by. Dining and nightlife options range from intimate cafes and bars to high-end restaurants and lounges.
Housing downtown consists mostly of luxury condos and apartments. Residents tend to be single professionals and young couples.
""",
'Hurl' : 'https://www.redfin.com/neighborhood/173120/TX/Austin/Downtown-Austin/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.downtownaustin.org/'
    }],

'WestOakHillArr': [{
	  'name' : 'West Oak Hill',
        'description' : """One of the largest neighborhoods in Austin. West Oak Hill is a long-established area at the famous "Y", where Hwy. 290 branches out from Hwy. 71 and changes from an elevated highway to a hill country thoroughfare. West Oak Hill is actually the western part of a large region that includes older forested homesites, newer master-planned communities, shops and strip malls, and many amenities.
""",
'Hurl' : 'https://www.redfin.com/neighborhood/164286/TX/Austin/West-Oak-Hill/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.niche.com/places-to-live/n/west-oak-hill-austin-tx/'
    }],

'BelterraArr': [{
	  'name' : 'Belterra',
        'description' : """Circle C Ranch is a large master-planned community about 20 minutes' commute from downtown. With about 5,000 homes, It is a safe, suburban, residential neighborhood with several amenities and access to some of Austin's best parks and outdoor venues. The neighborhood is close to Hwy. 1 (MoPac) and Hwy. 290, providing access to the rest of the city and areas west of Austin. There is little to no public transportation here, so residents need a vehicle to get around. There is shopping and dining within walking distance for some residents.""",
'Hurl' : 'https://www.redfin.com/neighborhood/497554/TX/Dripping-Springs/Belterra/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.belterracommunity.com/home/'
    }],

'HighpointeArr': [{
	  'name' : 'Highpointe',
        'description' : """Highpointe is a deluxe master-planned community on the southwestern outskirts of Austin, about 25 miles from downtown. Highpointe offers newer homes with nice views of the central Texas hill country, proximity to forests and grasslands, many community amenities, and convenient travel to downtown Austin via State Highway 290.

""",
'Hurl' : 'https://www.redfin.com/neighborhood/233755/TX/Dripping-Springs/High-Pointe?utm_source=google&utm_medium=ppc&utm_term=aud-1529945865573:dsa-1526340592292&utm_content=569216595591&utm_campaign=1034095&gclid=CjwKCAjwoMSWBhAdEiwAVJ2ndqtnNueWTS2wdCt1fxQpn-Zuy-6iaPXj_dTtuSRpoMHkKKcA-rtx-xoCvNsQAvD_BwE',
    'url' : 'https://highpointehoa.connectresident.com/'
    }],

'MuellerArr': [{
	  'name' : 'Mueller',
        'description' : """Mueller is a planned mixed-use community which is quickly becoming one of the trendiest and more desirable locations in Austin. Just three miles from downtown and two miles from the University of Texas, the Mueller development includes single family and multi-family homes, apartments, a shopping center, restaurants and food trailers, connections to public transportation, and modern office and retail space. The development plan was approved and construction began in 2007 and the neighborhood is scheduled to be completed in 2017.""",
'Hurl' : 'https://www.redfin.com/neighborhood/351586/TX/Austin/Mueller/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://muelleraustin.com/'
    }],

'LostCreekArr': [{
	  'name' : 'Lost Creek',
        'description' : """Lost Creek is a safe, quiet, high-end neighborhood with large homes hidden in the trees and forests in west Austin. The neighborhood is known for its good views of the hill country, natural scenery, and peaceful atmosphere. Although there are few restaurants and businesses within the neighborhood, it is very close to the Barton Creek Square Mall. The neighborhood offers many opportunities for outdoor recreation, with parks, walking and bike trails, and its own country club and golf course.""",
'Hurl' : 'https://www.redfin.com/city/24058/TX/Lost-Creek/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.lcna.com/default.php'
    }],

'McKinneyArr': [{
	  'name' : 'McKinney',
        'description' : """McKinney is an interesting combination of urban living and natural scenery, industrial park and residential community. In one section of the neighborhood there are industrial and commercial buildings, and in another section are houses with large lots.
The neighborhood borders two major local highways, and is also next to a large state park. There are not many dining or shopping options in the neighborhood itself, but the area is not far from downtown and south Austin.""",
'Hurl' : 'https://www.redfin.com/city/11666/TX/McKinney/filter/include=forsale+mlsfsbo+construction',
    'url' : 'http://www.mckinneyheights.com/'
    }],

'EastCesarChavezArr': [{
	  'name' : 'East Cesar Chavez',
        'description' : """East Cesar Chavez is named for E. Cesar Chavez St., one of the main streets that pass through this neighborhood. East Cesar Chavez is a diverse, active neighborhood just east of downtown. Diverse in the styles of homes, and the types of businesses and people in the neighborhood. Active in that there are many dining and nightlife options in the area.
The neighborhood retains much of its old-town feel, but has undergone a revival recently with many new, local businesses springing up, including a variety of restaurants and bars. Downtown is just a few blocks west. Public transportation is readily available.
""",
'Hurl' : 'https://www.redfin.com/neighborhood/166183/TX/Austin/East-Cesar-Chavez/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://eastcesarchavez.org/'
    }],

'GovalleArr': [{
	  'name' : 'Govalle',
        'description' : """Govalle is a neighborhood in Austin, Texas with a population of 5,316. Govalle is in Travis County. Living in Govalle offers residents an urban suburban mix feel and most residents own their homes. In Govalle there are a lot of bars, restaurants, coffee shops, and parks. Many young professionals live in Govalle and residents tend to lean liberal. The public schools in Govalle are above average.
""",
'Hurl' : 'https://www.redfin.com/neighborhood/164283/TX/Austin/Govalle/filter/include=forsale+mlsfsbo+construction',
    'url' : 'http://metafactory.ca/govalle/'
    }],


'AngusValleyArr': [{
	  'name' : 'Angus',
        'description' : """Angus Valley is a smaller neighborhood located adjacent to Hwy. 183 (Research Blvd.), a major local thoroughfare. Most of the homes here were built in the 1960s and 70s, though a few are newer.
The neighborhood is conveniently located. Besides being near a major local highway, Angus Valley is virtually in the middle of the shopping and dining district of north/northwest Austin. The neighborhood is also close to the high-tech companies of north Austin, and not far from downtown.
""",
'Hurl' : 'https://www.redfin.com/neighborhood/231913/TX/Austin/Angus-Valley/filter/include=forsale+mlsfsbo+construction',
    'url' : 'https://www.angusvalley.org/'
    }],




}






neighboRet = []
holdingInfo = []



@app.route('/', methods=['GET', 'POST'])
def home():
   if request.method == 'POST':
       if request.form['submit_button'] == 'secOpiAdd':
           open('sample.json', 'w').close()
           holdingInfo.clear()
           pythonTran = []
           neighboRet.clear()
           pythonTran.clear()
           pythonTran = request.form.getlist('myCheckbox')
           pythonTran.append(request.form.get('thirdForm'))
           pythonTran.append(request.form.get('secForm'))
           pythonTran.append(request.form.get('exampleForm'))
           pythonTran = list(map(int, pythonTran))
           exec(open("webscraper.py").read())
           print(pythonTran)
        #Create Recommendations ===========================
           for key, values in neighborhoods.items():
                if pythonTran[-1] == 1 and values[0] == 1:
                    stoVal1 = len(set(pythonTran).intersection(values))
                    if stoVal1 >= 2:
                        neighboRet.append(key)
                if pythonTran[-1] == 2 and values[0] == 2:
                    stoVal1 = len(set(pythonTran).intersection(values))
                    if stoVal1 >= 2:
                        neighboRet.append(key)
                if pythonTran[-1] == 3 and values[0] == 3:
                    stoVal1 = len(set(pythonTran).intersection(values))
                    if stoVal1 >= 2 :
                        neighboRet.append(key)

           for community in neighboRet:
                raw_data = data[community][0]
                json_str = json.dumps(raw_data, indent=4, sort_keys=True)
                resp = json.loads(json_str)
                holdingInfo.append(resp)
                with open("sample.json", "a") as outfile:
                    outfile.write(json_str)

           outfile.close()
           #datan = [json.loads(line) for line in open('sample.json', 'r')]
           #print(datan)
           return redirect(url_for('second'))
   return render_template('index.html', holdingInfo = holdingInfo)

@app.route('/finale')
def second():
    return render_template('other.html', finalList = holdingInfo)

@app.route('/map')
def third():
    return render_template('my_map1.html', finalList = holdingInfo)
@app.route('/about')
def aboutt():
    return render_template('aboutus.html', finalList = holdingInfo)



if __name__ == '__main__':
   app.debug = True
   app.run()
