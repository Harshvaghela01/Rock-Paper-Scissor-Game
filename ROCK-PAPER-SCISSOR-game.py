#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SimpleGUICS2pygame


# In[ ]:





# In[5]:


import random


# In[7]:


import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# In[8]:


import math


# In[15]:


import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ['rock', 'paper', 'scissors']
    
    print("Let's play Rock-Paper-Scissors!")
    print("Choose one: rock, paper, scissors")
    player_choice = input("Your choice: ").lower()
    
    while player_choice not in choices:
        print("Invalid choice. Please choose again.")
        player_choice = input("Your choice: ").lower()
    
    computer_choice = random.choice(choices)
    
    print(f"Your choice: {player_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Play the game
play_game()


# In[ ]:





# In[ ]:




