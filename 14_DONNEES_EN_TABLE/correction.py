import csv
t = []
file = open('table_pokedex.csv', 'r')
d = csv.DictReader(file,delimiter=',')
for i in d :
    t.append(dict(i))
file.close()
'''
#1
type(t) # list
#2 
type(t[0]) # dict
#3
print(t)
t
# Question 4 :
question4 = []
for poke in t :
    if poke["Legendary"] == "True" :
        question4.append(poke['Name'])
# Question 5 :
question5 = []
for poke in t :
    if poke["Type 1"] == "Fire" or poke["Type 2"] == "Fire":
        question5.append(poke['Name'])

[o[’Name’] for o in t if o[’Generation’] == "3"]

bonus = []
for o in t :
    if o['Generation'] == '3' :
        bonus.append(o['Name'])

t.append({'#' : '999', 'Name' : 'NSI', 'Type 1' : 'Sleep', 'Type 2' : 'Sound', 'HP' : '4', 'Attack' : "1300", 'Defense' : '0', 'Sp. Atk' : '2080', 'Sp. Def' : '0', 'Speed' : '210', 'Generation' : '47', 'Legendary' : 'True' 
    
    })
    
#7
for i in t :
    i['total_stat'] = str(int(i['HP']) + int(i['Attack']) + int(i['Defense']) \
    + int(i['Sp. Atk']) + int(i['Sp. Def']) + int(i['Speed']))
#8 
def cle_tri(t):
    return int(t['HP'])

>>> t.sort(key = cle_tri, reverse=True)
>>> print(t[0])
{'#': '357', 'Name': 'Tropius', 'Type 1': 'Grass', 'Type 2': 'Flying', 'HP': '99', 'Attack': '68', 'Defense': '83', 'Sp. Atk': '72', 'Sp. Def': '87', 'Speed': '51', 'Generation': '3', 'Legendary': 'False'}
>>> %Run test.py
>>> t.sort(key = cle_tri, reverse=True)
>>> print(t[0])
{'#': '242', 'Name': 'Blissey', 'Type 1': 'Normal', 'Type 2': '', 'HP': '255', 'Attack': '10', 'Defense': '10', 'Sp. Atk': '75', 'Sp. Def': '135', 'Speed': '55', 'Generation': '2', 'Legendary': 'False'}
>>> print(t[-1])
{'#': '292', 'Name': 'Shedinja', 'Type 1': 'Bug', 'Type 2': 'Ghost', 'HP': '1', 'Attack': '90', 'Defense': '45', 'Sp. Atk': '30', 'Sp. Def': '30', 'Speed': '40', 'Generation': '3', 'Legendary': 'False'}
>>> print(t[len(t)-1])
{'#': '292', 'Name': 'Shedinja', 'Type 1': 'Bug', 'Type 2': 'Ghost', 'HP': '1', 'Attack': '90', 'Defense': '45', 'Sp. Atk': '30', 'Sp. Def': '30', 'Speed': '40', 'Generation': '3', 'Legendary': 'False'}


#9
t[:3]
t[-3:] / t[len(t)-3:]
'''

def cle_tri(t):
    return int(t['HP'])
t.sort(key = cle_tri, reverse=True)