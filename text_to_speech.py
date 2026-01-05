"""
Text-to-Speech functionality for Spelling Game
Handles speech synthesis using pyttsx3.
"""

import queue
import threading

try:
    import pyttsx3

    TTS_AVAILABLE = True
except Exception:
    pyttsx3 = None
    TTS_AVAILABLE = False


class TextToSpeech:
    """Queue-based TTS worker that initializes the engine in the worker thread.

    This avoids issues with pyttsx3 engine usage across threads on some platforms.
    """

    def __init__(self):
        self.engine = None
        self._queue = queue.Queue()
        self._worker = threading.Thread(target=self._process_queue, daemon=True)
        self._worker.start()

    def speak(self, text):
        """Enqueue text to be spoken."""
        try:
            self._queue.put(text)
        except Exception as e:
            print(f"TTS enqueue error: {e}")

    def _init_engine(self):
        """Initialize pyttsx3 engine inside the worker thread."""
        if not TTS_AVAILABLE:
            print("pyttsx3 not available")
            return
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty("rate", 150)
            voices = self.engine.getProperty("voices")
            if voices:
                self.engine.setProperty("voice", voices[0].id)
            print("TTS engine initialized in worker thread")
        except Exception as e:
            print(f"TTS initialization error (worker): {e}")
            self.engine = None

    def _process_queue(self):
        """Worker loop: initialize engine when needed and speak queued texts."""
        while True:
            try:
                text = self._queue.get()
                if text is None:
                    break

                if self.engine is None:
                    self._init_engine()

                if self.engine is None:
                    print(f"(no engine) would speak: {text}")
                    self._queue.task_done()
                    continue

                try:
                    self.engine.say(text)
                    self.engine.runAndWait()
                except Exception as e:
                    print(f"TTS speak error: {e}")
                finally:
                    self._queue.task_done()
            except Exception as e:
                print(f"TTS worker error: {e}")
