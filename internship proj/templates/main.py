# Import necessary packages
import folium
'''
import os 

from folium import plugins
import rioxarray as rxr
import earthpy as et
import earthpy.spatial as es


'''

myMap = folium.Map(location=[30.24033723168927, -97.82746517105676], zoom_start = 13, control_scale=True , width = 600, height = 600) #able to change tiles, zoom, etc if wanted
#after the popup, put tooltip = 'neighborhood name', and then the discription as the popup
#coord, popup label for the marker, icon


folium.Marker( location=[30.24033723168927, -97.82746517105676], popup = folium.Popup(
    'East Oak Hill is one of the larger neighborhoods in Austin and stretches across a sizeable part of the southwest area of town, from MoPac to the Barton Hills Wilderness Park. It is nestled in the hill country and has many larger, relatively new homes, some with impressive views of the Texas hills and Lady Bird Lake.',
    max_width=300), tooltip = 'East Oak Hill', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.286016729723357, -97.8668536758317], popup = folium.Popup(
    "Barton Creek is one of the larger and older neighborhoods in Austin. Some of the homes date back to the start of the 20th Century, others to the 1920s, and many are quite large as well as old. About two-thirds of the area is greenspace, and the neighborhood is surrounded by the Barton Creek Greenbelt and Zilker Park, Austin's favorite city park. Barton Creek Square Mall is nearby with its luxury stores and restaurants, and students have access to top-rated schools.",
    max_width=300), tooltip = 'Barton Creek',icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.314965821230526, -97.83296041048956], popup = folium.Popup(
    "Rob Roy is an established, private neighborhood located on Hwy. 360 (Capital of Texas Hwy.), one of the main thoroughfares in west Austin. Rob Roy is one of Austin's largest private neighborhoods with high-end homes located on large lots overlooking the hill country. The neighborhood has mature trees, abundant green spaces, and meticulously maintained landscaping.",
    max_width=300), tooltip = 'Rob Roy',icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.347512603060192, -97.862249513358], popup = folium.Popup(
    "Austin Lake Estates is an affluent neighborhood located on the banks of Lake Austin. It is a close-knit community with friendly people in which residents know and look out for each other. Although it has grown recently, along with the rest of the city, it retains its down-to-earth, community-oriented feel. The neighborhood is just 20 minutes' drive from downtown Austin, and is also close to the shopping and dining of the Bee Caves area of west Austin. The neighborhood itself has many amenities related to the lake and outdoors, and has a park and ample green spaces. The area neighborhood association is active in maintaining the neighborhood's environment and facilities.",
    max_width=300), tooltip = 'Austin Lake Estates',icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.364425899824475, -97.89371938240618], popup = folium.Popup(
    "Steiner Ranch is a large master-planned community located in the hills and green spaces between Lake Austin and Lake Travis. It is adjacent to a major wildlife preserve and has many amenities in and around the neighborhood. The neighborhood also contains shopping centers, restaurants, and highly rated schools. Steiner Ranch is close to a major west Austin highway and about a half hour drive to downtown.",
    max_width=300), tooltip = 'Steiner Ranch', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.370767396232583, -97.85686111718108], popup = folium.Popup(
    "River Place is a newer neighborhood located in a scenic spot in the Texas hill country. Although River Place does not have as many shopping and dining venues as some other neighborhoods, it has abundant green space and many options for outdoor recreation. Many homes have expansive views of the hills or green spaces in the neighborhood. Residents have access to parks, miles of hiking and bike trails, a marina on Lake Austin for water recreation, and a golf course. The neighborhood is just off a major local highway for direct access to the rest of the city.",
    max_width=300), tooltip = 'River Place',icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.37765180579217, -97.79658013554207], popup = folium.Popup(
    "Jester Estates is a scenic, conveniently located neighborhood at the intersection of two major local highways and close to major shopping centers. Jester Estates has several neighborhood amenities including a pool and ball courts. There are shopping and dining options nearby. The area is in the hill country and many homes have excellent views of the Colorado River and even downtown. The area has abundant green space for outdoor recreation and is close to the high-tech companies and shopping in north Austin.",
    max_width=300), tooltip = 'Jester Estates',icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.296287178225384, -97.75601850625127], popup = folium.Popup(
    "Old West Austin is a historic, centrally located neighborhood just north of Lady Bird Lake and just west of downtown. The neighborhood’s historic district dates back to the mid-1800s, shortly after the city of Austin was incorporated. The neighborhood is one of the most sought-after to live in, because of its convenient location and access to many amenities, including the lake, local hike and bike trails, and several parks.Along with local shops and restaurants the neighborhood is adjacent to the numerous dining, shopping, and entertainment options offered by downtown and south Austin. Parking is next to impossible here, but public transportation is readily accessible.",
    max_width=300), tooltip = 'Old West Austin',icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[ 30.30250887718204, -97.75424218159125], popup = folium.Popup(
    "Bryker Woods is an established neighborhood in north central Austin with mostly older, smaller single-family homes. Located just a few minutes drive from downtown and the University of Texas, and with well-known local restaurants in the area, the neighborhood is popular for its convenient location and its small-town atmosphere in the middle of the city. Residents enjoy plenty of green space with parks and two golf courses in the area. The neighborhood has its own elementary school. Bryker Woods has some longtime residents and some younger singles and families attracted to the relaxed, natural environment and good location.",
    max_width=300), tooltip = 'Bryker Woods',icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.31451259491662, -97.74562696172536], popup = folium.Popup(
    "Rosedale is an older, comfortable, residential neighborhood in the northwest section of central Austin. The central part of the neighborhood has older, modest-sized homes and some new construction, while the outer sections have restaurants and shops. The area has several major parks with a pool, playscapes, tennis courts, and athletic fields. The community is close-knit and the residents take an active part in maintaining the charming, historic feel to their neighborhood. The neighborhood is conveniently located next to MoPac (Hwy. 1), one of the local highways, providing access to other parts of the city. The area is also not very far from downtown and the University of Texas. Public transportation is also ample here.",
    max_width=300), tooltip = 'Rosedale',icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.312312373697416, -97.73560319486162], popup = folium.Popup(
    "Triangle State is a newer, upscale, residential/commercial neighborhood in north central Austin. The neighborhood was designed to be largely self-contained with many amenities to appeal to younger, urban professional singles and couples. The area has consists of luxury condos, homes, and apartments interspersed with shopping centers containing many fine restaurants, stores, and supermarkets. There are also cafes, bars, and other businesses. The area is close to the University of Texas and downtown, and public transportation is readily accessible. Within the neighborhood are several large green spaces suitable for kids and pets.",
    max_width=300), tooltip = 'Triangle State',icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.308281949180586, -97.72667719260232], popup = folium.Popup(
    "Hyde Park is an older, historic neighborhood in Austin and one of the most desirable places to live for many because of its residential atmosphere, safety, sense of community, and convenient location. Hyde Park is located close to the University of Texas and to downtown. The neighborhood is quiet and residential, with mostly single-family homes. There are not as many shops and restaurants as in some other areas, but there are many amenities in adjacent neighborhoods just a short walk or bus ride away. Residents consist mainly of families, graduate students, and professors.",
    max_width=300), tooltip = 'Hyde Park', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.296641056051577, -97.72352663378156], popup = folium.Popup(
    "Hancock is a comfortable, safe, residential neighborhood conveniently located just west of I-35 and north of the University of Texas and downtown. Despite being close to the center of the city, the neighborhood is quiet, with many single-family homes on streets lined with mature trees. The area also has parks, bike-friendly streets, an abundance of green space. Shopping, restaurants, fitness centers, and live music are readily available in the neighborhood, and public transportation is easily accessible. The neighborhood is popular with families, university students and faculty, and professionals who work downtown.",
    max_width=300), tooltip = 'Hancock',icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.28508521869459, -97.73398576011617], popup = folium.Popup(
    "This neighborhood encompasses the area surrounding the University of Texas at Austin campus. As the university is one of the largest in the nation, students pretty much dominate this neighborhood, and many of the local businesses and restaurants cater to students, faculty, and others affiliated with the university. The neighborhood has a youthful feel and the population is predominantly young and single. There are a few families living here. Most residents attend or work at the university. After graduation, most students who stay in the area move to other neighborhoods. Housing is in high demand and tends to be occupied by students. About 80 percent of the university students live off-campus. The neighborhood tends to be boisterous, especially on weekends during the academic year.",
    max_width=300), tooltip = 'University of Texas', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2720150682229, -97.74502751874148], popup = folium.Popup(
    "Downtown Austin is the hub of the city and the seat of Texas state government. Many companies have offices here, and there are many business services available. The neighborhood also has a wide range of dining, shopping, entertainment, nightlife, recreation, and sightseeing options. Many of Austin's well-known restaurants, lounges, live performance venues, and landmarks are in the neighborhood or very close by. Dining and nightlife options range from intimate cafes and bars to high-end restaurants and lounges. Housing downtown consists mostly of luxury condos and apartments. Residents tend to be single professionals and young couples.",
    max_width=300),tooltip = 'Downtown', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.238901652495382, -97.89512895845921], popup = folium.Popup(
    '''One of the largest neighborhoods in Austin. West Oak Hill is a long-established area at the famous "Y", where Hwy. 290 branches out from Hwy. 71 and changes from an elevated highway to a hill country thoroughfare. West Oak Hill is actually the western part of a large region that includes older forested homesites, newer master-planned communities, shops and strip malls, and many amenities.''',
    max_width=300),tooltip = 'West Oak Hill', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.191857619647745, -97.88707124255075], popup = folium.Popup(
    "Circle C Ranch is a large master-planned community about 20 minutes' commute from downtown. With about 5,000 homes, It is a safe, suburban, residential neighborhood with several amenities and access to some of Austin's best parks and outdoor venues. The neighborhood is close to Hwy. 1 (MoPac) and Hwy. 290, providing access to the rest of the city and areas west of Austin. There is little to no public transportation here, so residents need a vehicle to get around. There is shopping and dining within walking distance for some residents.",
    max_width=300),tooltip = 'Circle C Ranch', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.189643415545135, -97.98245805280547], popup = folium.Popup(
    "Belterra is a 1,600 acre master planned community off of State Highway 290 West, about 18 miles from downtown Austin and seven miles from Dripping Springs, Texas. The community offers many amenities, close proximity to the Texas hill country and nearby state parks, rivers, and lakes, and is convenient to shopping, schools, restaurants, and entertainment.",
    max_width=300),tooltip = 'Belterra', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.171628809117237, -97.99492222105448], popup = folium.Popup(
    "Highpointe is a deluxe master-planned community on the southwestern outskirts of Austin, about 25 miles from downtown. Highpointe offers newer homes with nice views of the central Texas hill country, proximity to forests and grasslands, many community amenities, and convenient travel to downtown Austin via State Highway 290.",
    max_width=300),tooltip = 'Highpointe', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.29871153081968, -97.70080957427255], popup = folium.Popup(
    "Mueller is a planned mixed-use community which is quickly becoming one of the trendiest and more desirable locations in Austin. Just three miles from downtown and two miles from the University of Texas, the Mueller development includes single family and multi-family homes, apartments, a shopping center, restaurants and food trailers, connections to public transportation, and modern office and retail space. The development plan was approved and construction began in 2007 and the neighborhood is scheduled to be completed in 2017.",
    max_width=300),tooltip = 'Mueller', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.282674775144724, -97.84299117110557], popup = folium.Popup(
    "Lost Creek is a safe, quiet, high-end neighborhood with large homes hidden in the trees and forests in west Austin. The neighborhood is known for its good views of the hill country, natural scenery, and peaceful atmosphere. Although there are few restaurants and businesses within the neighborhood, it is very close to the Barton Creek Square Mall. The neighborhood offers many opportunities for outdoor recreation, with parks, walking and bike trails, and its own country club and golf course.",
    max_width=300),tooltip = 'Lost Creek', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.212718290883238, -97.73638269028146], popup = folium.Popup(
    "McKinney is an interesting combination of urban living and natural scenery, industrial park and residential community. In one section of the neighborhood there are industrial and commercial buildings, and in another section are houses with large lots. The neighborhood borders two major local highways, and is also next to a large state park. There are not many dining or shopping options in the neighborhood itself, but the area is not far from downtown and south Austin.",
    max_width=300),tooltip = 'McKinney', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.258061764901946, -97.73150879106682], popup = folium.Popup(
    "East Cesar Chavez is named for E. Cesar Chavez St., one of the main streets that pass through this neighborhood. East Cesar Chavez is a diverse, active neighborhood just east of downtown. Diverse in the styles of homes, and the types of businesses and people in the neighborhood. Active in that there are many dining and nightlife options in the area. The neighborhood retains much of its old-town feel, but has undergone a revival recently with many new, local businesses springing up, including a variety of restaurants and bars. Downtown is just a few blocks west. Public transportation is readily available.",
    max_width=300),tooltip = 'East Ceasar Chavez', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.256034040813, -97.70241493424967], popup = folium.Popup(
    "Govalle is a neighborhood in Austin, Texas with a population of 5,316. Govalle is in Travis County. Living in Govalle offers residents an urban suburban mix feel and most residents own their homes. In Govalle there are a lot of bars, restaurants, coffee shops, and parks. Many young professionals live in Govalle and residents tend to lean liberal. The public schools in Govalle are above average.",
    max_width=300),tooltip = 'Govalle', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.214158790835487, -97.76811350418134], popup = folium.Popup(
    "Battle Bend Springs is a family-oriented neighborhood with a diverse population. The community is close knit and there are many neighborhood activities, as well as schools, parks, and a creek. It is conveniently close to the attractions of downtown and west Austin, such as Barton Springs and ZilkerPark, by car and public bus.",
    max_width=300),tooltip = 'Battle Bend Springs', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.427509280463994, -97.73441575643487], popup = folium.Popup(
    "Angus Valley is a smaller neighborhood located adjacent to Hwy. 183 (Research Blvd.), a major local thoroughfare. Most of the homes here were built in the 1960s and 70s, though a few are newer. The neighborhood is conveniently located. Besides being near a major local highway, Angus Valley is virtually in the middle of the shopping and dining district of north/northwest Austin. The neighborhood is also close to the high-tech companies of north Austin, and not far from downtown.",
    max_width=300),tooltip = 'Angus Valley', icon = folium.Icon() ).add_to(myMap)



