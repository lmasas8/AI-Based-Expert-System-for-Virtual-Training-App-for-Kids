import tkinter as tk
from tkinter import messagebox

def get_suggestion():
    try:
        age = int(age_entry.get())
        fitness = fitness_level.get()
        goal = goal_var.get()

        if age < 3:
            suggestion = "Too young for structured workouts. Focus on playful movement."
        elif age <= 5:
            if fitness == "Low":
                suggestion = "Simple stretching and playful movement."
            elif fitness == "Medium":
                suggestion = "Short walks and dancing games."
            else:
                suggestion = "Balance games, light jogging."
        elif age <= 10:
            if fitness == "Low":
                suggestion = "Walking, light stretching."
            elif fitness == "Medium":
                suggestion = "Jumping jacks, cycling."
            else:
                suggestion = "Sports drills, kids yoga."
        else:
            if fitness == "Low":
                suggestion = "Brisk walking, flexibility exercises."
            elif fitness == "Medium":
                suggestion = "Running, circuit games."
            else:
                suggestion = "Structured training routines (with guidance)."

        if goal == "Fun":
            suggestion += "\nFocus on keeping it fun and engaging!"
        elif goal == "Fitness":
            suggestion += "\nAim for daily activity with variety."
        else:
            suggestion += "\nBuild consistency with motivation."

        result_label.config(text="Suggested Activity:\n" + suggestion)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid age.")

# Create GUI
root = tk.Tk()
root.title("Kids Fitness Expert System")
root.geometry("550x500")
root.configure(bg="#F0F8FF")

title = tk.Label(root, text="🏃‍♂️ AI Expert System for Kids' Fitness 🏃‍♀️", font=("Comic Sans MS", 18, "bold"), bg="#F0F8FF", fg="#333")
title.pack(pady=15)

frame = tk.Frame(root, bg="#F0F8FF")
frame.pack()

tk.Label(frame, text="Enter Age of the Child:", font=("Arial", 12), bg="#F0F8FF").pack(pady=3)
age_entry = tk.Entry(frame, font=("Arial", 12), width=20)
age_entry.pack(pady=5)

tk.Label(frame, text="Select Fitness Level:", font=("Arial", 12), bg="#F0F8FF").pack()
fitness_level = tk.StringVar(value="Medium")
tk.Radiobutton(frame, text="Low", variable=fitness_level, value="Low", bg="#F0F8FF", font=("Arial", 11)).pack()
tk.Radiobutton(frame, text="Medium", variable=fitness_level, value="Medium", bg="#F0F8FF", font=("Arial", 11)).pack()
tk.Radiobutton(frame, text="High", variable=fitness_level, value="High", bg="#F0F8FF", font=("Arial", 11)).pack()

tk.Label(frame, text="Select Goal:", font=("Arial", 12), bg="#F0F8FF").pack(pady=3)
goal_var = tk.StringVar(value="Fitness")
goal_menu = tk.OptionMenu(frame, goal_var, "Fun", "Fitness", "Improvement")
goal_menu.config(font=("Arial", 11))
goal_menu.pack(pady=5)

tk.Button(root, text="🎯 Get Exercise Suggestion 🎯", command=get_suggestion, font=("Comic Sans MS", 12), bg="#B0E0E6").pack(pady=15)

result_label = tk.Label(root, text="", wraplength=450, font=("Arial", 12), bg="#F0F8FF", fg="#444")
result_label.pack(pady=10)

root.mainloop()
