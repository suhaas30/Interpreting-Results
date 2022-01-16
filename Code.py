import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("filtered_stars.csv")

star_name = df["Star_name"].tolist()
distance = df["Distance"].tolist()
mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

star_name.sort()
distance.sort()
mass.sort()
radius.sort()
gravity.sort()

plt.bar(star_name, mass)
plt.title("Bar chart for Mass and Star Name")
plt.xlabel("Mass")
plt.ylabel("Star Name")
plt.show()

plt.bar(star_name, distance)
plt.title("Bar chart for Distance and Star Name")
plt.xlabel("Distance")
plt.ylabel("Star Name")
plt.show()

plt.bar(star_name, radius)
plt.title("Bar chart for Radius and Star Name")
plt.xlabel("Radius")
plt.ylabel("Star Name")
plt.show()

plt.bar(star_name, gravity)
plt.title("Bar chart for Gravity and Star Name")
plt.xlabel("Gravity")
plt.ylabel("Star Name")
plt.show()