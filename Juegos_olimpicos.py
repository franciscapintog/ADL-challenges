import pandas as pd

df = pd.read_csv("athlete_events.csv")

ejercicio_3 = len(df["ID"].value_counts())
print(ejercicio_3)

athletes_s = df[df["Season"].eq("Summer")]["ID"].value_counts()
athletes_w = df[df["Season"].eq("Winter")]["ID"].value_counts()
print(athletes_s, athletes_w)

athletes_sw = len(pd.merge(athletes_s, athletes_w, on = "ID", how = "inner"))