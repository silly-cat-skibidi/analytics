irish_players = df[df['nationality_name'] == 'Republic of Ireland']
print(irish_players) #this gets an exact match of our criteria

irish_players= df[df[ 'nationality_name'] == 'Republic of Ireland']
print(irish_players[['short_name', 'overall']]) #same thing but adds the rows
#real program example
prem = df [df['league_name']
print(prem['club_name'])'English Premier League']
#show 20 premier league clubs
prem=df[df['league_name']=='English Premier League']
print (prem['club_name'].drop_duplicates())
#retrieving number data
new_dfdf[['short_name', 'value_eur', 'player_positions', 'pace']]
over 50m = new_df[df['value_eur'] > 50000000]
print (over50m)
#contains the value
pacewith8 = new_df[df['pace'].astype('str').str.contains('8')]
print(pacewith8)
#retrieving multiple data
new_df[(df['value_eur'] > 50000000) & (df[ 'league_name']=='English Premier League')]=over50mEPL
print(over50mEPL) #this is an and statement
#this is or
irlor92 = new_df[(df['nationality_name'] =='Republic of Ireland') | (df['overall'] > 92)]print(irlor92)
print(irlor92)
#this is a not
notunder90 = df [~(df['overall'] < 90)]
print(notunder90[ ['short_name', 'overall']])
#the loc function helps retrieve data values with ease
over25 = df.loc[df['age'] > 25, ['short_name', 'age']]
print(over25)
#passing the loc call that contain man
manclubs = df.loc[df['club_name'].str.contains('Man', case=False, na=False), ['short_name', 'age', 'club_name']]
print(manclubs)
#rows
rows = df.loc[1:5]
print(rows['short_name'])
#slicing
slicing = df.loc[1:5, 'short_name':'overall']
print(slicing)