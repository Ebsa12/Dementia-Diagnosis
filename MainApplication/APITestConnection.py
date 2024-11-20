#Test API Connection
import pandas as pd
import requests

#requestURL
url = "https://api.akkio.com/api"
project_key = 'a1accea5-c654-48b9-9e8b-580886cdb772/1'
api_key = 'b91100c5-a3a6-404c-a92c-ec10a1fc6938'
data = '''
    [{
        "Gender":"1",
        "FunctionalAssessment":"6",
        "FamilyHistoryAlzheimers":"0",
        "MMSE":"27.4",
        "BehavioralProblems":"1",
        "Ethnicity":"0",
        "Diabetes":"1",
        "ADL":"10",
        "Smoking":"0",
        "HeadInjury":"0",
        "MemoryComplaints":"1",
        "Forgetfulness":"0"
      }]
'''
  
deploy_transforms_only = 'false'

params = {
    'project_key': project_key,
    'api_key': api_key,
    'data': data,
    'deploy-transforms-only': deploy_transforms_only
}
response = requests.get(url, params=params)

# Print the response from the server
print(response.text)

