# #Selects the first 20 from both columns
# plt.plot(df["short_name"].dropna().head(20),df["power_strenght"].dropna()head(20))
# #rotates the x-axis 45 degrees, to view all names
# plt.xticks(rotation= 45, ha="right")
# plt.title("Top 20 Players Strenght")
# plt.xlabel("Names")
# plt.ylabel("strenght")
# #To view the names on the x-axis
# plt.tight_layout(h_pad=1.0)
# plt.show()

# #Selects the first 20 from both columns and attaches label which will be in line 1
# plt.plot(df["short_name"].dropna().head(20),df["power_strenght"].dropna()head(20), label="Strength")
# #Selects the first 20 from both columns and attaches label which will be in line 2
# plt.plot(df["short_name"].dropna().head(20),df["movement_acceleration"].dropna()head(20),label="Pace")
# plt.xticks(rotation= 45, ha="right")
# plt.title("Top 20 Players\nStrenght and Pace")
# plt.xlabel("Names")
# plt.ylabel("stats")
# plt.tight_layout(h_pad=1.0)
# #Creats a legend for the labels
# plt.legend
# plt.show()

# #Reduce the dataframe down to a specific team
# harpsdf=df[df["club_name"] == "Finn Harps"]
# #Creates a bar chart with 2 columns of equal size with bar colours of blue and yellow
# plt.bar(harpsdf["short_name"],harpsdf["overall"],color=["blue","yellow"])
# plt.xticks(rotation=45, ha="right")
# plt.title("Finn Harps Squad")
# plt.xlabel("Names")
# plt.ylabel("Overall")
# plt.tight_layout(h_pad=1.0)
# plt.show()

#plt.bar(counties,population,color=["green","white"],edgecolor=["blue"]

# avgleagues=df.groupby("league_name")["value_eur"].mean().sort_values(ascending=False)
# top10leagues=list(avgleagues[:10])
# top10values = list(avgleagues[:10].keys())
# plt.ticklabel_format(style= "plain")
# plt.bar(top10values,top10leagues)
# plt.xticks(rotation=45, ha="right")
# plt.title("Average Price of Player\nin Top 10 Leagues")
# plt.xlabel("Leagues")
# plt.ylabel("Average Value")
# plt.tight_layout(h_pad=1.0)
# plt.show()

# irishleaguedf=df[df["league_name"] == "Rep Ireland Airtricity League"]
# irishleagueddf= irishleaguedf.groupby("club_name")[["overall","pace","movemnet_acceleration"]].mean()
# print(list(irishleaguedf.index))

# import numpy as np
# x=np.arange(len(irishleaguedf))
# y1=list(irishleaguedf["overall"])
# y2=list(irishleaguedf["pace"])
# y3=list(irishleaguedf["movement_acceleration"])
# width=0.3
# plt.bar(x-0.3,y1,width,color=["green"])
# plt.bar(x,y2,width,color=["blue"])
# plt.bar(x+0.3,y3,width,color=["orange"])
# plt.xticks(x,list(irishleaguedf.index),rotation=45,ha="right")
# plt.tight_layout()
# plt.show

# foot=df["preferred_foot"].value_counts()
# plt.title("Preferred Foot")
# plt.pie(foot,labels= foot.keys())
# plt.show

# nationalities=df["nationality_name"].value_counts()
# print(nationalities[:10])
# plt.title("Top 10 Number of Nationalities in Fifa")
# plt.pie(nationalities[:10],labels=nationalities.index[:10])
# plt.show()

# prem_league=df.loc[df["league_name"] == "English Premier League"]
# plt.title("Premier League overall distribution")
# plt.scatter(prem_league["short_name"],prem_league["overall"])
# plt.ylabel("overalls")
# plt.show

# prem=df.loc[df["League_name"] == "English premier league"]
# premace= prem.loc[prem.groupby("club_name")["pace"].idxmax()]
# plt.scatter(prempace["short_name"].premace["pace"])
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show

# plt.hist(df.groupby("league_name")["overall"].mean(),color=["green"])
# plt.title("Overall")
# plt.ylabel("Times")
# plt.xlabel("Overall")
# plt.show

# cpus=["Intel Core i9-11900k","AMD Ryzen 9 5950X","Intel Core i7-11700K",]
# benchmark_score=[1443,1597,1405,1520]
# max_temp=[82,69,85,72]
# plt.plot(cpus,benchmark_score)
# plt.plot(cpus,max_temp)
# plt.show()

# cpus=["Intel Core i9-11900k","AMD Ryzen 9 5950X","Intel Core i7-11700K",]
# single_thred_score=[164,167,155,161]
# multi_thread_score=[1172,1388,1216,1326]
# thermal_design_power=[125,105,125,105]
# plt.plot(cpus,single_thread_score)
# plt.plot(cpus, multi_thread_score)
# plt.plot(cpus,thermal_design_power)
# plt.show()