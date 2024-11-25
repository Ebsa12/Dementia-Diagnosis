from tkinter import *
import pandas as pd
import subprocess
from HelpScreen import open_help_window

def validate_float(P):
    if P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False

def launchResults():
    subprocess.Popen(['python3', 'Test_Result.py'])
    root.destroy()
    
def process_prediction():
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
    df.to_csv('AppData.csv', index=False)
    print('data added to dataframe')
    launchResults()

root = Tk()
root.geometry("700x500")

vcmd = (root.register(validate_float), '%P')


titleText = StringVar()
titleText.set("Dementia Diagnosis Prediction")
titleTextLabel = Label(textvariable=titleText, fg="white", font=("Arial", 20, "bold"))
titleTextLabel.grid(row=0, column=1)


genderText = StringVar()
genderText.set("Gender")
genderTextLabel = Label(textvariable=genderText, fg="lightgreen", font=("Arial", 12))
genderTextLabel.grid(row=1, column=0)

genderOptions = StringVar()
gender = OptionMenu(root, genderOptions, 'Male', 'Female')
genderOptions.set("select")
gender.grid(row=2, column=0, padx=5, pady=5)


ethnicityText = StringVar()
ethnicityText.set("Ethnicity")
ethnicityTextLabel = Label(textvariable=ethnicityText, fg="lightgreen", font=("Arial", 12))
ethnicityTextLabel.grid(row=1, column= 1)

ethnicityOptions = StringVar()
ethnicity = OptionMenu(root, ethnicityOptions, 'White', 'African American', 'Asian', 'Other')
ethnicityOptions.set("select")
ethnicity.grid(row=2, column=1, padx=5, pady=5)


smokingText = StringVar()
smokingText.set("History of Smoking")
smokingTextLabel = Label(textvariable=smokingText, fg="lightgreen", font=("Arial", 12))
smokingTextLabel.grid(row=1, column= 2)

smokingOptions = StringVar()
smoking = OptionMenu(root, smokingOptions, 'No', 'Yes')
smokingOptions.set("select")
smoking.grid(row=2, column=2, padx=5, pady=5)


historyText = StringVar()
historyText.set("Family History")
historyTextLabel = Label(textvariable=historyText, fg="lightgreen", font=("Arial", 12))
historyTextLabel.grid(row=3, column= 0)

historyOptions = StringVar()
history = OptionMenu(root, historyOptions, 'No', 'Yes')
historyOptions.set("select")
history.grid(row=4, column=0, padx=5, pady=5)


diabetesText = StringVar()
diabetesText.set("Diabetic")
diabetesTextLabel = Label(textvariable=diabetesText, fg="lightgreen", font=("Arial", 12))
diabetesTextLabel.grid(row=3, column= 1)

diabetesOptions = StringVar()
diabetes = OptionMenu(root, diabetesOptions, 'No', 'Yes')
diabetesOptions.set("select")
diabetes.grid(row=4, column=1, padx=5, pady=5)


memoryText = StringVar()
memoryText.set("Memory Issues")
memoryTextLabel = Label(textvariable=memoryText, fg="lightgreen", font=("Arial", 12))
memoryTextLabel.grid(row=3, column= 2)

memoryOptions = StringVar()
memory = OptionMenu(root, memoryOptions, 'No', 'Yes')
memoryOptions.set("select")
memory.grid(row=4, column=2, padx=5, pady=5)


hiText = StringVar()
hiText.set("Head Injury(s)")
hiTextLabel = Label(textvariable=hiText, fg="lightgreen", font=("Arial", 12))
hiTextLabel.grid(row=5, column= 0)

headInjuryOptions = StringVar()
headInjury = OptionMenu(root, headInjuryOptions, 'No', 'Yes')
headInjuryOptions.set("select")
headInjury.grid(row=6, column=0, padx=5, pady=5)


forgetfulText = StringVar()
forgetfulText.set("Forgetful")
forgetfulTextLabel = Label(textvariable=forgetfulText, fg="lightgreen", font=("Arial", 12))
forgetfulTextLabel.grid(row=5, column= 1)

forgetfulnessOptions = StringVar()
forgetfulness = OptionMenu(root, forgetfulnessOptions, 'No', 'Yes')
forgetfulnessOptions.set("select")
forgetfulness.grid(row=6, column=1, padx=5, pady=5)


behaveText = StringVar()
behaveText.set("Behavior Problems")
behaveTextLabel = Label(textvariable=behaveText, fg="lightgreen", font=("Arial", 12))
behaveTextLabel.grid(row=5, column=2)

behaviorOptions = StringVar()
behavioralProblems = OptionMenu(root, behaviorOptions, 'No', 'Yes')
behaviorOptions.set("select")
behavioralProblems.grid(row=6, column=2, padx=5, pady=5)


adlLabelText = StringVar()
adlLabelText.set("ADL Score")
adlLabel = Label(textvariable=adlLabelText, font=("Arial", 12), fg="lightgreen")
adlLabel.grid(row=7, column=0)

adlText = Entry(root, validate='key', validatecommand=vcmd)
adlText.grid(row=8, column=0, padx=5, pady=5)


mmseLabelText = StringVar()
mmseLabelText.set("MMSE Score")
mmseLabel = Label(textvariable=mmseLabelText, font=("Arial", 12), fg="lightgreen")
mmseLabel.grid(row=7, column=1)

mmseText = Entry(root, validate='key', validatecommand=vcmd)
mmseText.grid(row=8, column=1)


faLabelText = StringVar()
faLabelText.set("Functional Assessment Score")
faLabel = Label(textvariable=faLabelText, font=("Arial", 12), fg="lightgreen")
faLabel.grid(row=7, column=2)

functionalAssessmentText = Entry(root, validate='key', validatecommand=vcmd)
functionalAssessmentText.grid(row=8, column=2)

submissionButton = Button(root, text="Process Prediction", command=process_prediction, bg="green", activebackground="white")
submissionButton.grid(row=9, column=1)

helpButton = Button(root, text="Help", command=open_help_window)
helpButton.grid(row=11, column=2)

root.mainloop()

