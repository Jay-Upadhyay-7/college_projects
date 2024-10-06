import tkinter as tk
import os

def run_traffic_detection():
    os.system("python traffic_detection.py")

def run_agent_learning():
    os.system("python demo.py")

root = tk.Tk()
root.title("Algorithmic Analysis and Development of Features for Human Autonoumus Vehicle Coexistence")
root.configure(bg="light blue")  # Set window background color

# Calculate new window size
window_width = 800
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Function to run selected function
def run_selected_function(command):
    if command == "traffic_detection":
        run_traffic_detection()
    elif command == "agent_learning":  # Modified function name
        run_agent_learning()  # Modified function name

# Configure style for buttons
button_style = {
    "font": ("Helvetica", 16, "bold"),
    "width": 20,
    "height": 3,
    "bg": "green",
    "fg": "black",
    "activebackground": "red",
    "bd": 3,  # border width
    "relief": "raised"  # button relief style
}

# Create buttons
traffic_detection_button = tk.Button(root, text="Traffic Detection", command=lambda: run_selected_function("traffic_detection"), **button_style)
traffic_detection_button.grid(row=0, column=0, pady=(window_height // 3) - 30, padx=(window_width // 8))

agent_learning_button = tk.Button(root, text="Agent Learning", command=lambda: run_selected_function("agent_learning"), **button_style)  # Modified button text
agent_learning_button.grid(row=0, column=1, pady=(window_height // 3) - 30, padx=(window_width // 8))  # Modified grid position


root.mainloop()
