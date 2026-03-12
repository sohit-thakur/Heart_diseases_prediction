import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Define Middle-Aged (roughly 40-64 based on common AgeCategory)
middle_age_cats = ['40-44', '45-49', '50-54', '55-59', '60-64']
df_middle_aged = df[df['AgeCategory'].isin(middle_age_cats)]

# 1. Visualization for Dr. Sharma: Lifestyle Factors in Middle-Aged patients
plt.figure(figsize=(14, 10))

# Subplot 1: Smoking vs Heart Disease
plt.subplot(2, 2, 1)
sns.countplot(data=df_middle_aged, x='Smoking', hue='HeartDisease', palette='viridis')
plt.title('Smoking & Heart Disease (Middle-Aged: 40-64)')

# Subplot 2: Physical Activity vs Heart Disease
plt.subplot(2, 2, 2)
sns.countplot(data=df_middle_aged, x='PhysicalActivity', hue='HeartDisease', palette='viridis')
plt.title('Physical Activity & Heart Disease (Middle-Aged)')

# Subplot 3: BMI Distribution by Heart Disease status
plt.subplot(2, 2, 3)
sns.boxplot(data=df_middle_aged, x='HeartDisease', y='BMI', palette='Set2')
plt.title('BMI Distribution vs Heart Disease (Middle-Aged)')

# Subplot 4: Sleep Time vs Heart Disease
plt.subplot(2, 2, 4)
sns.boxplot(data=df_middle_aged, x='HeartDisease', y='SleepTime', palette='Set3')
plt.title('Sleep Time vs Heart Disease (Middle-Aged)')

plt.tight_layout()
plt.savefig('dr_sharma_lifestyle.png')

# 2. Visualization for Ramesh: Population Trends & Sedentary Lifestyle
plt.figure(figsize=(14, 10))

# Subplot 1: Prevalence by Race
plt.subplot(2, 2, 1)
race_hd = df.groupby('Race')['HeartDisease'].apply(lambda x: (x == 'Yes').mean() * 100).sort_values(ascending=False)
sns.barplot(x=race_hd.values, y=race_hd.index, palette='magma')
plt.title('Heart Disease Prevalence (%) by Race')
plt.xlabel('Prevalence (%)')

# Subplot 2: Physical Activity Impact
plt.subplot(2, 2, 2)
activity_hd = df.groupby('PhysicalActivity')['HeartDisease'].apply(lambda x: (x == 'Yes').mean() * 100)
sns.barplot(x=activity_hd.index, y=activity_hd.values, palette='coolwarm')
plt.title('Prevalence by Physical Activity Status')
plt.ylabel('Prevalence (%)')

# Subplot 3: Age Category Trends
plt.subplot(2, 1, 2)
age_hd = df.groupby('AgeCategory')['HeartDisease'].apply(lambda x: (x == 'Yes').mean() * 100).sort_index()
sns.lineplot(x=age_hd.index, y=age_hd.values, marker='o', color='red')
plt.title('Heart Disease Prevalence Trend by Age')
plt.ylabel('Prevalence (%)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('ramesh_population_trends.png')

# 3. Visualization for Anita: Health Benchmarking
plt.figure(figsize=(12, 6))

# Melt data for benchmarking
health_metrics = df.groupby('HeartDisease')[['PhysicalHealth', 'MentalHealth', 'SleepTime']].mean().reset_index()
health_metrics_melted = health_metrics.melt(id_vars='HeartDisease', var_name='Metric', value_name='Average Days/Hours')

sns.barplot(data=health_metrics_melted, x='Metric', y='Average Days/Hours', hue='HeartDisease', palette='muted')
plt.title('Average Health Metrics: Heart Disease (Yes) vs Healthy Benchmarks (No)')
plt.savefig('anita_benchmarks.png')

print("Visualizations created.")