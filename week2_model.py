import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

#loading clean data
df = pd.read_csv('process_data_clean.csv')

#preparing features
#one hot encode scrap grade
grade_dummies = pd.get_dummies(df['scrap_grade'], prefix='grade').astype(int)
print('One hot encoded grades: ')
print(grade_dummies)

#building feature matirix
X = pd.concat([
    df[['temperature', 'flux', 'input_mass']],
    grade_dummies
], axis=1)

#Target variable
y = df['recovery_rate']

print('\nFeatures shape:', X.shape)
print('Target shape:', y.shape)

#splitting data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print('\nTraining rows:', len(X_train))
print('Testing rows:', len(X_test))

#Training model
model = LinearRegression()
model.fit(X_train, y_train)

#evaluating model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print('\n--- Model Results ---')
print(f'Mean Absolute Error: {mae:.2f}%')
print(f'R2 Score: {r2:.3f}')

#what matters most
print('\n--- Feature Importance ---')
for feature, coef in zip(X.columns, model.coef_):
    print(f'{feature}: {coef:.4f}')