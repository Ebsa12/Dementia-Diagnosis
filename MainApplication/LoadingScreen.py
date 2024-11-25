from tkinter import *
from tkinter import messagebox
import subprocess
from APIConnection import PosDiagnosis  # Ensure this returns a valid numeric value

# Debugging: Print the original value of PosDiagnosis
print(f"Original PosDiagnosis value: {PosDiagnosis}")

# Force PosDiagnosis to an integer to ensure no decimals
try:
    PosDiagnosis = int(float(PosDiagnosis))  # Handles both string and float inputs
except ValueError:
    # Handle the case where PosDiagnosis is invalid
    print("Error: PosDiagnosis is not a valid number.")
    PosDiagnosis = 0  # Default to 0 if invalid

# Debugging: Print the converted value of PosDiagnosis
print(f"Converted PosDiagnosis value: {PosDiagnosis}")

# Function to close the application and redirect to home
def go_home():
    messagebox.showinfo("Home", "Returning to the Home Page.")
    subprocess.Popen(['python3', 'LoadingScreen.py'])
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

# Create and pack the "Home" button
home_button = Button(root, text="Home", font=("Arial", 12), fg="#4CAF50", command=go_home)
home_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
