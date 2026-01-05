"""
Settings Dialog for Spelling Game
Provides a dialog for configuring game settings.
"""

import tkinter as tk
from tkinter import messagebox, ttk


class SettingsDialog:
    """Settings dialog for game configuration."""

    def __init__(self, parent, settings):
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Settings")
        self.dialog.geometry("300x220")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()

        # Center the dialog
        self.dialog.geometry(f"+{parent.winfo_x() + 150}+{parent.winfo_y() + 100}")

        # Settings frame
        frame = ttk.Frame(self.dialog, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # Number of questions
        ttk.Label(frame, text="Number of Questions:").grid(
            row=0, column=0, sticky=tk.W, pady=5
        )
        self.questions_var = tk.StringVar(value=str(settings["num_questions"]))
        questions_spin = ttk.Spinbox(
            frame, from_=5, to=20, textvariable=self.questions_var, width=10
        )
        questions_spin.grid(row=0, column=1, pady=5)

        # Minimum word length
        ttk.Label(frame, text="Minimum Word Length:").grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        self.min_len_var = tk.StringVar(value=str(settings["min_length"]))
        min_spin = ttk.Spinbox(
            frame, from_=3, to=15, textvariable=self.min_len_var, width=10
        )
        min_spin.grid(row=1, column=1, pady=5)

        # Maximum word length
        ttk.Label(frame, text="Maximum Word Length:").grid(
            row=2, column=0, sticky=tk.W, pady=5
        )
        self.max_len_var = tk.StringVar(value=str(settings["max_length"]))
        max_spin = ttk.Spinbox(
            frame, from_=3, to=15, textvariable=self.max_len_var, width=10
        )
        max_spin.grid(row=2, column=1, pady=5)

        # Use downloaded dictionary
        self.use_downloaded_var = tk.BooleanVar(
            value=settings.get("use_downloaded_dict", False)
        )
        ttk.Checkbutton(
            frame, text="Use downloaded dictionary", variable=self.use_downloaded_var
        ).grid(row=3, column=0, columnspan=2, pady=5)

        # Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Save", command=self.save).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.cancel).pack(
            side=tk.LEFT, padx=5
        )

    def save(self):
        """Save settings and close dialog."""
        try:
            num_q = int(self.questions_var.get())
            min_len = int(self.min_len_var.get())
            max_len = int(self.max_len_var.get())

            if min_len > max_len:
                messagebox.showerror(
                    "Error", "Minimum length cannot be greater than maximum length."
                )
                return

            self.result = {
                "num_questions": num_q,
                "min_length": min_len,
                "max_length": max_len,
                "use_downloaded_dict": self.use_downloaded_var.get(),
            }
            self.dialog.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def cancel(self):
        """Cancel and close dialog."""
        self.dialog.destroy()
