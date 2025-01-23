from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
from model import train_model, predict_single
from pydantic import BaseModel


app = FastAPI()


model = None  
data = None   

# Input model for prediction
class PredictInput(BaseModel):
    Temperature: float
    Run_Time: float


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to the Manufacturing Predictive API!",
        "endpoints": [
            {"method": "POST", "path": "/upload", "description": "Upload manufacturing data (CSV)."},
            {"method": "POST", "path": "/train", "description": "Train the predictive model."},
            {"method": "POST", "path": "/predict", "description": "Predict machine downtime."}
        ]
    }



@app.post("/upload")
async def upload_data(file: UploadFile = File(...)):
    global data
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")
    
    
    data = pd.read_csv(file.file)
    print("Uploaded dataset columns:", data.columns)  
    return {"message": "File uploaded successfully!", "columns": list(data.columns)}


# Train model endpoint
@app.post("/train")
def train():
    global data, model  
    if data is None:
        raise HTTPException(status_code=400, detail="No dataset uploaded.")
    
    # Train the model using the dataset
    model, metrics = train_model(data)
    print("Model trained successfully with metrics:", metrics)  
    return {"message": "Model trained successfully!", "metrics": metrics}


# Predict endpoint
@app.post("/predict")
def predict(input_data: PredictInput):
    global model 
    if model is None:
        print("Model is None at /predict endpoint")  
        raise HTTPException(status_code=400, detail="Model is not trained yet.")
    
    # Log input data for debugging
    print("Prediction input received:", input_data.dict()) 
    prediction = predict_single(model, input_data.dict())
    print("Prediction result:", prediction)
    return prediction
