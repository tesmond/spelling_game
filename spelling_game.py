"""
Spelling Game
A simple spelling game that speaks a word, provides its definition,
and asks you to spell it correctly.
"""

import random
import tkinter as tk
from tkinter import messagebox, ttk

import playsound3

from dictionary_manager import DictionaryManager
from settings_dialog import SettingsDialog
from text_to_speech import TextToSpeech


class SpellingGame:
    """Main spelling game class."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Spelling Game")
        self.root.geometry("800x700")
        self.root.minsize(700, 600)
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)
        self.root.configure(bg="#f0f0f0")

        # Modern styling
        style = ttk.Style()
        style.theme_use("clam")

        # Configure fonts to use system defaults with better sizes
        style.configure("TLabel", font=("TkDefaultFont", 12), background="#f0f0f0")
        style.configure(
            "TButton",
            font=("TkDefaultFont", 12),
            padding=10,
            relief="raised",
            borderwidth=1,
            background="#ffffff",
        )
        style.configure("TEntry", font=("TkTextFont", 12), padding=5)
        style.configure("TFrame", background="#f0f0f0")
        style.configure(
            "TLabelFrame", background="#f0f0f0", borderwidth=2, relief="groove"
        )
        style.configure(
            "TLabelFrame.Label",
            font=("TkHeadingFont", 14, "bold"),
            background="#f0f0f0",
        )
        style.configure("TScrollbar", background="#f0f0f0")

        # Custom styles
        style.configure("WordEntry.TEntry", font=("TkDefaultFont", 22), padding=10)
        style.configure("Title.TLabel", font=("TkDefaultFont", 20, "bold"))
        style.configure("Feedback.TLabel", font=("TkDefaultFont", 14))

        style.configure("Custom.TLabelframe", background="#f0f0f0")
        style.configure("Custom.TLabelframe.Label", background="#f0f0f0")

        # Button hover effects
        style.map("TButton", background=[("active", "#e8e8e8")])

        # Settings
        self.settings = {
            "num_questions": 10,
            "min_length": 5,
            "max_length": 7,
            "use_downloaded_dict": False,
            "voice": "en-GB-SoniaNeural",
        }

        # Game state
        self.current_word = ""
        self.current_definition = ""
        self.question_number = 0
        self.score = 0
        self.results = []  # List of (word, user_answer, correct) tuples
        self.word_list = []

        # Initialize components
        self.dict_manager = DictionaryManager(
            use_downloaded=self.settings["use_downloaded_dict"]
        )
        self.tts = TextToSpeech(voice=self.settings["voice"])

        # Create UI
        self.create_menu()
        self.create_game_frame()
        self.create_results_frame()

        # Show game frame
        self.show_game_frame()
        self.start_new_game()

    def create_menu(self):
        """Create the menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Game menu
        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.start_new_game)
        game_menu.add_separator()
        game_menu.add_command(label="Settings", command=self.show_settings)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.root.quit)

    def create_game_frame(self):
        """Create the main game interface."""
        self.game_frame = ttk.Frame(self.root, padding="30")

        # Progress label
        self.progress_label = ttk.Label(
            self.game_frame, text="Question 1 of 10", style="Title.TLabel"
        )
        self.progress_label.pack(pady=(0, 10))

        # Score label
        self.score_label = ttk.Label(self.game_frame, text="Score: 0")
        self.score_label.pack(pady=(0, 20))

        # Definition frame
        def_frame = ttk.LabelFrame(
            self.game_frame, text="Definition", padding="20", style="Custom.TLabelframe"
        )
        def_frame.pack(fill=tk.X, pady=(0, 30))

        # Container for definition text and speaker button
        def_container = ttk.Frame(def_frame)
        def_container.pack(fill=tk.BOTH, expand=True)

        self.definition_label = ttk.Label(
            def_container,
            text="",
            wraplength=600,
            justify=tk.CENTER,
        )
        self.definition_label.pack(pady=10)

        # Speaker button in bottom right
        speaker_btn = ttk.Button(
            def_frame, text="🔊", width=3, command=self.speak_definition
        )
        speaker_btn.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-5)

        # Replay button
        self.replay_btn = ttk.Button(
            self.game_frame, text="Replay Word", command=self.speak_word
        )
        self.replay_btn.pack(pady=(0, 20))

        # Entry frame
        entry_frame = ttk.Frame(self.game_frame)
        entry_frame.pack(pady=(0, 30))

        ttk.Label(entry_frame, text="Spell the word:").pack(pady=(0, 10))

        self.word_entry = ttk.Entry(
            entry_frame,
            width=25,
            justify=tk.CENTER,
            style="WordEntry.TEntry",
            font=("TkDefaultFont", 22),
        )
        self.word_entry.pack(pady=(0, 20))
        self.word_entry.bind("<Return>", lambda e: self.submit_answer())

        # Submit button
        self.submit_btn = ttk.Button(
            self.game_frame, text="Submit Answer", command=self.submit_answer
        )
        self.submit_btn.pack(pady=(0, 20))

        # Feedback label
        self.feedback_label = ttk.Label(
            self.game_frame, text="", style="Feedback.TLabel"
        )
        self.feedback_label.pack(pady=(0, 10))

    def create_results_frame(self):
        """Create the results screen."""
        self.results_frame = ttk.Frame(self.root, padding="30")

        # Title
        self.results_title = ttk.Label(
            self.results_frame, text="Game Over!", style="Title.TLabel"
        )
        self.results_title.pack(pady=(0, 20))

        # Final score
        self.final_score_label = ttk.Label(
            self.results_frame, text="", style="Feedback.TLabel"
        )
        self.final_score_label.pack(pady=(0, 20))

        # Results list frame with scrollbar
        list_frame = ttk.Frame(self.results_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 30))

        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.results_listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            height=12,
            font=("TkDefaultFont", 14),
        )
        self.results_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.results_listbox.yview)

        # Play again button
        self.play_again_btn = ttk.Button(
            self.results_frame, text="Play Again", command=self.start_new_game
        )
        self.play_again_btn.pack(pady=(0, 10))

    def show_game_frame(self):
        """Show the game frame."""
        self.results_frame.pack_forget()
        self.game_frame.pack(fill=tk.BOTH, expand=True)

    def show_results_frame(self):
        """Show the results frame."""
        self.game_frame.pack_forget()
        self.results_frame.pack(fill=tk.BOTH, expand=True)

        # Update final score
        self.final_score_label.config(
            text=f"Your Score: {self.score} / {self.settings['num_questions']}"
        )

        if self.score >= self.settings["num_questions"] // 2:
            playsound3.playsound("sounds/cheer.mp3", block=False)  # Finished sound
        else:
            playsound3.playsound("sounds/boo.mp3", block=False)  # Finished sound

        # Populate results list
        self.results_listbox.delete(0, tk.END)
        for i, (word, user_answer, correct) in enumerate(self.results, 1):
            status = "✓" if correct else "✗"
            if correct:
                self.results_listbox.insert(tk.END, f"{i}. {status} {word}")
            else:
                self.results_listbox.insert(
                    tk.END, f"{i}. {status} {word} (you typed: {user_answer})"
                )

    def show_settings(self):
        """Show the settings dialog."""
        dialog = SettingsDialog(self.root, self.settings)
        self.root.wait_window(dialog.dialog)

        if dialog.result:
            old_use_downloaded = self.settings.get("use_downloaded_dict", False)
            old_voice = self.settings.get("voice", "en-GB-SoniaNeural")
            self.settings = dialog.result
            if self.settings["use_downloaded_dict"] != old_use_downloaded:
                self.dict_manager = DictionaryManager(
                    use_downloaded=self.settings["use_downloaded_dict"]
                )
            if self.settings["voice"] != old_voice:
                self.tts = TextToSpeech(voice=self.settings["voice"])

    def start_new_game(self):
        """Start a new game."""
        self.question_number = 0
        self.score = 0
        self.results = []

        # Get words for this game
        available_words = self.dict_manager.get_words_by_length(
            self.settings["min_length"], self.settings["max_length"]
        )

        if len(available_words) < self.settings["num_questions"]:
            messagebox.showwarning(
                "Warning",
                f"Only {len(available_words)} words available for selected length range. "
                "Consider adjusting settings.",
            )

        # Select random words
        word_items = list(available_words.items())
        random.shuffle(word_items)
        self.word_list = word_items[: self.settings["num_questions"]]

        # Show game frame and load first question
        self.show_game_frame()
        self.load_next_question()

    def load_next_question(self):
        """Load the next question."""
        if self.question_number >= len(self.word_list):
            self.show_results_frame()
            return

        self.current_word, self.current_definition = self.word_list[
            self.question_number
        ]

        # Update UI
        self.progress_label.config(
            text=f"Question {self.question_number + 1} of {len(self.word_list)}"
        )
        self.score_label.config(text=f"Score: {self.score}")
        self.definition_label.config(text=self.current_definition)
        self.feedback_label.config(text="")
        self.word_entry.delete(0, tk.END)
        self.word_entry.focus()

        # Speak the word after a 1 second delay
        self.root.after(1000, self.speak_word)

    def speak_word(self):
        """Speak the current word."""
        self.tts.speak(f"Spell the word: {self.current_word}")
        self.word_entry.focus()

    def speak_definition(self):
        """Speak the current definition."""
        if self.current_definition:
            self.tts.speak(self.current_definition)
        self.word_entry.focus()

    def submit_answer(self):
        """Submit the user's answer."""
        user_answer = self.word_entry.get().strip().lower()
        correct_answer = self.current_word.lower()

        if not user_answer:
            messagebox.showinfo("Info", "Please enter a word.")
            return

        is_correct = user_answer == correct_answer

        if is_correct:
            self.score += 1
            self.feedback_label.config(text="✓ Correct!", foreground="green")
            playsound3.playsound("sounds/success.mp3", block=False)  # Success sound
        else:
            self.feedback_label.config(
                text=f"✗ Incorrect. The correct spelling is: {self.current_word}",
                foreground="red",
            )
            playsound3.playsound("sounds/error.mp3", block=False)  # Error sound

        # Record result
        self.results.append((self.current_word, user_answer, is_correct))

        # Move to next question after a short delay
        self.question_number += 1
        self.root.after(1500, self.load_next_question)

    def run(self):
        """Run the game."""
        self.root.mainloop()


if __name__ == "__main__":
    game = SpellingGame()
    game.run()
