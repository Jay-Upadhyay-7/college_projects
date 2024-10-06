import tkinter as tk
import os

def run_traffic_detection():
    os.system("python traffic_detection.py")

def run_agent_learning():
    os.system("python demo.py")

root = tk.Tk()
root.title("Algorithmic Analysis and Development of Features for Human Autonomous Vehicle Coexistence")
root.configure(bg="light blue")  # Set window background color

# Calculate new window size
window_width = 800
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Function to run selected function
def run_selected_function(command):
    if command == "traffic_detection":
        run_traffic_detection()
    elif command == "agent_learning":
        run_agent_learning()

# Configure style for buttons
button_style = {
    "font": ("Helvetica", 12, "bold"),
    "width": 25,
    "height": 3,
    "bg": "green",
    "fg": "black",
    "activebackground": "red",
    "bd": 3,  # border width
    "relief": "raised"  # button relief style
}

# Create buttons
traffic_detection_button = tk.Button(root, text="Traffic Detection", command=lambda: run_selected_function("traffic_detection"), **button_style)
traffic_detection_button.grid(row=1, column=0, pady=10, padx=20)

agent_learning_button = tk.Button(root, text="Agent Learning:NEAT-Based Nvgn.", command=lambda: run_selected_function("agent_learning"), **button_style)
agent_learning_button.grid(row=1, column=1, pady=10, padx=20)

lane_detection_button = tk.Button(root, text="Lane Detection", command=lambda: run_selected_function("traffic_detection"), **button_style)
lane_detection_button.grid(row=2, column=0, pady=10, padx=20)

speed_detection_button = tk.Button(root, text="Speed Detection and Alert System", command=lambda: run_selected_function("agent_learning"), **button_style)
speed_detection_button.grid(row=2, column=1, pady=10, padx=20)

# Centering the grid
for i in range(2):
    root.grid_columnconfigure(i, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

# Create the welcome label
welcome_label = tk.Label(root, text="Welcome! Select Your Choice", font=("Helvetica", 16, "bold"), bg="light blue", fg="black")
welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

# Animation function
def blink():
    current_color = welcome_label.cget("fg")
    next_color = "black" if current_color == "light blue" else "light blue"
    welcome_label.config(fg=next_color)
    root.after(500, blink)

# Start the animation
blink()

root.mainloop()
