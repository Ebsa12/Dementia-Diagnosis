from tkinter import *
import pandas as pd



def validate_float(P):
    if P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False
    
def process_prediction():
    AppData = pd.read_csv('AppData.csv')
    data = {
        'Gender': [genderOptions.get()],
        'Ethnicity': [ethnicityOptions.get()],
        'Smoking': [smokingOptions.get()],
        'FamilyHistoryAlzheimers': [historyOptions.get()],
        'Diabetes': [diabetesOptions.get()],
        'MemoryComplaints': [memoryOptions.get()],
        'HeadInjury': [headInjuryOptions.get()],
        'Forgetfulness': [forgetfulnessOptions.get()],
        'BehavioralProblems': [behaviorOptions.get()],
        'ADL': [adlText.get()],
        'MMSE': [mmseText.get()],
        'FunctionalAssessment': [functionalAssessmentText.get()]
    }
    df = pd.DataFrame(data)
    AppData = pd.concat([AppData, df])
    AppData.to_csv('AppData.csv', index=False)
    print(AppData.tail(1))
    

root = Tk()
root.geometry("700x400")



vcmd = (root.register(validate_float), '%P')

# Create and place the OptionMenus and Entry widgets in a 3x4 grid
genderOptions = StringVar()
gender = OptionMenu(root, genderOptions, 'Male', 'Female')
gender.grid(row=0, column=0, padx=5, pady=5)

ethnicityOptions = StringVar()
ethnicity = OptionMenu(root, ethnicityOptions, 'White', 'African American', 'Asian', 'Other')
ethnicity.grid(row=0, column=1, padx=5, pady=5)

smokingOptions = StringVar()
smoking = OptionMenu(root, smokingOptions, 'No', 'Yes')
smoking.grid(row=0, column=2, padx=5, pady=5)

historyOptions = StringVar()
history = OptionMenu(root, historyOptions, 'No', 'Yes')
history.grid(row=1, column=0, padx=5, pady=5)

diabetesOptions = StringVar()
diabetes = OptionMenu(root, diabetesOptions, 'No', 'Yes')
diabetes.grid(row=1, column=1, padx=5, pady=5)

memoryOptions = StringVar()
memory = OptionMenu(root, memoryOptions, 'No', 'Yes')
memory.grid(row=1, column=2, padx=5, pady=5)

headInjuryOptions = StringVar()
headInjury = OptionMenu(root, headInjuryOptions, 'No', 'Yes')
headInjury.grid(row=2, column=0, padx=5, pady=5)


forgetfulnessOptions = StringVar()
forgetfulness = OptionMenu(root, forgetfulnessOptions, 'No', 'Yes')
forgetfulness.grid(row=2, column=1, padx=5, pady=5)

behaviorOptions = StringVar()
behavioralProblems = OptionMenu(root, behaviorOptions, 'No', 'Yes')
behavioralProblems.grid(row=2, column=2, padx=5, pady=5)

adlText = Entry(root, validate='key', validatecommand=vcmd)
adlText.grid(row=3, column=0)

mmseText = Entry(root, validate='key', validatecommand=vcmd)
mmseText.grid(row=3, column=1)

functionalAssessmentText = Entry(root, validate='key', validatecommand=vcmd)
functionalAssessmentText.grid(row=3, column=2)

submissionButton = Button(root, text="Process Prediction", command=process_prediction)
submissionButton.grid(row=4, column=1)

root.mainloop()

