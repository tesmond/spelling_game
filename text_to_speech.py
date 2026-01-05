"""
Text-to-Speech functionality for Spelling Game
Handles speech synthesis using Edge TTS.
"""

import asyncio
import os
import queue
import tempfile
import threading

try:
    import edge_tts

    TTS_AVAILABLE = True
except Exception:
    edge_tts = None
    TTS_AVAILABLE = False

try:
    import pygame

    PLAYBACK_AVAILABLE = True
except Exception:
    pygame = None
    PLAYBACK_AVAILABLE = False


class TextToSpeech:
    """Queue-based TTS worker that uses Microsoft Edge TTS for speech synthesis.

    Uses Edge TTS for high-quality neural text-to-speech with no compilation required.
    """

    def __init__(self, voice="en-GB-SoniaNeural"):
        self.engine_ready = False
        self.voice = voice
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
        """Initialize pygame mixer for audio playback."""
        if not TTS_AVAILABLE:
            print("Edge TTS not available")
            return
        if not PLAYBACK_AVAILABLE:
            print("pygame not available for audio playback")
            return
        try:
            pygame.mixer.init()
            self.engine_ready = True
            print("Edge TTS engine initialized in worker thread")
        except Exception as e:
            print(f"TTS initialization error (worker): {e}")
            self.engine_ready = False

    async def _synthesize_speech(self, text, output_path):
        """Async function to synthesize speech using Edge TTS."""
        # Use configured voice
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(output_path)

    def _process_queue(self):
        """Worker loop: initialize engine when needed and speak queued texts."""
        while True:
            try:
                text = self._queue.get()
                if text is None:
                    break

                if not self.engine_ready:
                    self._init_engine()

                if not self.engine_ready:
                    print(f"(no engine) would speak: {text}")
                    self._queue.task_done()
                    continue

                try:
                    # Generate speech to a temporary MP3 file
                    with tempfile.NamedTemporaryFile(
                        suffix=".mp3", delete=False
                    ) as tmp_file:
                        tmp_path = tmp_file.name

                    # Run async TTS synthesis
                    asyncio.run(self._synthesize_speech(text, tmp_path))

                    # Play the audio using pygame
                    pygame.mixer.music.load(tmp_path)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)

                    # Clean up temporary file
                    try:
                        os.unlink(tmp_path)
                    except:
                        pass

                except Exception as e:
                    print(f"TTS speak error: {e}")
                finally:
                    self._queue.task_done()
            except Exception as e:
                print(f"TTS worker error: {e}")
