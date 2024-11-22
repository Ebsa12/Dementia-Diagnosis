# Import module 
import tkinter as tk
import tkinter.scrolledtext as scrolledtext

# Create object 
root = tk.Tk() 

# Root window appearance options
root.geometry( "700x400" ) 
root.title("Help")

# Function to open help document
def open_help():
    file_path = "./HelpDoc.txt"
    with open(file_path, "r") as file:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, file.read())
        
# Function for back button
def main_menu_button():
    pass

# Create area to display text from file
text_area = scrolledtext.ScrolledText(root, height=22)
text_area.pack()

# Add back button 
to_main_button = tk.Button(root, text = "Back")
to_main_button.pack(side='bottom')

# Create Label 
label = tk.Label( root , text = " " ) 
label.pack() 

open_help()
# Execute tkinter 
root.mainloop() 