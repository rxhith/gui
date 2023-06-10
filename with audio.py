from tkinter import *
from PIL import Image, ImageTk
import pyttsx3

root = Tk()
root.geometry("900x600")
root.title("Sliding animation")

txt = "Come Here!!!!"
count = 0
text = ''

# Create a Label widget for displaying the text
text_label = Label(root, text=txt, font=('Arial', 30, "bold"), fg='black')
text_label.pack(pady=100)

# Load the animated GIF
gif_frames = []
gif_image = Image.open("cat-cute (1).gif")
frames = gif_image.n_frames

for i in range(frames):
    gif_image.seek(i)
    frame = ImageTk.PhotoImage(gif_image)
    gif_frames.append(frame)

# Create a Label widget for displaying the GIF
gif_label = Label(root)
gif_label.pack()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the speech rate (speed)
engine.setProperty('rate', 300)  # Adjust the value as per your preference

def update_gif(frame_index):
    frame = gif_frames[frame_index]
    gif_label.config(image=frame)
    root.after(100, update_gif, (frame_index + 1) % frames)

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def slider():
    global count, text
    if count >= len(txt):
        count = -1
        text = ''
        text_label.config(text=text)
    else:
        text = text + txt[count]
        text_label.config(text=text)
        if txt[count] == ' ' or count == len(txt)-1:  # Speak out the word when a space is encountered or at the end of the text
            speak_text(text.strip())
            text = ''
    count = count + 1
    text_label.after(100, slider)

# Start the sliding animation
slider()

# Start the GIF animation
update_gif(0)

root.mainloop()
