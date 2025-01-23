from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd

def train_model(data: pd.DataFrame):
    if not {'Temperature', 'Run_Time', 'Downtime_Flag'}.issubset(data.columns):
        raise ValueError("Dataset must contain 'Temperature', 'Run_Time', 'Downtime_Flag' columns.")
    
    X = data[['Temperature', 'Run_Time']]
    y = data['Downtime_Flag']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred, average='weighted')
    }
    return model, metrics

def predict_single(model, input_data):
    input_df = pd.DataFrame([input_data])
    print("Input DataFrame for prediction:", input_df)  
    prediction = model.predict(input_df)[0]
    confidence = max(model.predict_proba(input_df)[0]) 
    return {"Downtime": "Yes" if prediction == 1 else "No", "Confidence": round(confidence, 2)}
