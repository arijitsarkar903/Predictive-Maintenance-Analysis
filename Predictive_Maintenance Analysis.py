# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd #importing the necessary modules
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

pm_data= pd.read_csv('ai4i2020.csv') #importing the dataset

pm_data.head(10)

pm_data.tail(10)

# ## Data Preprocessing 


pm_data.isnull().sum() #checking the null values

pm_data.dropna(inplace=True)

pm_data.shape #size of the dataset

pm_data.info()

pm_data.describe()

# renaming columns
pm_data.rename(columns={'TWF':'Tool_wear_failure','HDF':'Heat_dissipation_failure ', 'PWF':'Power_failure', 'OSF':'Overstrain failure', 'RNF':'Random_failures'},inplace=True)

import warnings
warnings.filterwarnings("ignore") # removing warnings

pm_data= pm_data.drop(columns=['Product ID'])
pm_data= pm_data.drop(columns=['UDI'])

# ## EDA


# Univariate Analysis


#distribution of the machine failures
color= ['cyan', 'red']
plt.figure(figsize=(8,6))
sns.countplot(x='Machine failure', data=pm_data, palette= color, edgecolor='black')
plt.xlabel('Machine Failure distribution')
plt.ylabel('Count')
plt.show()

#  Pie Chart for the machine product Type distribution
plt.figure(figsize=(8, 6))
pm_data['Type'].value_counts().plot(kind='pie',autopct='%1.0f%%')
plt.title('Proportion of the Machine types')
plt.show()

# Distribution of the Air Temperature
plt.figure(figsize=(10, 6))
sns.histplot(pm_data['Air temperature [K]'], bins=30,color='brown',kde=True)
plt.title('Distribution of Air Temperature [K]')
plt.xlabel('Air Temperature [K]')
plt.ylabel('Frequency')
plt.show()

# Bivariate Analysis


# showing the graph Rotational Speed by Torque
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Rotational speed [rpm]', y='Torque [Nm]', data=pm_data, color='y', marker='*',  s=150)
plt.title('Rotational Speed vs. Torque')
plt.xlabel('Rotational Speed [rpm]')
plt.ylabel('Torque [Nm]')
plt.show()

# Defining the levels for the legend
levels = sorted(pm_data['Process temperature [K]'].unique())

# Scatter plot with the color according to 'Process temperature'
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(x='Air temperature [K]', y='Process temperature [K]', hue='Process temperature [K]',
                          palette='Reds', data=pm_data)
plt.title('Process Temperature vs. Air Temperature')
plt.xlabel('Air Temperature [K]')
plt.ylabel('Process Temperature [K]')

# Developing the legend with the discrete values
legend = scatter.legend(title='Process Temperature [K]', labels=[f'{level:.1f}' for level in levels],
                        fontsize='medium', markerscale=1.5)

plt.show()

# Multivariate Analysis


# Choosing crucial attributes for the correlation heatmap
data_modified = [
    'Air temperature [K]',
    'Process temperature [K]',
    'Rotational speed [rpm]',
    'Torque [Nm]',
    'Tool wear [min]',
    'Machine failure'
]

# Developing the correlation matrix
correlation_matrix = pm_data[data_modified].corr()

# Plotting the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='BrBG', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()

# Grouping by 'Type' and summing up the failure types
failure_counts = pm_data.groupby('Type')[['Tool_wear_failure','Heat_dissipation_failure ','Power_failure', 'Overstrain failure','Random_failures']].sum().reset_index()

# Reshaping the data for Seaborn's bar plot
failure_counts = failure_counts.melt(id_vars='Type', var_name='Failure Type', value_name='Count')

# Plotting the grouped bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Type', y='Count', hue='Failure Type', data=failure_counts, palette='Set2', edgecolor='black')
plt.title('Failure Types by Product Type')
plt.xlabel('Product Type')
plt.ylabel('Count')
plt.legend(title='Failure Type')
plt.show()

# ## Additional Preprocessing


from sklearn.preprocessing import LabelEncoder
# Instantiate LabelEncoder
label_encoder = LabelEncoder()

# Encode categorical variable 'Type' to numeric
pm_data['Type'] = label_encoder.fit_transform(pm_data['Type'])

pm_data.head(15)

# Converting the float data to integer data
pm_data['Torque [Nm]'] = pm_data['Torque [Nm]'].astype(int)
pm_data['Air temperature [K]'] = pm_data['Air temperature [K]'].astype(int)
pm_data['Process temperature [K]'] = pm_data['Process temperature [K]'].astype(int)

pm_data.tail()



