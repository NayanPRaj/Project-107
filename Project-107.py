import pandas as pd
import plotly.express as px


df=pd.read_csv("./Project-107.csv")
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
print(mean)

fig=px.scatter(mean,x="student_id",y="level",color="attempt",size="attempt")
fig.show()

