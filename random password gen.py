import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length should be greater than zero.")
        
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))

# main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")
root.configure(bg='pink')  

#colors
frame_bg_color = "pink"  
label_color = "black"  
entry_bg_color = "#ffffff" 
button_bg_color = "#4caf50"  
button_fg_color = "#ffffff" 

# Create a frame to center all widgets
frame = tk.Frame(root, bg=frame_bg_color)
frame.pack(expand=True)

# Create and place the widgets inside the frame
label_length = tk.Label(frame, text="Enter Length:", bg=frame_bg_color, fg=label_color, font=('Arial', 15))
label_length.pack(pady=5)

entry_length = tk.Entry(frame, width=10, bg=entry_bg_color, font=('Arial', 15))
entry_length.pack(pady=5)

button_generate = tk.Button(frame, text="Generate Password", command=generate_password, 
                            bg=button_bg_color, fg=button_fg_color, font=('Arial', 15))
button_generate.pack(pady=10)

label_password = tk.Label(frame, text="Your Random password is:", bg=frame_bg_color, fg=label_color, font=('Arial', 15))
label_password.pack(pady=5)

entry_password = tk.Entry(frame, width=50, bg=entry_bg_color, font=('Arial', 15))
entry_password.pack(pady=5)
root.mainloop()
