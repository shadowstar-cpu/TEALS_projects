"""
My Pokemon game.
"""

from players import Computer, User

def show_pikachu():
    """Some ASCII art."""
    print("""
`;-.          ___,
  `.`\_...._/`.-"`
    \        /      ,
    /()   () \    .' `-._
   |)  .    ()\  /   _.'
   \  -'-     ,; '. <
    ;.__     ,;|   > \\
   / ,    / ,  |.-'.-'
  (_/    (_/ ,;|.<`
    \    ,     ;-`
     >   \    /
    (_,-'`> .'
         (_,'
""")

def start_game():
    """Start the Pokemon game."""
    show_pikachu()

    user = User(input("Your name? "))
    #user = Computer("Pikachu")
    computer = Computer("Lysandre")
    user.take_a_turn_against(computer)

# Get this game started.
start_game()
