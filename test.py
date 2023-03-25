from steam import Steam
from decouple import config
import pandas as pd
import numpy as np

testfile = open('test.txt', 'w')

KEY = config("STEAM_API_KEY")
steam = Steam(KEY)

user = steam.apps.search_games("Persona")

listResult = user.get("apps")

df = pd.DataFrame.from_records(listResult)

np.savetxt(r'test.txt', df.values, header="ID\tLINK\tNAME\tIMG\tPRICE", fmt='%s')

print(df['id'].iloc[0])
print(len(df['id']))