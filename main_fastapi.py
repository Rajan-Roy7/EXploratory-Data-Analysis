from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd
import io
from preprocess import DataPreprocessor  # Import your data preprocessing module

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
        return {"filename": file.filename, "data_preview": df.head().to_json()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/process/")
async def process_data(
    file: UploadFile = File(...),
    numerical_cols: Optional[str] = Form(None),
    categorical_cols: Optional[str] = Form(None),
    encoding_type: Optional[str] = Form(None),
    missing_values_strategy: Optional[str] = Form(None),
    missing_categorical_strategy: Optional[str] = Form(None),
    normalization_strategy: Optional[str] = Form(None),
    outlier_n: Optional[int] = Form(None),
    outlier_features: Optional[str] = Form(None)
):
    try:
        # Read the uploaded file into a DataFrame
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        # Create a DataPreprocessor instance
        processor = DataPreprocessor(df)

        # Convert form data from strings to lists as needed
        numerical_cols = numerical_cols.split(',') if numerical_cols else []
        categorical_cols = categorical_cols.split(',') if categorical_cols else []
        outlier_features = outlier_features.split(',') if outlier_features else []

        # Apply various preprocessing steps based on the request
        if numerical_cols and missing_values_strategy:
            processor.handle_missing_values(numerical_cols, missing_values_strategy)
        if categorical_cols and missing_categorical_strategy:
            processor.handle_missing_categorical(categorical_cols, missing_categorical_strategy)
        if categorical_cols and encoding_type:
            processor.encode(categorical_cols, encoding_type)
        if numerical_cols and normalization_strategy:
            processor.normalize(numerical_cols, normalization_strategy)
        if outlier_n is not None and outlier_features:
            processor.detect_outliers(outlier_n, outlier_features)

        # Get the processed data
        processed_data = processor.get_data()
        return JSONResponse(content=processed_data.to_json())

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the Data Preprocessing API!"}
