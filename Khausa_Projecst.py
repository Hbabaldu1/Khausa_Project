import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


# Load dataset
data = pd.read_csv("POWER_Point_Daily_20000101_20260101_012d24N_009d91E_LST.csv", skiprows=12)

# Rename columns
data = data.rename(columns={
    'T2M': 'Temp',
    'RH2M': 'Humidity',
    'PS': 'Pressure',
    'WS2M': 'Wind'
})

# Convert YEAR + DOY to real date
data['Date'] = pd.to_datetime(data['YEAR'].astype(str) + data['DOY'].astype(str), format='%Y%j')

# Set as index
data = data.set_index('Date')

# Create next-day temperature target
data['Target'] = data['Temp'].shift(-1)

# Drop last row (NaN target)
data = data.dropna()

#Features & Target
X = data[['Temp', 'Humidity', 'Pressure', 'WS2M_MAX']]
y = data['Target']

#Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)



                    #Model Training
#=================================================
#Linear Regression
# lr_model = LinearRegression()

# lr_model.fit(X_train, y_train)

# lr_predictions = lr_model.predict(X_test)

# #Evaluate Linear Regression
# lr_mae = mean_absolute_error(y_test, lr_predictions)
# lr_mse = mean_squared_error(y_test, lr_predictions)

# print("Linear Regression MAE:", lr_mae)
# print("Linear Regression MSE:", lr_mse)

# #Plot Actual vs Predicted
# plt.figure()

# plt.plot(y_test.values[:100], label='Actual')
# plt.plot(lr_predictions[:100], label='Predicted')

# plt.title("Linear Regression: Actual vs Predicted Temperature")
# plt.xlabel("Samples")
# plt.ylabel("Temperature (°C)")
# plt.legend()

# plt.show()

#=================================================
#DECISION TREE
# dt_model = DecisionTreeRegressor(random_state=42)

# dt_model.fit(X_train, y_train)

# dt_predictions = dt_model.predict(X_test)

# #Evaluate
# dt_mae = mean_absolute_error(y_test, dt_predictions)
# dt_mse = mean_squared_error(y_test, dt_predictions)

# print("Decision Tree MAE:", dt_mae)
# print("Decision Tree MSE:", dt_mse)

# #Plot Results
# plt.figure()

# plt.plot(y_test.values[:100], label='Actual')
# plt.plot(dt_predictions[:100], label='Predicted')

# plt.title("Decision Tree: Actual vs Predicted Temperature")
# plt.xlabel("Samples")
# plt.ylabel("Temperature (°C)")
# plt.legend()

# plt.show()


#=================================================
#RANDOM FOREST
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)


#Evaluate
rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_mse = mean_squared_error(y_test, rf_predictions)

# print("Random Forest MAE:", rf_mae)
# print("Random Forest MSE:", rf_mse)

#Plot Results
# plt.figure()

# plt.plot(y_test.values[:100], label='Actual')
# plt.plot(rf_predictions[:100], label='Predicted')

# plt.title("Random Forest: Actual vs Predicted Temperature")
# plt.xlabel("Samples")
# plt.ylabel("Temperature (°C)")
# plt.legend()

# plt.show()

#=================================================
#FEATURE IMPORTANCE ANALYSIS
importance = rf_model.feature_importances_

features = X.columns

importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': importance
})

print(importance_df)

#PLOT FEATURE IMPORTANCE
plt.figure()

plt.bar(features, importance)

plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")

plt.show()







































# print(data.describe())