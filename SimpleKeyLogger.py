import tkinter as tk
from tkinter import messagebox, filedialog
import datetime

class SimpleKeylogger:
    def __init__(self, window):
        # Set up the main window
        window.title("Keyboard Logger (Demo)")
        window.geometry("500x400")
        
        # Store pressed keys
        self.keys_logged = []
        self.logging_active = False
        
        # Create the typing area
        self.text_box = tk.Text(window, height=10, width=50)
        self.text_box.pack(pady=20)
        self.text_box.bind("<KeyPress>", self.log_key)
        
        # Create control buttons
        self.start_btn = tk.Button(window, text="Start Logging", command=self.start)
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_btn = tk.Button(window, text="Stop Logging", command=self.stop, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT)
        
        self.save_btn = tk.Button(window, text="Save Log", command=self.save)
        self.save_btn.pack(side=tk.RIGHT, padx=10)
        
        # Status display
        self.status = tk.Label(window, text="Status: Ready")
        self.status.pack(pady=10)
        
        # Warning label
        warning = tk.Label(window, text="NOTE: Only logs typing in this window!", fg="red")
        warning.pack()

    def log_key(self, event):
        # Record key presses when logging is active
        if self.logging_active:
            key = event.char
            
            # Handle special keys
            if key == "\x08":  # Backspace
                key = "[BACKSPACE]"
            elif key == "\r":  # Enter
                key = "[ENTER]"
            elif key == " ":
                key = "[SPACE]"
            elif not key.isprintable():
                return  # Skip non-printable keys
            
            # Add timestamp and save
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            self.keys_logged.append(f"{timestamp} - {key}")

    def start(self):
        # Start logging keys
        self.logging_active = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status.config(text="Status: Logging...", fg="green")
        messagebox.showinfo("Started", "Now logging your keystrokes!")

    def stop(self):
        # Stop logging keys
        self.logging_active = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status.config(text="Status: Stopped", fg="red")
        messagebox.showinfo("Stopped", "No longer logging keystrokes")

    def save(self):
        # Save logged keys to a file
        if not self.keys_logged:
            messagebox.showwarning("Empty", "No keys logged yet!")
            return
            
        # Create default filename with current date/time
        filename = f"keylog_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        # Ask user where to save
        filepath = filedialog.asksaveasfilename(
            initialfile=filename,
            filetypes=[("Text Files", "*.txt")]
        )
        
        if filepath:
            try:
                with open(filepath, "w") as f:
                    f.write("\n".join(self.keys_logged))
                messagebox.showinfo("Saved", f"Keys saved to:\n{filepath}")
                self.keys_logged = []  # Clear after saving
            except Exception as e:
                messagebox.showerror("Error", f"Couldn't save file:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleKeylogger(root)
    root.mainloop()
