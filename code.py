import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")

print(df.groupby("level")["attempt"].mean())

fig=px.scatter(df.groupby("level")["attempt"].mean(),x=["level1","level2","level3","level4"],y="attempt",color="attempt")

fig.show()