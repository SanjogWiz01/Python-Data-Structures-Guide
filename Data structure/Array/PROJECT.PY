# Nepal_Flood_Risk_Simple.py

# Data arrays (lists)
districts = ["Kathmandu", "Chitwan", "Sunsari", "Dang", "Jhapa"]
rivers = ["Bagmati", "Rapti", "Koshi", "Babai", "Kankai"]
rainfall_mm = [1200, 1600, 1800, 900, 1700]
water_levels_m = [4.5, 5.2, 6.5, 3.2, 5.8]
population = [1000000, 500000, 600000, 400000, 350000]

# 1️⃣ Identify high-risk districts (Rainfall >1500 OR Water Level >5.0)
high_risk_districts = []
for i in range(len(districts)):
    if rainfall_mm[i] > 1500 or water_levels_m[i] > 5.0:
        high_risk_districts.append(districts[i])
print("High-risk Districts:", high_risk_districts)

# 2️⃣ Total population at risk
total_pop_risk = 0
for i in range(len(districts)):
    if districts[i] in high_risk_districts:
        total_pop_risk += population[i]
print("Total Population at Risk:", total_pop_risk)

# 3️⃣ Districts sorted by water level (descending)
combined = list(zip(districts, water_levels_m))
combined.sort(key=lambda x: x[1], reverse=True)
print("Districts sorted by Water Level:")
for district, level in combined:
    print(district, "-", level, "m")

# 4️⃣ Simple Visualization
import matplotlib.pyplot as plt

plt.bar(districts, water_levels_m, color='skyblue')
plt.ylabel("Water Level (m)")
plt.title("River Water Levels in Nepal")
plt.show()
# 5️⃣ Average Rainfall