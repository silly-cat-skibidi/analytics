#FILTERING

# import pandas
# 
# df = pandas.read_csv("players_22.csv")

# germanAge_Pos = df.loc[(df["nationality_name"] == "Germany"), ["short_name", "club_name", "player_positions", "pace"]]
# print(germanAge_Pos)
# print(germanAge_Pos.dropna())

#print(df["age"])
# print(df["age"].drop_duplicates())


# prem = df[df["league_name"] == "English Premier League"]
# #print(prem["club_name"].drop_duplicates())
# 
# print(prem[["club_name", "nationality_name"]].drop_duplicates())

# print(df["value_eur"])
# print(df["value_eur"].astype("str"))

# print(df.loc[df["overall"] >88, ["short_name", "club_name", "overall"]].to_string())

# print(df["wage_eur"])

#need to remove nulls to convert to int
# print(df["wage_eur"].dropna().astype(f"int"))

#convert pandas column to a list
# print(list(df["club_name"].drop_duplicates()))
# print(list(df["short_name"][:10]))
# print(list(df["value_eur"][:10]))

# print(dict(df["short_name"][:10]))

# datadict = dict(df["short_name"][:10])
# for index, value in datadict.items():
#     print(index, "is", value)
# print(list(df["value_eur"][:10]))

# datadict = dict(df[["short_name", "overall", "club_name"]][:10])
# print(datadict["overall"])

#REPLACING VALUES
# fifa_23 = pandas.read_csv("FIFA23_official_data.csv")
# bad_data = fifa_23[["Height", "Weight", "Wage", "Value", "Position"]]
# #print(bad_data)
# bad_data["Height"] = bad_data["Height"].str.replace("cm", "")
# #print(bad_data)
# bad_data["Weight"] = bad_data["Weight"].str.replace("kg", "")
# #print(bad_data)
# bad_data["Weight"] = bad_data["Weight"].astype("int")
# 
# #replacing euro signs and ks and ms
# bad_data["Wage"] = bad_data["Wage"].str.replace("€", "")
# bad_data["Wage"] = bad_data["Wage"].replace({"K": "*1e3","M": "*1e6"}, regex=True).map(pandas.eval).astype(int)
# bad_data["Value"] = bad_data["Value"].str.replace("€", "")
# bad_data["Value"] = bad_data["Value"].replace({"K": "*1e3","M": "*1e6"}, regex=True).map(pandas.eval).astype(int)
# #print(bad_data)

# bad_data["Position"] = bad_data["Position"].str.split(pat=">").str[1]
# print(bad_data["Position"])