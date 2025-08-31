#Renewable Energy & AI - Green Skills Project
#Loads, cleans, and processes renewable energy data from Kaggle for EduNet Green Skills project.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler

# Load dataset 
df = pd.read_csv('./data/renewable_energy.csv') 

# Explore
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Cleaning
df = df.dropna()
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Feature engineering
if 'renewable_energy_production' in df.columns and 'total_energy_production' in df.columns:
    df['renewable_share'] = (df['renewable_energy_production'] / df['total_energy_production']) * 100

if 'year' in df.columns and 'renewable_energy_production' in df.columns:
    df['yearly_growth'] = df.groupby('country')['renewable_energy_production'].pct_change() * 100

# Save cleaned dataset
Path('./data').mkdir(exist_ok=True)
df.to_csv('./data/renewable_energy_clean.csv', index=False)
print("✅ Clean dataset saved to data/renewable_energy_clean.csv")
