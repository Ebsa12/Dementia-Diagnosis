import tkinter as tk
import tkinter.scrolledtext as scrolledtext

def open_help_window():
    new_window = tk.Toplevel()
    new_window.geometry("700x400")
    new_window.title("Help")

    def open_help():
        file_path = "./HelpDoc.txt"
        with open(file_path, "r") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file.read())

    text_area = scrolledtext.ScrolledText(new_window, height=22)
    text_area.pack()

    to_main_button = tk.Button(new_window, text="Back", command=new_window.destroy)
    to_main_button.pack(side='bottom')

    open_help()