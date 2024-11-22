# Final_Game_Project
# Jump_Pro Game

# Summary
Jump_Pro is a beginner-friendly 2D arcade game made with Python, Pygame, and simpleGE. The goal is to keep the character, Mikky, on moving platforms while earning points. If Mikky falls, the game ends with a sound effect to signal failure.

# How to Play
   - Use the arrow keys to move Mikky left, right, or jump.

# Objective
   - Stay on the platforms as long as possible to earn points.
   - Avoid falling off the platforms, or the game will end.

# Technologies and Techniques
   - Technologies: Python, Pygame, simpleGE
   - Used sprite-based graphics for Mikky and the platforms.
   - Implemented collision detection to check if Mikky lands on platforms.
   - Integrated sound for background music and losing events. (OpenGameArt -  https://opengameart.org/art-search?keys=audio&page=1)
   - Integrated game arts for visuals  (OpenGameArt - https://opengameart.org/)
   - Used timers to adjust game difficulty and increase platform speed. 

# My Process
# What I Learned
- How to use Pygame to build a basic game.
- Adding background music and sound effects.
- Handling player movement and collisions.

# Challenges
- Getting the losing sound ('letstryagain.wav') to play at the right time was tricky. I fixed this by ensuring the sound was loaded before transitioning to the next scene.
- Balancing the speed of the platforms as the score increased required some fine-tuning.

# Areas for Improvement
- I’d like to add more features, like a pause button or multiple levels for variety.
- The character could have animations for jumping and landing to make the game more engaging.
- I’d also test sound and transitions separately to avoid debugging them during integration.

# Deviation from original design
- I followed the game design document for the most part. The core gameplay mechanics (jumping, moving platforms, and scoring) stayed the same.
- However, I added background music and a sound effect for falling to make the game more fun.
