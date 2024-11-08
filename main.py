import tkinter as tk
from tkinter import *
import datetime
import Speak
import Neuronix
import time



# Create the main window
root = tk.Tk()
root.title("Neuronix")
root.geometry("1180x850")
img=PhotoImage(file='.\\images\\ai.png')
root.iconphoto(False,img)

now = datetime.datetime.now()
today = datetime.date.today()


formatted_time = now.strftime("%H:%M:%S")


def on_button_click():
    
    time.sleep(1) 
    Speak.wishMe()
    while True:
        Neuronix.Main()
    
def close():
    root.destroy()
    


# Create a top frame
top_frame = tk.Frame(root, bg="blue", width=400, height=100)
top_frame.pack(fill="x", padx=0, pady=0)

# Add a label to the top frame
top_label = tk.Label(top_frame, text="Neuronix",fg='#FFD700', font=('Helvetica', 20, 'bold'),bg="blue")
top_label.pack(pady=50)

# Create a middle frame
middle_frame = tk.Frame(root, bg="black", width=400, height=100)
middle_frame.pack(fill="x", padx=10, pady=5)

text_area = tk.Text(middle_frame, wrap='word',fg='green', height=10, width=50,bg='black',font=('Helvetica', 14),bd=0, highlightthickness=0)
text_area.grid(row=0, column=0,pady=20, padx=20)
text_area.insert('1.0', f"Time : {formatted_time}")
text_area.insert('1.0', f"Date : {today}\n")


text_area2 = tk.Text(middle_frame, wrap='word',fg='green', height=25, width=40,bg='black',font=('Helvetica', 12), bd=0, highlightthickness=0)
text_area2.grid(row=0, column=2,pady=20, padx=20)
text_area2.insert('1.0', "Welcome to the system.\n\n")
text_area2.insert('3.0',"\nNeuronix is live now.....\n\n")
text_area2.insert('5.0', "\nNeuronix is an AI-powered, voice-activated assistant designed to streamline daily tasks and provide quick access to information.\n")










# Create a bottom frame
bottom_frame = tk.Frame(root, bg="blue", width=400, height=100)
bottom_frame.pack(fill="x", padx=0, pady=0)

# Add an entry widget to the bottom frame
button1 = tk.Button(bottom_frame, text="Start",command=on_button_click, font=('Helvetica', 14, 'bold'),bg='green')
button2 = tk.Button(bottom_frame, text="Stop",command=close, font=('Helvetica', 14, 'bold'),bg='red')
button1.grid(row=0, column=0, padx=20, pady=20)
button2.grid(row=0, column=1, padx=700, pady=20)

root.config(bg='black')

# Start the Tkinter event loop
root.mainloop()
