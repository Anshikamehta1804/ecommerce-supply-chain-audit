# ==============================================================================
# E-Commerce Shipment Delivery Performance Analysis & Prediction Pipeline
# Dataset: E-Commerce Shipping Data (Kaggle)
# ==============================================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

def load_and_preprocess_data(filepath):
    """Loads the dataset, handles cleaning, and encodes categorical features."""
    print("Loading dataset from:", filepath)
    df = pd.read_csv(filepath)
    
    print(f"Initial dataset shape: {df.shape}")
    
    # Basic data cleaning / summary
    print("Missing values per column:\n", df.isnull().sum())
    
    # Encoding categorical variables
    categorical_cols = ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']
    label_encoders = {}
    
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
        
    return df, label_encoders

def perform_eda(df):
    """Performs exploratory data analysis and prints key supply chain metrics."""
    print("\n--- Exploratory Data Analysis ---")
    
    # Overall On-Time Delivery Rate
    otd_rate = (df['Reached.on.Time_Y.N'].mean()) * 100
    print(f"Overall On-Time Delivery Rate: {otd_rate:.2f}%")
    
    # OTD Rate by Shipping Mode
    print("\nOn-Time Delivery Rate by Shipping Mode:")
    mode_otd = df.groupby('Mode_of_Shipment')['Reached.on.Time_Y.N'].mean() * 100
    print(mode_otd)
    
    # Average Cost and Discount by On-Time Status
    print("\nAverage Product Cost & Discount by Delivery Status:")
    summary_stats = df.groupby('Reached.on.Time_Y.N')[['Cost_of_the_Product', 'Discount_offered', 'Weight_in_gms']].mean()
    print(summary_stats)

def train_predictive_model(df):
    """Trains a Random Forest classifier to predict whether a shipment will be on time."""
    print("\n--- Training Machine Learning Model ---")
    
    X = df.drop(columns=['ID', 'Reached.on.Time_Y.N'])
    y = df['Reached.on.Time_Y.N']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    
    print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Feature Importance
    importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    print("\nFeature Importances:")
    print(importances)
    
    return model

if __name__ == "__main__":
    file_path = "Train.csv"
    df, encoders = load_and_preprocess_data(file_path)
    perform_eda(df)
    model = train_predictive_model(df)
    print("\nPipeline execution complete!")
