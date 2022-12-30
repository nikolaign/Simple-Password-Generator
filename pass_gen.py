import random
import string
import pyperclip
import tkinter as tk

def generate_password():
    # Generate a random password that includes uppercase letters, lowercase letters, and digits and special characters
    # and has a length between 8 and 12 characters
    password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=random.randint(8, 12)))
    password_label.config(text=password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create a label to display the generated password
password_label = tk.Label(master=window, text="")
password_label.pack()

# Create a button to generate a new password
generate_button = tk.Button(master=window, text="Generate", command=generate_password)
generate_button.pack()


# Function to be called when the "Copy" button is clicked
def copy_button_clicked(): 
  # Copy the text of the Label widget to the clipboard 
  pyperclip.copy(password_label["text"])

# Create a button to copy generated password
copy_button = tk.Button(text="Copy", command=copy_button_clicked)
copy_button.pack()

# Run the main loop
window.mainloop()