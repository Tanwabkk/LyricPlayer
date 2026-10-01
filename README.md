🎧 Terminal Song Lyric Player

A lightweight, command-line lyric synchronization tool written in Python. This script simulates a real-time karaoke or lyric video display by printing text character-by-character with custom typing animations and synchronized line-by-line pacing.

🛠️ Technologies & Languages Used

Language: Python 3.x

Core Built-in Libraries:

time — Manages delays between printed characters and pauses between lines.

sys — Directs standard output manipulation (sys.stdout) for precise buffer control.

⚙️️ How It Works & Concept Implementation

This script relies on stream control and data pairing to create a smooth terminal animation:

Data Association (zip):
The lyrics are stored in a list of strings (lyrics), while their respective pauses are stored in a parallel list of floats (timings). The built-in zip() function dynamically pairs each lyric line with its exact delay metric.

Character-by-Character Iteration:
Instead of outputting an entire block of text at once, a nested loop iterates through every single character of a given line.

Forced Stream Flushing (sys.stdout.flush()):
Python normally buffers terminal text until a newline character (\n) is encountered. By using sys.stdout.write(char) alongside sys.stdout.flush(), the program forces the console to render each letter instantly, creating the typewriter effect.

Cadence Control:

time.sleep(typing_speed) dictates how fast individual characters appear.

time.sleep(delay) introduces a custom pause after a full line is completed, matching the song's rhythm.

💡 What This Project Taught Me

Building this project helped me strengthen several foundational computer science and programming concepts:

Buffer Management: Understanding how terminal standard output behaves and how to bypass default buffering to build real-time visual interfaces in the command line.

Parallel Iteration: Learning how to cleanly coordinate multiple data structures simultaneously using zip().

Timing and Flow Control: Gaining practical experience with execution pacing using time delays.

Algorithmic Thinking: Breaking down a dynamic, real-world concept (karaoke tracking) into clean loops, lists, and variables.

🚀 Quick Start

Ensure you have Python 3 installed on your machine.

Clone or download this repository and save your script as player.py.

Run the script from your terminal:

python player.py
