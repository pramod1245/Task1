# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DKqkj9HGy9vzQOFls_mQi_baObY18OLM
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
# %matplotlib inline

df = pd.read_csv("/content/Titanic_Synthetic_Dataset.csv")


print("Dataset Info:")
print(df.info())
print("\nDescriptive Statistics:")
print(df.describe())
print("\nValue Counts:")
print("Survived:\n", df['survived'].value_counts())
print("Pclass:\n", df['pclass'].value_counts())
print("Sex:\n", df['sex'].value_counts())
print("Embarked:\n", df['embarked'].value_counts())

sns.pairplot(df[['age', 'fare', 'sibsp', 'parch', 'survived']], hue='survived')
plt.suptitle("Pairplot of Features by Survival", y=1.02)
plt.show()


plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


df.hist(column=['age', 'fare', 'sibsp', 'parch'], bins=20, figsize=(12, 8), color='skyblue')
plt.suptitle("Histograms of Numeric Columns")
plt.show()


plt.figure(figsize=(10, 5))
sns.boxplot(x='pclass', y='age', data=df)
plt.title("Boxplot of Age by Passenger Class")
plt.show()

sns.boxplot(x='sex', y='fare', data=df)
plt.title("Boxplot of Fare by Gender")
plt.show()

plt.figure(figsize=(10, 5))
sns.scatterplot(x='age', y='fare', hue='survived', data=df)
plt.title("Age vs Fare Colored by Survival")
plt.show()


print("\n🔍 Observations:")
print("""
1. Most passengers are in 3rd class, with more males than females.
2. Average fare increases with passenger class.
3. Survivors tend to be female and from higher classes.
4. Age and fare show weak correlation with survival, but higher fares suggest higher survival.
5. Boxplots show younger passengers and women had a better chance of survival.
""")

print("\n🧾 Summary:")
print("""
This EDA helped uncover key trends:
- Higher-class passengers had higher survival rates.
- Female passengers had better survival chances.
- Fare and age distributions varied by survival and class.
These insights could support predictive modeling or policy planning in real-world scenarios.
""")



pip install gradio













