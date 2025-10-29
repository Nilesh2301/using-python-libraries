
# 🏏 CRICKET SCORE ANALYSIS (Real-Life Data Project)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Create a Realistic Dataset


np.random.seed(42)

players = [
    "Rohit Sharma", "Virat Kohli", "Shubman Gill", "Suryakumar Yadav",
    "KL Rahul", "Hardik Pandya", "Ravindra Jadeja", "Rinku Singh",
    "Shreyas Iyer", "Ishan Kishan", "Jasprit Bumrah", "Mohammed Shami"
]

matches = np.random.randint(10, 30, len(players))
runs = np.random.randint(300, 1500, len(players))
balls = np.random.randint(200, 1200, len(players))
fifties = np.random.randint(0, 10, len(players))
hundreds = np.random.randint(0, 5, len(players))
not_outs = np.random.randint(0, 5, len(players))

df = pd.DataFrame({
    "Player": players,
    "Matches": matches,
    "Runs": runs,
    "Balls Faced": balls,
    "50s": fifties,
    "100s": hundreds,
    "Not Outs": not_outs
})

# Derived Stats
df["Average"] = (df["Runs"] / (df["Matches"] - df["Not Outs"]).replace(0, 1)).round(2)
df["Strike Rate"] = ((df["Runs"] / df["Balls Faced"]) * 100).round(2)
df["Boundary %"] = (np.random.uniform(40, 70, len(players))).round(2)

print("\n🏏 Cricket Dataset (First 5 Players):")
print(df.head())


#  Summary & Basic Stats

print("\n📊 Statistical Summary:")
print(df.describe())

top_scorer = df.loc[df["Runs"].idxmax()]
best_avg = df.loc[df["Average"].idxmax()]
best_sr = df.loc[df["Strike Rate"].idxmax()]

print("\n🏆 Top Scorer:", top_scorer["Player"], "with", top_scorer["Runs"], "runs")
print("💪 Best Batting Average:", best_avg["Player"], "with", best_avg["Average"])
print("⚡ Highest Strike Rate:", best_sr["Player"], "with", best_sr["Strike Rate"])

# Step 3: Visual Analysis


#Total Runs by Player
plt.figure(figsize=(8,5))
plt.bar(df["Player"], df["Runs"], color="orange")
plt.title("Total Runs by Player")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Runs")
plt.tight_layout()
plt.show()

# Batting Average Comparison
plt.figure(figsize=(8,5))
plt.plot(df["Player"], df["Average"], marker='o', color="blue", label="Average")
plt.title("Batting Average Comparison")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Average")
plt.legend()
plt.tight_layout()
plt.show()

#  Strike Rate vs Average
plt.figure(figsize=(6,5))
plt.scatter(df["Strike Rate"], df["Average"], color="green", s=80)
plt.title("Strike Rate vs Batting Average")
plt.xlabel("Strike Rate")
plt.ylabel("Average")
for i, player in enumerate(df["Player"]):
    plt.text(df["Strike Rate"][i]+0.3, df["Average"][i]+0.3, player, fontsize=8)
plt.grid(True)
plt.tight_layout()
plt.show()

#  Fifties and Hundreds Comparison
plt.figure(figsize=(7,5))
width = 0.35
x = np.arange(len(df["Player"]))
plt.bar(x - width/2, df["50s"], width, label="50s", color="skyblue")
plt.bar(x + width/2, df["100s"], width, label="100s", color="gold")
plt.xticks(x, df["Player"], rotation=45, ha="right")
plt.title("Half Centuries vs Centuries")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()
plt.show()

#run contri per player
plt.figure(figsize=(7,5))
plt.pie(df["Runs"], labels=df["Player"], autopct="%1.1f%%", startangle=120)
plt.title("Run Contribution by Player")
plt.tight_layout()
plt.show()






# Insights

print("\n📈 Insights:")
print(f"• Average Team Strike Rate: {df['Strike Rate'].mean():.2f}")
print(f"• Average Team Batting Average: {df['Average'].mean():.2f}")
print(f"• Most Consistent Player: {best_avg['Player']}")
print(f"• Most Aggressive Player: {best_sr['Player']}")
print(f"• Total Team Runs: {df['Runs'].sum()}")


# Save Result

df.to_csv("Cricket_Score_Analysis.csv", index=False)
print("\n✅ Analysis completed and saved as 'Cricket_Score_Analysis.csv'")
