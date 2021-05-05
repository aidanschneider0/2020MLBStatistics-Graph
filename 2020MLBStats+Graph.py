from bs4 import BeautifulSoup as bs 
import requests
import re
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

#gets website
website = requests.get('https://www.espn.com/mlb/history/season/_/year/2020')

#creates soup with desired file parser, prettify makes it look nicer
soup = bs(website.content, 'html.parser')

#soup find all is a list so each header is an entry where we strip it.
x = 0
headerList = []
abbreviations = []
oddRowTeams = []
evenRowTeams = []
for header in soup.find_all('tr', class_ = 'stathead'):
	if(0 < x < 3):
		headerList.append(header.get_text())
		x += 1
	else:
		x += 1	

y = 0
for abbreviationsList in soup.find_all('tr', class_ = "colhead"):
	for abbreviation in abbreviationsList:
		if(16 > y > 5):
			abbreviations.append(abbreviation.get_text())
			y += 1
		else:
			y += 1



z = 0
for stats in soup.find_all(class_ = "oddrow"):
	for stat in stats:
		if(35 < z < 216):
			oddRowTeams.append(stat.get_text())	
			z += 1
		else:
			z += 1

z = 0
for stats in soup.find_all(class_ = "evenrow"):
	for stat in stats:
		if(24 < z < 145):
			evenRowTeams.append(stat.get_text().strip())	
			z += 1
		else:
			z += 1




#plotting each team's data to a variable 
iterator = 0
if(iterator == 0):
	rays = oddRowTeams[iterator:iterator+10]
	yankees = evenRowTeams[iterator:iterator+10]
	iterator += 10
	bluejays = oddRowTeams[iterator:iterator+10]
	orioles = evenRowTeams[iterator:iterator+10]
	iterator += 10
	redsox = oddRowTeams[iterator:iterator+10]
	whitesox = evenRowTeams[iterator:iterator+10]
	iterator += 10
	twins = oddRowTeams[iterator:iterator+10]
	royals = evenRowTeams[iterator:iterator+10]
	iterator += 10
	indians = oddRowTeams[iterator:iterator+10]
	astros = evenRowTeams[iterator:iterator+10]
	iterator += 10
	tigers = oddRowTeams[iterator:iterator+10]
	angels = evenRowTeams[iterator:iterator+10]
	iterator += 10
	athletics = oddRowTeams[iterator:iterator+10]
	marlins = evenRowTeams[iterator:iterator+10]
	iterator += 10
	mariners = oddRowTeams[iterator:iterator+10]
	mets = evenRowTeams[iterator:iterator+10]
	iterator += 10
	rangers = oddRowTeams[iterator:iterator+10]
	cardinals = evenRowTeams[iterator:iterator+10]
	iterator += 10
	braves = oddRowTeams[iterator:iterator+10]
	brewers = evenRowTeams[iterator:iterator+10]
	iterator += 10
	phillies = oddRowTeams[iterator:iterator+10]
	padres = evenRowTeams[iterator:iterator+10]
	iterator += 10
	nationals = oddRowTeams[iterator:iterator+10]
	rockies = evenRowTeams[iterator:iterator+10]
	iterator += 10
	cubs = oddRowTeams[iterator:iterator+10]
	iterator += 10
	reds = oddRowTeams[iterator:iterator+10]
	iterator += 10
	pirates = oddRowTeams[iterator:iterator+10]
	iterator += 10
	dodgers = oddRowTeams[iterator:iterator+10]
	iterator += 10
	giants = oddRowTeams[iterator:iterator+10]
	iterator += 10
	diamondbacks = oddRowTeams[iterator:iterator+10]
	
teams = []

count = 0
ALeast = {'Team': [rays[count], yankees[count], bluejays[count], orioles[count], redsox[count]]}
ALcentral = {'Team': [twins[count], whitesox[count], indians[count], royals[count], tigers[count]]}
ALwest = {'Team': [athletics[count], astros[count], mariners[count], angels[count], rangers[count]]}
NLeast = {'Team': [braves[count], marlins[count], phillies[count], mets[count], nationals[count]]}
NLcentral = {'Team': [cubs[count], cardinals[count], reds[count], brewers[count], pirates[count]]}
NLwest = {'Team': [dodgers[count], padres[count], giants[count], rockies[count], diamondbacks[count]]}
count += 1
	
while(count < 10):

	tempDict1 = {abbreviations[count]: [rays[count], yankees[count], bluejays[count], orioles[count], redsox[count]]}
	tempDict2 = {abbreviations[count]: [twins[count], whitesox[count], indians[count], royals[count], tigers[count]]}
	tempDict3 = {abbreviations[count]: [athletics[count], astros[count], mariners[count], angels[count], rangers[count]]}
	tempDict4 = {abbreviations[count]: [braves[count], marlins[count], phillies[count], mets[count], nationals[count]]}
	tempDict5 = {abbreviations[count]: [cubs[count], cardinals[count], reds[count], brewers[count], pirates[count]]}
	tempDict6 = {abbreviations[count]: [dodgers[count], padres[count], giants[count], rockies[count], diamondbacks[count]]}
	ALeast.update(tempDict1)
	ALcentral.update(tempDict2)
	ALwest.update(tempDict3)
	NLeast.update(tempDict4)
	NLcentral.update(tempDict5)
	NLwest.update(tempDict6)
	count += 1

positions = ["Position one:", "Position two:", "Position three:", "Position four:", "Position five:"]
#dataframe contains multiple series objects, data frame that is the TYPE of the df
#series make the dataframe so the type of the column is series. 

#this was seemed easier and was dictionaries made it weird
print(headerList[0])
df1 = pd.DataFrame(ALeast, index = [positions])
print(df1)

"""df2 = pd.DataFrame(ALcentral)
print(df2)

df3 = pd.DataFrame(ALwest)
print(df3)
print("\n")
print(headerList[1])
df4 = pd.DataFrame(NLeast)
print(df4)
df5 = pd.DataFrame(NLcentral)
print(df5)
df6 = pd.DataFrame(NLwest)
print(df6)"""

#df1[['W', 'L']] = df1[['W', 'L']].apply(pd.to_numeric)

newList = []
for i in abbreviations:
	newList.append(i)

newList[0] = "Team"
ALeastWinsString = (ALeast['W'])
ALeastWinsIntegers = []

#the figure is the object, you give this figure axes.
fig = plt.figure()

#taken from initial plot - only way I found to do it
ax = fig.add_axes([0.125,0.11,0.775,0.77])
ax.invert_xaxis()



print(ALeast['Team'])
for i in ALeastWinsString:
	ALeastWinsIntegers.append(int(i))

for i in np.arange(0,5,1):
	win = ALeastWinsIntegers[i]
	plt.bar(ALeast['Team'][i], win)

plt.xlabel("Team Name")
plt.ylabel("Wins")
plt.title("AL East Standings")

plt.show()

