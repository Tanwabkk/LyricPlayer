import time
import sys

print("\nSong playing: Earrings.\n")

lyrics = [
    "Her love is in your head",
    "You lost you earrings in her bed",
    "You couldn't tell her that you lost 'em",
    "Cause you're scared and you're not talking",
    "So you think of what to say",
    "And save it for another day",
    "Cause you just never had the heart",
    "Now they just drift furthur apart", 
    "From you....."
]


timings = [1.0,1.0,1.2,1.2,1.2,1.2,1.6,1.2,1.2,1.8]


typing_speed=0.05

for line,delay in zip(lyrics,timings):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)
    print()
    time.sleep(delay)
