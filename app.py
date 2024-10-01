import streamlit as st 

st.title("My First app")
st.image("giphy.gif")

import random
import streamlit as st

# Function to get computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Streamlit app UI and logic
def play_game():
    st.title("Rock-Paper-Scissors Game")

    st.write("Choose one of the options below to play:")
    
    # Buttons for user input
    user_choice = st.radio("Make your choice:", ['rock', 'paper', 'scissors'])

    if st.button("Play"):
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        # Display the results
        st.write(f"You chose: {user_choice}")
        st.write(f"Computer chose: {computer_choice}")
        st.write(result)

if __name__ == "__main__":
    play_game()



