import pandas as pd
import requests

Appdata = pd.read_csv('AppData.csv')

# print(Appdata)

#Change Gender Value
Appdata.loc[Appdata['Gender'] == 'Female', 'Gender'] = '1'
Appdata.loc[Appdata['Gender'] == 'Male', 'Gender'] = '0'

# Change Ethnicity Value
Appdata.loc[Appdata['Ethnicity'] == 'White', 'Ethnicity'] = '0'
Appdata.loc[Appdata['Ethnicity'] == 'African American', 'Ethnicity'] = '1'
Appdata.loc[Appdata['Ethnicity'] == 'Asian', 'Ethnicity'] = '2'
Appdata.loc[Appdata['Ethnicity'] == 'Other', 'Ethnicity'] = '3'

# Change Smoking Value
Appdata.loc[Appdata['Smoking'] == 'No', 'Smoking'] = '0'
Appdata.loc[Appdata['Smoking'] == 'Yes', 'Smoking'] = '1'

# Change FamilyHistoryAlzheimers Value
Appdata.loc[Appdata['FamilyHistoryAlzheimers'] == 'No', 'FamilyHistoryAlzheimers'] = '0'
Appdata.loc[Appdata['FamilyHistoryAlzheimers'] == 'Yes', 'FamilyHistoryAlzheimers'] = '1'

# Change Diabetes Value
Appdata.loc[Appdata['Diabetes'] == 'No', 'Diabetes'] = '0'
Appdata.loc[Appdata['Diabetes'] == 'Yes', 'Diabetes'] = '1'

# Change MemoryComplaints Value
Appdata.loc[Appdata['MemoryComplaints'] == 'No', 'MemoryComplaints'] = '0'
Appdata.loc[Appdata['MemoryComplaints'] == 'Yes', 'MemoryComplaints'] = '1'

# Change HeadInjury Value
Appdata.loc[Appdata['HeadInjury'] == 'No', 'HeadInjury'] = '0'
Appdata.loc[Appdata['HeadInjury'] == 'Yes', 'HeadInjury'] = '1'

# Change Forgetfulness Value
Appdata.loc[Appdata['Forgetfulness'] == 'No', 'Forgetfulness'] = '0'
Appdata.loc[Appdata['Forgetfulness'] == 'Yes', 'Forgetfulness'] = '1'

# Change BehavioralProblems Value
Appdata.loc[Appdata['BehavioralProblems'] == 'No', 'BehavioralProblems'] = '0'
Appdata.loc[Appdata['BehavioralProblems'] == 'Yes', 'BehavioralProblems'] = '1'

# Last row of csv
newData = Appdata.tail(1)

print(newData)

# Define Variables
gender = str(newData.reset_index().loc[0,'Gender'])
functionalAssessment = str(newData.reset_index().loc[0,'FunctionalAssessment'])
familyHistoryAlzheimers =str(newData.reset_index().loc[0,'FamilyHistoryAlzheimers'])
mmse = str(newData.reset_index().loc[0,'MMSE'])
behavioralProblems = str(newData.reset_index().loc[0,'BehavioralProblems'])
ethnicity = str(newData.reset_index().loc[0,'Ethnicity'])
diabetes  = str(newData.reset_index().loc[0,'Diabetes'])
adl = str(newData.reset_index().loc[0,'ADL'])
smoking = str(newData.reset_index().loc[0,'Smoking'])
headInjury = str(newData.reset_index().loc[0,'HeadInjury'])
memoryComplaints = str(newData.reset_index().loc[0,'MemoryComplaints'])
forgetfulness = str(newData.reset_index().loc[0,'Forgetfulness'])

# print(gender, functionalAssessment, familyHistoryAlzheimers, mmse, behavioralProblems, adl, ethnicity, diabetes, smoking, headInjury, memoryComplaints, forgetfulness)

#requestURL
url = "https://api.akkio.com/api"
project_key = 'a1accea5-c654-48b9-9e8b-580886cdb772/1'
api_key = 'b91100c5-a3a6-404c-a92c-ec10a1fc6938'
data = f'''
    [{{
        "Gender":"{gender}",
        "FunctionalAssessment":"{functionalAssessment}",
        "FamilyHistoryAlzheimers":"{familyHistoryAlzheimers}",
        "MMSE":"{mmse}",
        "BehavioralProblems":"{behavioralProblems}",
        "Ethnicity":"{ethnicity}",
        "Diabetes":"{diabetes}",
        "ADL":"{adl}",
        "Smoking":"{smoking}",
        "HeadInjury":"{headInjury}",
        "MemoryComplaints":"{memoryComplaints}",
        "Forgetfulness":"{forgetfulness}"
    }}]
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
print(response.json()[0]['Probability Diagnosis is Yes'])
















































# # Import module 
# from tkinter import *

# # Create object 
# root = Tk() 

# # Adjust size 
# root.geometry( "200x200" ) 

# # Change the label text 
# def show(): 
# 	label.config( text = clicked.get() ) 

# # Dropdown menu options 
# options = [ 
# 	"Monday", 
# 	"Tuesday", 
# 	"Wednesday", 
# 	"Thursday", 
# 	"Friday", 
# 	"Saturday", 
# 	"Sunday"
# ] 

# # datatype of menu text 
# clicked = StringVar() 

# # initial menu text 
# clicked.set( "Monday" ) 

# # Create Dropdown menu 
# drop = OptionMenu( root , clicked , *options ) 
# drop.pack() 

# # Create button, it will change label text 
# button = Button( root , text = "click Me" , command = show ).pack() 

# # Create Label 
# label = Label( root , text = " " ) 
# label.pack() 

# # Execute tkinter 
# root.mainloop() 
