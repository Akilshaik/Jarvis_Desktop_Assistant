import tkinter as tk
from tkinter import ttk ,Text
from PIL import Image, ImageTk
import Speak
import jarvis
import Listen
from Listen import Listen,yousaid

#import jarvis 

#mian=jarvis.Main()


root= tk.Tk()
root.title("Jarvis")
root.geometry("1080x720")
def create_text_at_position(canvas, x, y, text, color, anchor):
    canvas.create_text(x, y, text=text, font=('Helvetica', 16), fill=color, anchor=anchor)




image = Image.open("E:\projects\Jarvis A.l\images\jarvisDashboard.jpeg")
tk_image = ImageTk.PhotoImage(image)
label = tk.Label(root, image=tk_image)
label.place(x=0, y=0, relwidth=1, relheight=1)


def on_button_click():
    print("Button clicked!")
    
    Speak.wishMe()
    while True:
        #jarvis.Main()
        print(yousaid)
        

def close():
    root.destroy()

    



button1 = tk.Button(root, text="Start", command=on_button_click,font=('Helvetica', 14, 'bold'),bg='blue')
button2 = tk.Button(root, text="Stop", command=close, font=('Helvetica', 14, 'bold'),bg='red')

button1.grid(row=0, column=0, padx=20, pady=20)
button2.grid(row=0, column=1, padx=20, pady=20)







def create_transparent_text_area(root, width, height, x, y):
    # Create a Canvas with a transparent-like background
    canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0)
    canvas.place(x=x, y=y)
    
    # Create a Text widget
    text_widget = Text(canvas,wrap='word', bg='black', fg='green', insertbackground='green', font=('Helvetica', 14))
    text_widget.place(x=0, y=0, width=width, height=height)
    
    
    

    return text_widget

text_area = create_transparent_text_area(root, width=500, height=200, x=300, y=300)








root.mainloop() 