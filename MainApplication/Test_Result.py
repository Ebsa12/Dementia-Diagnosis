from tkinter import *
from tkinter import messagebox
from APIConnection import PosDiagnosis
import subprocess
import APIConnection


# Function to close the application
def close_application():
    messagebox.showinfo("Close Application", "The application will now close.")
    root.destroy()


# Create the result application window
root = Tk()
root.title("Results Page")

# Set the window size
root.geometry("700x400")
root.resizable(False, False)

# Determine the risk level message based on PosDiagnosis
if PosDiagnosis >= 75:
    risk_message = f"You are at a high risk ({PosDiagnosis}%) of contracting Dementia."
elif 50 <= PosDiagnosis < 75:
    risk_message = f"You are at a moderate risk ({PosDiagnosis}%) of contracting Dementia."
elif 25 <= PosDiagnosis < 50:
    risk_message = f"You have a small risk ({PosDiagnosis}%) of contracting Dementia."
else:
    risk_message = f"You have little to no risk ({PosDiagnosis}%) of contracting Dementia."

# Create and pack the main title label
titleText = StringVar()
titleText.set(risk_message)
title_label = Label(root, textvariable=titleText, font=("Arial", 16), fg="lightgreen")
title_label.pack(pady=20)

# Create and pack the disclaimer label
disclaimer_label = Label(
    root,
    text=(
        "Disclaimer: This is not a diagnosis of Dementia.\n"
        "While the application has indicated you may be at\n"
        "risk of Dementia, do not seek any form of treatment\n"
        "until consulting a doctor or medical professional."
    ),
    font=("Arial", 10),
    fg="#666",
    justify="center",
)
disclaimer_label.pack(pady=10)

# Create and pack the "Close Application" button
close_button = Button(root, text="Close Application", font=("Arial", 12), fg="#4CAF50", command=close_application)
close_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
