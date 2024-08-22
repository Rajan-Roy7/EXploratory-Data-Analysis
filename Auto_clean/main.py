# main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd
import autoclean as ac  # Import the data cleaning module

app = FastAPI()

@app.post("/process-clean/")
async def process_clean(file: UploadFile = File(...)):
    if file.filename.endswith('.csv'):
        # Read the uploaded CSV file into a DataFrame
        df = pd.read_csv(file.file)

        # Use the read_data function from the autoclean module to clean the DataFrame
        try:
            cleaned_df = ac.read_data(df)
            
            # Convert the cleaned DataFrame back to CSV format to return as a response
            cleaned_csv = cleaned_df.to_csv(index=False)
            
            return JSONResponse(content={"status": "success", "cleaned_data": cleaned_csv})
        except Exception as e:
            return JSONResponse(content={"status": "error", "message": str(e)}, status_code=400)
    else:
        return JSONResponse(content={"status": "error", "message": "Only CSV files are supported"}, status_code=400)
