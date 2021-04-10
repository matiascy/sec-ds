import pandas as pd
import plotly.express as px

pb = pd.read_excel('Samsung DS_Top Pages & Search Keyword_210224.xlsx')
pb.columns = pb.iloc[5]
print(pb.head(10))



