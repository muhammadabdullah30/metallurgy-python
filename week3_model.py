import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt





df = pd.read_csv('process_data_100.csv')

grade_dummies = pd.get_dummies(df['scrap_grade'], prefix='grade').astype(int)

X = pd.concat([
    df[['temperature', 'flux', 'input_mass']],
    grade_dummies
], axis=1)

y = df['recovery_rate']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print('Training rows:', len(X_train))
print('Testing rows:', len(X_test))





lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)

lr_mae = mean_absolute_error(y_test, lr_predictions)
lr_r2 = r2_score(y_test, lr_predictions)

print('\n--- Linear Regression ---')
print(f'MAE: {lr_mae:.2f}%')
print(f'R2 Score: {lr_r2:.3f}')


rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_r2 = r2_score(y_test, rf_predictions)

print('\n--- Random Forest ---')
print(f'MAE: {rf_mae:.2f}%')
print(f'R2 Score: {rf_r2:.3f}')



importances = rf_model.feature_importances_
features = X.columns

plt.figure(figsize=(8, 5))
plt.barh(features, importances, color='steelblue')
plt.xlabel('Importance Score')
plt.title('What Drives Recovery Rate — Random Forest')
plt.tight_layout()
plt.savefig('chart4_feature_importance.png')
plt.show()
print('\nChart saved')