import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import random
import os

# Load questions
with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

random.shuffle(questions)

current_index = 0
score = 0
total_questions = len(questions)
answers_detail = []  # Lưu chi tiết câu trả lời

def load_question():
    global current_index
    if current_index < len(questions):
        question_label.config(text=questions[current_index]["sentence"])
        entry.delete(0, tk.END)
        result_label.config(text="")
        
        # Load image
        load_image(questions[current_index].get("image", ""))
        
        # Update progress
        progress_label.config(text=f"Question: {current_index + 1}/{total_questions}")
    else:
        show_game_over()

def load_image(image_path):
    """Load and display image for the question"""
    try:
        if image_path and os.path.exists(image_path):
            img = Image.open(image_path)
            img.thumbnail((400, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            image_label.config(image=photo)
            image_label.image = photo
        else:
            # Placeholder if no image
            image_label.config(image="", text="📚 No image available")
    except Exception as e:
        image_label.config(image="", text="❌ Error loading image")

def check_answer():
    global current_index, score
    user_answer = entry.get().strip().lower()
    correct_answer = questions[current_index]["answer"].lower()

    is_correct = user_answer == correct_answer
    
    # Save answer detail
    answers_detail.append({
        "question": questions[current_index]["sentence"],
        "user_answer": user_answer,
        "correct_answer": correct_answer,
        "is_correct": is_correct
    })

    if is_correct:
        result_label.config(text="✓ Correct!", fg="green")
        score += 1
    else:
        result_label.config(
            text=f"✗ Wrong! Answer: {correct_answer}", fg="red"
        )

    score_label.config(text=f"Score: {score}/{total_questions}")
    current_index += 1
    root.after(1500, load_question)

def show_game_over():
    """Display game over screen with results"""
    question_label.config(text="🎉 Game Over! 🎉")
    result_label.config(text=f"Final Score: {score}/{total_questions}")
    image_label.config(image="", text="")
    entry.config(state="disabled")
    submit_btn.config(state="disabled")
    progress_label.config(text="")
    
    # Show results button
    results_btn.config(state="normal")

def show_results():
    """Display detailed results"""
    results_window = tk.Toplevel(root)
    results_window.title("Results Summary")
    results_window.geometry("650x500")
    
    # Scrollable frame
    canvas = tk.Canvas(results_window, bg="white")
    scrollbar = tk.Scrollbar(results_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="white")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Title
    title = tk.Label(scrollable_frame, text="📊 Results Summary", font=("Arial", 16, "bold"), bg="white")
    title.pack(pady=10)
    
    # Statistics
    percentage = (score / total_questions) * 100
    stats_text = f"Score: {score}/{total_questions} ({percentage:.1f}%)"
    stats = tk.Label(scrollable_frame, text=stats_text, font=("Arial", 13, "bold"), fg="blue", bg="white")
    stats.pack(pady=5)
    
    # Separator
    tk.Label(scrollable_frame, text="=" * 60, bg="white").pack()
    
    # Answer details
    for i, detail in enumerate(answers_detail, 1):
        frame = tk.Frame(scrollable_frame, relief="solid", borderwidth=1, padx=10, pady=8, bg="white")
        frame.pack(fill="x", padx=8, pady=5)
        
        # Question
        q_label = tk.Label(frame, text=f"Q{i}: {detail['question']}", 
                          font=("Arial", 10, "bold"), wraplength=550, justify="left", bg="white")
        q_label.pack(anchor="w")
        
        # Your answer
        color = "green" if detail['is_correct'] else "red"
        status = "✓" if detail['is_correct'] else "✗"
        y_label = tk.Label(frame, text=f"{status} Your answer: {detail['user_answer']}", 
                          font=("Arial", 9), fg=color, bg="white")
        y_label.pack(anchor="w")
        
        # Correct answer (if wrong)
        if not detail['is_correct']:
            c_label = tk.Label(frame, text=f"✓ Correct answer: {detail['correct_answer']}", 
                              font=("Arial", 9), fg="green", bg="white")
            c_label.pack(anchor="w")
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Close button
    close_btn = tk.Button(results_window, text="Close", command=results_window.destroy, 
                         font=("Arial", 11), bg="#757575", fg="white")
    close_btn.pack(pady=10)

def restart_game():
    """Restart the game"""
    global current_index, score, answers_detail, questions
    
    current_index = 0
    score = 0
    answers_detail = []
    random.shuffle(questions)
    
    entry.config(state="normal")
    submit_btn.config(state="normal")
    results_btn.config(state="disabled")
    score_label.config(text="Score: 0")
    
    load_question()

# UI setup
root = tk.Tk()
root.title("English Fill-in-the-Blank Game")
root.geometry("650x750")
root.config(bg="#f0f0f0")

# Title
title = tk.Label(root, text="📝 Fill in the Blank", font=("Arial", 22, "bold"), bg="#f0f0f0", fg="#1976D2")
title.pack(pady=15)

# Progress
progress_label = tk.Label(root, text="", font=("Arial", 10), bg="#f0f0f0", fg="#666")
progress_label.pack()

# Image area
image_label = tk.Label(root, bg="white", width=400, height=200, relief="solid", borderwidth=2, 
                       font=("Arial", 14), fg="#999")
image_label.pack(pady=15, padx=15, fill="both", expand=True)

# Question
question_label = tk.Label(root, text="", font=("Arial", 14, "bold"), 
                         wraplength=550, justify="center", bg="#f0f0f0", fg="#333")
question_label.pack(pady=15)

# Input frame
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Your answer:", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(side="left", padx=5)
entry = tk.Entry(input_frame, font=("Arial", 12), width=28, relief="solid", borderwidth=1)
entry.pack(side="left", padx=5)
entry.bind('<Return>', lambda e: check_answer())  # Allow Enter key

# Button frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

submit_btn = tk.Button(button_frame, text="Submit", command=check_answer, 
                      font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", padx=15, relief="raised")
submit_btn.pack(side="left", padx=5)

results_btn = tk.Button(button_frame, text="View Results", command=show_results, 
                       font=("Arial", 11, "bold"), bg="#2196F3", fg="white", padx=15, relief="raised", state="disabled")
results_btn.pack(side="left", padx=5)

restart_btn = tk.Button(button_frame, text="Restart", command=restart_game, 
                       font=("Arial", 11, "bold"), bg="#FF9800", fg="white", padx=15, relief="raised")
restart_btn.pack(side="left", padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

# Score label
score_label = tk.Label(root, text="Score: 0", font=("Arial", 13, "bold"), 
                      fg="#2196F3", bg="#f0f0f0")
score_label.pack(pady=10)

load_question()
root.mainloop()
