# Predictive-Maintenance-Analysis

**Predictive Maintenance Dataset (AI4I 2020)**

Dataset link: https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020/data 

This project aims to enhance the understanding of factors leading to machine failures in milling operations through detailed analysis and visualization of relevant data. By identifying key process parameters affecting machine performance, the project seeks to develop predictive maintenance strategies, reduce downtime, and improve overall efficiency. The insights gained will help in implementing proactive maintenance schedules, ultimately extending the lifespan of the machinery and optimizing production processes.

**Dataset Variables**
- i) UID: Unique identifier for each record.
- ii) Product ID: Product quality variant and serial number.
- iii) Type: Product type (L, M, H).
- iv) Air temperature [K]: Ambient air temperature in Kelvin.
- v) Process temperature [K]: Temperature during processing in Kelvin.
- vi) Rotational speed [rpm]: Speed of rotation in revolutions per minute.
- vii) Torque [Nm]: Applied torque in Newton-meters.
- viii) Tool wear [min]: Duration of tool usage in minutes.
- ix) Machine failure: Indicates if a machine failure occurred.
- x) TWF: Tool wear failure indicator.
- xi) HDF: Heat dissipation failure indicator.
- xii) PWF: Power failure indicator.
- xiii) OSF: Overstrain failure indicator.
- xiv) RNF: Random failure indicator.

**Visualizations**

1. _Distribution of Machine Failures (Count Plot)_
Visualizes the count of machine failures and non-failures.

2. _Pie Chart of Machine Product Type Distribution_
Shows the proportion of different machine product types (L, M, H).

3. _Distribution of Air Temperature (Histogram)_
Illustrates the distribution of ambient air temperature in Kelvin.

4. _Scatter Plot of Rotational Speed vs. Torque_
Displays the relationship between rotational speed and torque with data points marked as stars.

5. _Scatter Plot of Process Temperature vs. Air Temperature_
Examines the relationship between process temperature and air temperature, with colors indicating process temperature values.

6. _Correlation Heatmap of Key Attributes_
Provides a visual representation of the correlation between key attributes, indicating how they are related.

7. _Grouped Bar Plot of Failure Types by Product Type_
Compares the count of different failure types (TWF, HDF, PWF, OSF, RNF) across product types (L, M, H).
