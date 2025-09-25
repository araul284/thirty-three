# 🏁 Step 1: Install any missing libraries (Colab usually has these preinstalled)
!pip install pandas numpy matplotlib seaborn scikit-learn

# 🏁 Step 2: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For ML later
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 🏁 Step 3: Settings (to make plots pretty)
sns.set_style("darkgrid")   # nice plot background
plt.rcParams["figure.figsize"] = (10, 5)  # bigger plots

print("✅ Setup complete! Libraries imported successfully.")