folium.Marker( location=[30.3393, -97.7470], popup = folium.Popup(
    "Allandale is in Travis County and is one of the best places to live in Texas. Living in Allandale offers residents an urban suburban mix feel and most residents own their homes. In Allandale there are a lot of bars, restaurants, coffee shops, and parks good for families and seniors.",
    max_width=300),tooltip = 'Allandale', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.19201 ,-9743103], popup = folium.Popup(
    "Austin's North Loop neighborhood is a unique part of town located just northeast of the University of Texas. North Loop's proximity to the university and mix of eclectic restaurants and shops makes it a popular local hangout among students and campus staff.",
    max_width=300),tooltip = 'North Loop', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.3483 , -97.7275  ], popup = folium.Popup(
    "Like Allendale, Crestview is in Travis County and is one of the best places to live in Texas. Living in Crestview offers residents an urban suburban mix feel and most residents rent their homes. In Crestview there are a lot of bars, restaurants, coffee shops, and parks.",
    max_width=300),tooltip = 'Crestview', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.3911 , -97.7218], popup = folium.Popup(
    "North Burnet is an older neighborhood with some new, upscale, urban developments. The neighborhood has lots of deluxe apartments and condos, few detached homes and little green space, but several shopping centers, and many restaurants.",
    max_width=300),tooltip = 'North Burnet', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.3891 , -97.6942], popup = folium.Popup(
    "Gracy Woods is a quiet, suburban neighborhood in far north Austin. There are several parks and abundant green spaces in the area and the residents love being intimate with nature. Shopping centers and restaurants are just to the north, many of the Austin high tech employers are just to the west, and the neighborhood is situated between two major local highways.",
    max_width=300),tooltip = 'Gracy Woods', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2573 , -97.7172], popup = folium.Popup(
    "Holly is a neighborhood in East Austin, Texas, that was recently ranked No. 24 in Time Out's list of the 50 coolest neighborhoods in the world. It's close to downtown Austin and borders the Colorado River, making it the ideal location for all Austin has to offer.",
    max_width=300),tooltip = 'Holly', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2791 , -97.7132], popup = folium.Popup(
    "Although most of the homes are older and modest in size, some new, larger houses are being built. The neighborhood is close enough to downtown and the University of Texas that residents can bike to either location",
    max_width=300),tooltip = 'Chestnut', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.3340 , -97.7170], popup = folium.Popup(
    "Highland is a quiet, working-class neighborhood with modest, single-family homes. The neighborhood is probably best known for the Highland Mall, once a prominent shopping center that has fallen into disuse in recent years.Public transportation is also highly accessible. The neighborhood has some local eateries and a cinema, and just to the west are parks, ball fields, and playgrounds.",
    max_width=300),tooltip = 'Highland', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.3680 , -97.9917 ], popup = folium.Popup(
    "Lakeway is a suburb of Austin with a population of 15,605. Lakeway is in Travis County and is one of the best places to live in Texas. Living in Lakeway offers residents a sparse suburban feel and most residents own their homes. In Lakeway there are a lot of parks.",
    max_width=300),tooltip = 'Lakeway', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2534 , -97.7835], popup = folium.Popup(
    "The area is safe and with access to a large park and top schools is a good place for young families. Barton Hills is a favorite area for many in which to live and hang out, because of the abundance of green spaces and the proximity to some of Austin's best amenities.",
    max_width=300),tooltip = 'Barton Hills', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2543 , -97.7670], popup = folium.Popup(
    "Zilker is one of the most desirable areas for many locals to settle down. There are abundant greenspaces and parks just to the west, shopping and dining are within walking distance, and downtown is just to the north.",
    max_width=300),tooltip = 'Zilker', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2515 , -97.7543], popup = folium.Popup(
    "Bouldin Creek is still a safe and tranquil neighborhood that allows residents to bike or walk safely in the streets. When compared to closeby neighborhoods such as Barton Hills and Zilker, there aren't many large families with children. This area became more suitable for creative, young professionals and students.",
    max_width=300),tooltip = 'Bouldin Creek', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2050 , -97.7748], popup = folium.Popup(
    "South Congress epitomizes the hip, trendy ambiance of south Austin. It's possibly the best-known neighborhood in Austin for its unique, local shops and boutiques, diners, coffee shops, and lounges that line Congress Ave.The California-style food trucks that are now ubiquitous around town appeared here first and have been spreading out to other parts of town. Crowded with pedestrians at almost all hours, the neighborhood is a city hub and landmark, and a walkable exhibition of Austin's one-of-a-kind, slightly offbeat local character.",
    max_width=300),tooltip = 'South Congress', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2443 , -97.7444], popup = folium.Popup(
    "Travis Heights is one of the older Austin neighborhoods and one of the more exclusive and affluent areas of south Austin. Old mansions and other homes, with sizable yards, along with a few apartments are here. The area is conveniently located near the trendy shopping and dining districts of South Congress Ave. There are also several major parks. The population spans a wide range of age groups and occupations.",
    max_width=300),tooltip = 'Travis Heights', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2289 , -97.7526], popup = folium.Popup(
    "Saint Edwards is a residential community surrounding the beautiful campus of St. Edward's University. Although a popular location for students, a mix of other residents also live here, including artists, single young professionals, and families. Residents tend to be friendly and close-knit. Many homes have well-maintained gardens. There are many local shops and restaurants in and near the neighborhood. The neighborhood is bounded on three sides by major local highways and thoroughfares, giving easy access to the rest of the city.",
    max_width=300),tooltip = 'St. Edwards', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2372 , -97.7838], popup = folium.Popup(
    "South Lamar is a trendy neighborhood with many local shops, restaurants, and lounges. It is also conveniently located just five minutes from downtown and very close to the parks and hiking/biking trails around Barton Springs to the west. Although it is close to central Austin, crime here is relatively low. The population is of mixed ethnicity and includes singles, families, students, and seniors. The area also has top-rated schools.",
    max_width=300),tooltip = 'South Lamar', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2132 , -97.7744], popup = folium.Popup(
    "West Congress is a small, ethnic, residential neighborhood bordering Hwy. 71 to the north. Many modest, ranch-style homes and apartment complexes are here. Also many casual restaurants. The neighborhood is popular among families and college students.",
    max_width=300),tooltip = 'West Congress', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2140 , -97.7681], popup = folium.Popup(
    "Battle Bend Springs is a family-oriented neighborhood with a diverse population. The community is close knit and there are many neighborhood activities, as well as schools, parks, and a creek. It is conveniently close to the attractions of downtown and west Austin, such as Barton Springs and Zilker Park, by car and public bus.",
    max_width=300),tooltip = 'Battle Bend', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.3627 , -97.6792], popup = folium.Popup(
    "Windsor Hills is in many ways a classic suburban neighborhood, quiet, family-friendly, well-tended homes and yards, and not much in the way of entertainment or nightlife. But it is attractive to young families, as well as students and single professionals, because housing is inexpensive and it is easy to commute by car or public transportation to other parts of the city. Although the neighborhood is largely residential, there is shopping and casual dining nearby.",
    max_width=300),tooltip = 'Windsor Hills', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.4088 , -97.7716], popup = folium.Popup(
    "Great Hills is a suburban neighborhood conveniently located near two major local highways and a shopping center.Great Hills is located next to an abundance of shopping and dining options, as well as a hotel, cinema, bookstore, and several coffee shops. There are also two parks, a country club, a pool, playground, and hiking and bike trails in the area. Residents include young professionals and couples, families, and students. While there are not as many families here as in other neighborhoods, there are still highly rated schools and kids' activities in the area",
    max_width=300),tooltip = 'Great Hills', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.4065 , -97.7376], popup = folium.Popup(
    "Balcones Woods is a small community conveniently located near the major thoroughfares and shopping centers of north Austin.The neighborhood offers amenities including a community center, pool, park, and tennis courts. The area is close to the high-tech centers and employers of north Austin and not far from downtown. The proximity to the local highways gives ready access to other parts of the city.",
    max_width=300),tooltip = 'Balcones Woods', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.4984 , -97.7811], popup = folium.Popup(
    "Avery Ranch is a planned community in far northwest Austin, one of the fastest-growing areas of town (and the U.S.). With 1,800 acres and 4,000 homes, Avery Ranch is one of the larger neighborhoods,and has a range of houses and amenities to match. Many of the homes have views of the surrounding countryside, as well as large windows and landscaped backyards.",
    max_width=300),tooltip = 'Avery Ranch', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2716 , -97.7249], popup = folium.Popup(
    "Central East Austin is a historic east Austin neighborhood that is undergoing gradual revitalization. The neighborhood is close to downtown and the University of Texas by car, public bus, or even on foot. Public transportation is readily available in this neighborhood, and there is quick access to I-35, providing an easy commute to other parts of the city.The neighborhood has a mix of people including older, longtime residents, young singles and couples, and college students. Although some homes and sections are rundown, the neighborhood generally is well-kept and residents friendly.",
    max_width=300),tooltip = 'Central East Austin', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.3532 , -97.7675], popup = folium.Popup(
    "Northwest Hills is an upscale, scenic, family-friendly neighborhood set on a hilltop in west Austin, just off Hwy. 1 (MoPac). Residents have good views of the hill country and easy access to the shopping and dining, as well as major high-tech employers, of north and northwest Austin.The neighborhood is bounded by several major local highways and there are top-rated schools right in the neighborhood. There are upscale restaurants scattered around the neighborhood. and shopping malls are just minutes’ commute away. Downtown is also close. The neighborhood has a park and hiking and bike trails.",
    max_width=300),tooltip = 'Northwest Hills', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.3634 , -97.7791], popup = folium.Popup(
    "Cat Mountain is an affluent neighborhood in the hills of northwest Austin, with good views of Lake Austin and the Colorado River. The neighborhood is conveniently located near two major local highways, and just a few minutes' drive from downtown and the shopping centers of northwest and west Austin.The neighborhood offers several amenities to enable residents to enjoy the outdoors and the lake, and other amenities are nearby in the area. Many of the homes are fairly new, as the community underwent substantial development in the early 2000s to accommodate a large influx of newcomers.",
    max_width=300),tooltip = 'Cat Mountain', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.3321 , -97.7598], popup = folium.Popup(
    "Highland Park West Balcones is known for its large, beautiful, well-maintained homes and its abundant natural scenery with nice views of the city skyline and Lake Austin. The area is on a hill at several hundred feet elevation so views are plentiful here.The neighborhood also has several parks and nature preserves as well as a historic (and still functioning) military post. The area is close to Hwy. 1 (MoPac), a major local highway, and is close to downtown.",
    max_width=300),tooltip = 'Highland Park West Balcones', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.3008 , -97.7685], popup = folium.Popup(
    "Tarrytown is an affluent neighborhood located just west of MoPac, a major local highway, and close to downtown and the University of Texas. It is a well-appointed area with both modern and traditional Southern homes, well-kept yards, tree-lined streets, and wooded areas. Tarrytown is known as one of the most prestigious, and expensive, neighborhoods in the city. Although it is mostly residential, with few businesses and restaurants in the neighborhood, residents have just a short drive to reach downtown or south Austin for extensive shopping, dining, and entertainment options.There is plenty of green space in the area. Additionally, there are parks in the area for swimming, playgrounds, ball courts, hiking, and biking.",
    max_width=300),tooltip = 'Tarrytown', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2769 , -97.7911], popup = folium.Popup(
    "Rollingwood is known in Austin as an upscale neighborhood conveniently located close to the amenities of downtown, south, and west Austin. The neighborhood offers abundant opportunities for outdoor recreation. It has its own recreational facilities and provides easy access to local parks and lakes, as well as high-end dining and shopping. Rollingwood is a small, established community with well-appointed homes, tree-lined streets, and natural scenery.",
    max_width=300),tooltip = 'Rollingwood', icon = folium.Icon() ).add_to(myMap)
folium.Marker( location=[30.2980 , -97.8020], popup = folium.Popup(
    "West Lake Hills is a small, suburban neighborhood in the Texas hill country near Lake Austin. It has abundant trees, woodlands, green space, hills, and hiking and bike trails, and is near Lake Austin and a wildlife preserve. However it is also close to shopping and dining and 10 minutes drive from downtown.The neighborhood is next to Bee Cave Rd. and Hwy. 360 (Capital of Texas Hwy.), two main thoroughfares in west Austin, offering easy access to the city. There are many local shops and restaurants nearby, and several major shopping centers are close by",
    max_width=300),tooltip = 'Westlake Hills', icon = folium.Icon() ).add_to(myMap)

myMap.save(" my_map1.html " )



