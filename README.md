# Techpranee Assignment

This assignment implements a RESTful API for predictive analysis in manufacturing operations. The API predicts machine downtime based on inputs like temperature and run time using machine learning models. The endpoints allow users to upload a dataset, train the model, and make predictions.

---

## **Features**

- Upload manufacturing data in CSV format.
- Train a machine learning model (Decision Tree or Random Forest).
- Make predictions about machine downtime.
- Returns results in JSON format, including confidence scores.

---

## **Setup Instructions**

### **1. Prerequisites**

Ensure the following are installed on your system:
- Python 3.8+
- pip (Python package manager)
- Git (optional, for cloning the repository)

### **2. Clone the Repository**

If you haven't downloaded the project yet, clone it from the repository:
```bash
git clone <repository_url>
cd <repository_folder>
```

Or, download and extract the project zip file.

### **3. Create a Virtual Environment (Optional)**

It is recommended to use a virtual environment to avoid conflicts with other Python packages:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **4. Install Dependencies**

Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **5. Start the Server**

Run the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000` by default.

---

## **API Endpoints**

### **1. Upload Dataset**

**Endpoint**: `POST /upload`

**Description**: Upload a CSV file containing manufacturing data.

**Request**:
- **Headers**: `Content-Type: multipart/form-data`
- **Body**: Upload the CSV file with key as `file`.

---

### **2. Train Model**

**Endpoint**: `POST /train`

**Description**: Train a machine learning model on the uploaded dataset.

**Request**:
- No body required.

---

### **3. Make Predictions**

**Endpoint**: `POST /predict`

**Description**: Predict machine downtime based on input values.

**Request**:
- **Headers**: `Content-Type: application/json`
- **Body** (example):
  ```json
  {
      "Temperature": 85,
      "Run_Time": 120
  }
  ```

---

## **Testing the API**

### **Using Postman**

1. Open Postman and create a new request.
2. Use the following details for testing:

#### Upload Dataset:
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/upload`
- **Body**: Select "form-data" and upload your CSV file with key as `file`.

#### Train Model:
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/train`

#### Predict Downtime:
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/predict`
- **Body**: Select "raw", choose `JSON`, and enter:
  ```json
  {
      "Temperature": 85,
      "Run_Time": 120
  }
  ```

### **Using cURL**

#### Upload Dataset:
```bash
curl -X POST "http://127.0.0.1:8000/upload" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@your_dataset.csv"
```

#### Train Model:
```bash
curl -X POST "http://127.0.0.1:8000/train"
```

#### Predict Downtime:
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"Temperature": 85, "Run_Time": 120}'
```

---

## **Future Enhancements**

- Add bulk prediction support.
- Save prediction results to a file or database.
- Integrate authentication for API endpoints.

---

## **Contact**
For questions or support, please contact [rajshreeprajapati124@gmail.com].


