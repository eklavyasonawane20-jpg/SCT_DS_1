import matplotlib.pyplot as plt

# Step 1: Data define karo
age_groups = ["0-20 Years", "21-64 Years", "65+ Years"]
population_percent = [36.1, 57.0, 6.9]   # In percentage
population_million = [512, 807, 98]      # In millions

# Step 2: Bar chart banao
plt.bar(age_groups, population_percent, color=["yellow", "blue", "pink"])

# Step 3: Labels and title
plt.xlabel("Age Groups")
plt.ylabel("Population (%)")
plt.title("India's Population Distribution by Age (2022)")

# Step 4: Show chart
plt.show()
