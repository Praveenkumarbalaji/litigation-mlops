import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = joblib.load('model.pkl')

# Initialize LabelEncoder for categorical features
label_encoder = LabelEncoder()

app = FastAPI()

# Define the input data structure
class CaseData(BaseModel):
    case_number: str
    plaintiff: str
    defendant: str

@app.post("/predict")
def predict(case: CaseData):
    try:
        # Transform categorical data using LabelEncoder
        plaintiff_encoded = label_encoder.fit_transform([case.plaintiff])
        defendant_encoded = label_encoder.fit_transform([case.defendant])

        # Prepare features for prediction
        features = [case.case_number, plaintiff_encoded[0], defendant_encoded[0]]

        # Use the model for prediction
        prediction = model.predict([features])

        # Convert numeric prediction (0, 1) to "win" and "loss"
        result = "win" if prediction[0] == 1 else "loss"
        
        return {"prediction": result}

    except Exception as e:
        return {"error": str(e)}

# Define the root endpoint (optional)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Litigation MLOps API!"}
