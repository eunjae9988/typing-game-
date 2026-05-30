I made a simple Python typing game where users answer randomly generated word questions and measure how long it takes to complete them.
Through this project, I explore cognitive processing speed, attention, and response accuracy using a timed word recognition task.
This project focuses on building a small interactive program that measures how quickly and accurately users respond to text prompts. It combines basic Python concepts with real-time user input and timing.

How process work
- The list (cat,fox,monkey,etc) is the system visual stimuli.
- When an incorrect input occurs then system detect conflict and drving behavioral correction.

Techical implementation and code analysis
- import time is used to fetch the exact time. By calculating the difference between the start and end of the session, the program measures the exact reaction time taken to complete the task.
- import random is for utilized via "random.choice' to ensuring the subject canot predict the next word
- time.time() is a function that captures the exact timestamp in seconds. It measures the time taken to process the word and type it out.

What I learned
- I learned how to use isdigit() to prevent errors by checking if user input is a number
- I practiced using loops, standard libraries and recursive function to build a functional interactive program. 
