#Import Nessecary Libraries
from bs4 import BeautifulSoup
import requests 
import lxml
import pandas as pd

from recommendations import neighborhoods

#Extract NL
neighborhood_html = requests.get('https://www.austintexasinsider.com/austinneighborhoods.html')
neighborhood_soup = BeautifulSoup(neighborhood_html.text, 'html.parser')

dfs = pd.read_html(neighborhood_html.text)
table = dfs[0]

#Initialize the dictionary here 
mp_table = {
    'dining': [],
    'greenery' : [],
    'nightlife' : [],
    'community' : [],
    'shopping' : [],
    'singles' : [],
    'seniors' : [],
    'quiet' : [],
    'transportation' : [],
    'safe' : []
}

value_key = {
    'dining': 11,
    'greenery' : 12,
    'nightlife' : 13,
    'community' : 14,
    'shopping' : 15,
    'singles' : 16,
    'seniors' : 17,
    'transportation' : 18,
}
#Add each value to the dictionary 
for i in range(1, 11):
    temp_list = []
    for j in table[1][i].split(', '):
        temp_list.append(j.replace(" ", "") + "Arr")
        key = list(mp_table)[i-1]
        mp_table[key] = temp_list

#Push the webscraping data into the arrays
for item in mp_table.keys():
    for place in mp_table[item]:
        temp_list = neighborhoods[place]

        try:
            temp_list.append(value_key[item])
        
        except:
            pass

        neighborhoods[place] = temp_list

print(neighborhoods)




    










    
    



