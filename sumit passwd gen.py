import tkinter as tk
import random
import string

def generate_password(length, complexity):
    if complexity == 'Letters':
        characters = string.ascii_letters
    elif complexity == 'Letters and Numbers':
        characters = string.ascii_letters + string.digits
    elif complexity == 'Letters, Numbers, and Symbols':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(entry_length.get())
        complexity = complexity_var.get()
        password = generate_password(length, complexity)
        password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        password_label.config(text="Invalid length. Please enter a valid number.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label_length = tk.Label(frame, text="Enter password length:")
label_length.grid(row=0, column=0, pady=5)

entry_length = tk.Entry(frame)
entry_length.grid(row=0, column=1, pady=5)

label_complexity = tk.Label(frame, text="Select complexity:")
label_complexity.grid(row=1, column=0, pady=5)

complexity_options = ['Letters', 'Letters and Numbers', 'Letters, Numbers, and Symbols']
complexity_var = tk.StringVar()
complexity_var.set(complexity_options[0])  # Default complexity
complexity_menu = tk.OptionMenu(frame, complexity_var, *complexity_options)
complexity_menu.grid(row=1, column=1, pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

password_label = tk.Label(frame, text="Generated Password: ")
password_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
