from tkinter import *
from tkinter import messagebox
from APIConnection import PosDiagnosis
import APIConnection


# Function to simulate running the model again
def run_model_again():
    messagebox.showinfo("Run Model", "Model is running again!")

# Create the the result application window
root = Tk()
root.title("Results Page")

# Set the window size
root.geometry("700x400")
root.resizable(False, False)

# Create and pack the main title label
titleText = StringVar()
titleText.set(f"You have a {PosDiagnosis}% change of contracting Dementia")
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

# Create and pack the "Run Model Again" button
run_button = Button(root, text="Run Model Again", font=("Arial", 12), fg="#4CAF50", command=run_model_again)
run_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
