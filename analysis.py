from django.conf import Settings
import pandas as pd
from ydata_profiling import ProfileReport
import json

def generate_profile_json(df, title="Profiling Report", minimal=False):
    
    # Generate the profile report
    # config = Settings()
    # config.html.style.logo = ""
    # config.missing_diagrams = {"heatmap": False}
    profile = ProfileReport(df, title=title, minimal=minimal,explorative=False)
    
    # Convert the report to JSON
    json_data = profile.to_json()
    
    # If an output file is specified, save the JSON to that file
    return json_data

# Example usage:
import pandas as pd

# Load your data
df = pd.read_csv('salary_account.csv')

# Generate the profile report JSON
json_report = generate_profile_json(df, 
                                    title="My Dataset Profile", 
                                    minimal=False
                        )

# If you want to print the JSON to console
with open('output.txt', 'w') as f:     print(json_report, file=f)  
# print(json_report)