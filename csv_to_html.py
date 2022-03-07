import pandas as pd

df = pd.read_csv("Resources/cities.csv")

df.to_html("cities.html", index=False)
