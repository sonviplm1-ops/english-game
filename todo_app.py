import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os
from datetime import datetime

# Configuration
DATA_FILE = "todos.json"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List Application")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.config(bg="#f0f0f0")
        self.root.resizable(False, False)
        
        self.todos = []
        self.load_todos()
        
        self.setup_ui()
        self.refresh_list()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Header
        header_frame = tk.Frame(self.root, bg="#1976D2", height=80)
        header_frame.pack(fill="x")
        
        title = tk.Label(header_frame, text="📝 My To-Do List", 
                        font=("Arial", 24, "bold"), bg="#1976D2", fg="white")
        title.pack(pady=15)
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=15, padx=15, fill="x")
        
        tk.Label(input_frame, text="Add new task:", font=("Arial", 10, "bold"), bg="#f0f0f0").pack(anchor="w")
        
        entry_frame = tk.Frame(input_frame, bg="#f0f0f0")
        entry_frame.pack(fill="x", pady=5)
        
        self.entry = tk.Entry(entry_frame, font=("Arial", 11), relief="solid", borderwidth=1)
        self.entry.pack(side="left", fill="both", expand=True, padx=(0, 5))
        self.entry.bind('<Return>', lambda e: self.add_todo())
        
        add_btn = tk.Button(entry_frame, text="Add", command=self.add_todo, 
                           font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", padx=20)
        add_btn.pack(side="left")
        
        # Stats Frame
        stats_frame = tk.Frame(self.root, bg="white", relief="solid", borderwidth=1)
        stats_frame.pack(pady=10, padx=15, fill="x")
        
        left_stats = tk.Frame(stats_frame, bg="white")
        left_stats.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        tk.Label(left_stats, text="Total Tasks", font=("Arial", 9), bg="white", fg="#666").pack(anchor="w")
        self.total_label = tk.Label(left_stats, text="0", font=("Arial", 16, "bold"), bg="white", fg="#1976D2")
        self.total_label.pack(anchor="w")
        
        middle_stats = tk.Frame(stats_frame, bg="white")
        middle_stats.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        tk.Label(middle_stats, text="Completed", font=("Arial", 9), bg="white", fg="#666").pack(anchor="w")
        self.completed_label = tk.Label(middle_stats, text="0", font=("Arial", 16, "bold"), bg="white", fg="#4CAF50")
        self.completed_label.pack(anchor="w")
        
        right_stats = tk.Frame(stats_frame, bg="white")
        right_stats.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        tk.Label(right_stats, text="Remaining", font=("Arial", 9), bg="white", fg="#666").pack(anchor="w")
        self.remaining_label = tk.Label(right_stats, text="0", font=("Arial", 16, "bold"), bg="white", fg="#FF9800")
        self.remaining_label.pack(anchor="w")
        
        # Filter Frame
        filter_frame = tk.Frame(self.root, bg="#f0f0f0")
        filter_frame.pack(pady=10, padx=15, fill="x")
        
        tk.Label(filter_frame, text="Filter:", font=("Arial", 10, "bold"), bg="#f0f0f0").pack(side="left", padx=5)
        
        self.filter_var = tk.StringVar(value="all")
        filters = [("All", "all"), ("Active", "active"), ("Completed", "completed")]
        
        for text, value in filters:
            rb = tk.Radiobutton(filter_frame, text=text, variable=self.filter_var, value=value,
                              command=self.refresh_list, bg="#f0f0f0", font=("Arial", 10))
            rb.pack(side="left", padx=5)
        
        # List Frame with Scrollbar
        list_frame = tk.Frame(self.root, bg="#f0f0f0")
        list_frame.pack(pady=10, padx=15, fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, 
                                 font=("Arial", 10), relief="solid", borderwidth=1,
                                 bg="white", activestyle="none")
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.listbox.yview)
        
        # Button Frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10, padx=15, fill="x")
        
        clear_completed_btn = tk.Button(button_frame, text="Clear Completed", 
                                       command=self.clear_completed,
                                       font=("Arial", 10, "bold"), bg="#FF9800", fg="white", padx=15)
        clear_completed_btn.pack(side="left", padx=5)
        
        delete_all_btn = tk.Button(button_frame, text="Delete All", 
                                  command=self.delete_all,
                                  font=("Arial", 10, "bold"), bg="#F44336", fg="white", padx=15)
        delete_all_btn.pack(side="left", padx=5)
        
        export_btn = tk.Button(button_frame, text="Export", 
                             command=self.export_todos,
                             font=("Arial", 10, "bold"), bg="#2196F3", fg="white", padx=15)
        export_btn.pack(side="right", padx=5)
        
        # Bind listbox click event
        self.listbox.bind('<Double-Button-1>', self.on_listbox_click)
        self.listbox.bind('<Delete>', lambda e: self.delete_selected())
        self.listbox.bind('<space>', lambda e: self.toggle_selected())
    
    def add_todo(self):
        """Add a new todo item"""
        task = self.entry.get().strip()
        
        if not task:
            messagebox.showwarning("Empty Task", "Please enter a task!")
            return
        
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed_at": None
        }
        
        self.todos.append(todo)
        self.save_todos()
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.refresh_list()
        messagebox.showinfo("Success", "Task added successfully! ✓")
    
    def toggle_todo(self, index):
        """Toggle todo completion status"""
        if 0 <= index < len(self.todos):
            self.todos[index]["completed"] = not self.todos[index]["completed"]
            if self.todos[index]["completed"]:
                self.todos[index]["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                self.todos[index]["completed_at"] = None
            self.save_todos()
            self.refresh_list()
    
    def delete_todo(self, index):
        """Delete a todo item"""
        if 0 <= index < len(self.todos):
            self.todos.pop(index)
            self.save_todos()
            self.refresh_list()
    
    def on_listbox_click(self, event):
        """Handle listbox double-click"""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.show_todo_menu(index)
    
    def show_todo_menu(self, index):
        """Show context menu for todo item"""
        menu = tk.Menu(self.root, tearoff=False)
        menu.add_command(label="✓ Toggle Completion", 
                        command=lambda: self.toggle_todo(index))
        menu.add_command(label="✎ Edit", 
                        command=lambda: self.edit_todo(index))
        menu.add_command(label="📋 View Details", 
                        command=lambda: self.view_details(index))
        menu.add_separator()
        menu.add_command(label="✕ Delete", 
                        command=lambda: self.delete_with_confirm(index))
        
        try:
            menu.tk_popup(self.root.winfo_pointerx(), self.root.winfo_pointery())
        finally:
            menu.grab_release()
    
    def edit_todo(self, index):
        """Edit a todo item"""
        old_task = self.todos[index]["task"]
        new_task = simpledialog.askstring("Edit Task", f"Current task:\n{old_task}", 
                                         initialvalue=old_task)
        
        if new_task and new_task.strip():
            self.todos[index]["task"] = new_task.strip()
            self.save_todos()
            self.refresh_list()
            messagebox.showinfo("Success", "Task updated successfully! ✓")
    
    def view_details(self, index):
        """Show task details"""
        todo = self.todos[index]
        details = f"""
Task: {todo['task']}

Status: {'✓ Completed' if todo['completed'] else '○ Active'}

Created: {todo['created_at']}

Completed: {todo['completed_at'] if todo['completed_at'] else 'Not completed yet'}
        """
        messagebox.showinfo("Task Details", details.strip())
    
    def delete_with_confirm(self, index):
        """Delete with confirmation"""
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?"):
            self.delete_todo(index)
            messagebox.showinfo("Success", "Task deleted successfully! ✓")
    
    def toggle_selected(self):
        """Toggle selected item with spacebar"""
        selection = self.listbox.curselection()
        if selection:
            self.toggle_todo(selection[0])
    
    def delete_selected(self):
        """Delete selected item with Delete key"""
        selection = self.listbox.curselection()
        if selection:
            self.delete_with_confirm(selection[0])
    
    def clear_completed(self):
        """Clear all completed tasks"""
        completed_count = sum(1 for todo in self.todos if todo["completed"])
        
        if completed_count == 0:
            messagebox.showinfo("Info", "No completed tasks to clear!")
            return
        
        if messagebox.askyesno("Confirm", f"Delete {completed_count} completed task(s)?"):
            self.todos = [todo for todo in self.todos if not todo["completed"]]
            self.save_todos()
            self.refresh_list()
            messagebox.showinfo("Success", f"Cleared {completed_count} task(s)! ✓")
    
    def delete_all(self):
        """Delete all tasks"""
        if not self.todos:
            messagebox.showinfo("Info", "No tasks to delete!")
            return
        
        if messagebox.askyesno("Confirm", f"Delete all {len(self.todos)} task(s)? This cannot be undone!"):
            self.todos = []
            self.save_todos()
            self.refresh_list()
            messagebox.showinfo("Success", "All tasks deleted! ✓")
    
    def export_todos(self):
        """Export todos to JSON file"""
        export_file = "todos_export.json"
        try:
            with open(export_file, "w", encoding="utf-8") as f:
                json.dump(self.todos, f, indent=2, ensure_ascii=False)
            messagebox.showinfo("Success", f"Tasks exported to {export_file}! ✓")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {str(e)}")
    
    def refresh_list(self):
        """Refresh the listbox display"""
        self.listbox.delete(0, tk.END)
        
        filter_type = self.filter_var.get()
        
        for todo in self.todos:
            if filter_type == "active" and todo["completed"]:
                continue
            if filter_type == "completed" and not todo["completed"]:
                continue
            
            status = "✓" if todo["completed"] else "○"
            display_text = f"{status} {todo['task']}"
            self.listbox.insert(tk.END, display_text)
        
        # Update statistics
        total = len(self.todos)
        completed = sum(1 for todo in self.todos if todo["completed"])
        remaining = total - completed
        
        self.total_label.config(text=str(total))
        self.completed_label.config(text=str(completed))
        self.remaining_label.config(text=str(remaining))
    
    def save_todos(self):
        """Save todos to JSON file"""
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(self.todos, f, indent=2, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")
    
    def load_todos(self):
        """Load todos from JSON file"""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    self.todos = json.load(f)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load: {str(e)}")
                self.todos = []
        else:
            self.todos = []

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
