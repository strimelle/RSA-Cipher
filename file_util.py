from tkinter import filedialog, END


def open_file(message):
    filepath = filedialog.askopenfilename(filetypes=[("Text File", "*.txt")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            file_msg = file.read()
        message.delete(0, END)
        message.insert(0, file_msg)


def save_file(outputWindow):
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
    if filepath:
        file = open(filepath, "w", encoding="utf-8")
        file.write(outputWindow.get("1.0", END).strip())
        file.close()