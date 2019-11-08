import pandas as pd

whr = pd.read_csv("2015.csv")

print(whr['Country'][0:22])