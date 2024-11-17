# import streamlit as st
# import pandas as pd
# import numpy as np
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error
# import matplotlib.pyplot as plt

# # Load datasets
# def load_data():
#     train_data = pd.read_csv("raw/train_FD001.txt", sep=" ", header=None).iloc[:, :-2]
#     test_data = pd.read_csv("raw/test_FD001.txt", sep=" ", header=None).iloc[:, :-2]
#     rul_data = pd.read_csv("raw/RUL_FD001.txt", sep=" ", header=None, names=["RUL"])
#     return train_data, test_data, rul_data

# # Preprocess training data
# def preprocess_data(data):
#     columns = ['Engine_ID', 'Cycle', 'Op_Set1', 'Op_Set2', 'Op_Set3'] + [f'Sensor_{i}' for i in range(1, 22)]
#     data.columns = columns
#     data['RUL'] = data.groupby('Engine_ID')['Cycle'].transform(max) - data['Cycle']
#     data.fillna(0, inplace=True)  # Handle missing values
#     return data

# # Preprocess test data
# def preprocess_test_data(test_data, rul_data):
#     columns = ['Engine_ID', 'Cycle', 'Op_Set1', 'Op_Set2', 'Op_Set3'] + [f'Sensor_{i}' for i in range(1, 22)]
#     test_data.columns = columns

#     # Filter the last cycle for each engine
#     test_data_last_cycle = test_data.groupby('Engine_ID').last().reset_index()

#     # Match RUL values based on Engine_ID
#     test_data_last_cycle = test_data_last_cycle.merge(rul_data, left_on='Engine_ID', right_index=True)

#     test_data_last_cycle.fillna(0, inplace=True)  # Handle missing values
#     return test_data_last_cycle

# # Train model
# def train_model(X_train, y_train):
#     model = RandomForestRegressor(n_estimators=100, random_state=42)
#     model.fit(X_train, y_train)
#     return model

# # Evaluate model
# def evaluate_model(model, X_test, y_test):
#     predictions = model.predict(X_test)
#     mse = mean_squared_error(y_test, predictions)
#     return mse, predictions

# # Plot results
# def plot_results(y_true, y_pred):
#     plt.figure(figsize=(10, 6))
#     plt.scatter(range(len(y_true)), y_true, label="Actual RUL", color="blue", alpha=0.6)
#     plt.scatter(range(len(y_pred)), y_pred, label="Predicted RUL", color="red", alpha=0.6)
#     plt.title("Actual vs Predicted Remaining Useful Life (RUL)")
#     plt.xlabel("Engine Instance")
#     plt.ylabel("RUL")
#     plt.legend()
#     plt.grid(True)
#     st.pyplot(plt)

# # Streamlit application
# def main():
#     st.title("Predictive Maintenance for OEMs")
#     st.write("This app predicts the Remaining Useful Life (RUL) of engines.")

#     # Load and preprocess data
#     train_data, test_data, rul_data = load_data()
#     train_data = preprocess_data(train_data)
#     test_data = preprocess_test_data(test_data, rul_data)

#     # Prepare training and testing sets
#     X_train = train_data.drop(['Engine_ID', 'RUL'], axis=1)
#     y_train = train_data['RUL']
#     X_test = test_data.drop(['Engine_ID', 'RUL'], axis=1)
#     y_test = test_data['RUL']

#     # Check for missing values
#     st.write("Checking for missing values in datasets...")
#     st.write("X_train missing values:", X_train.isnull().sum().sum())
#     st.write("y_train missing values:", y_train.isnull().sum())
#     st.write("X_test missing values:", X_test.isnull().sum().sum())
#     st.write("y_test missing values:", y_test.isnull().sum())

#     # Train and evaluate model
#     st.write("Training model...")
#     model = train_model(X_train, y_train)
#     st.write("Evaluating model...")
#     mse, predictions = evaluate_model(model, X_test, y_test)

#     # Display results
#     st.write(f"Mean Squared Error: {mse:.2f}")
#     plot_results(y_test.values, predictions)

# # Entry point
# if __name__ == "__main__":
#     main()
