#In the game Rock-Paper-Scissors, two opponents
#simultaneously choose to throw either "Rock", "Paper",
#or "Scissors". Rock beats Scissors, Scissors beats Paper,
#and Paper beats Rock. If both players throw the same
#object, the round is a tie.
#
#Write a function called find_winner. find_winner will take
#as input a list of 2-tuples, each representing a round of
#Rock-Paper-Scissors. Each 2-tuple will contain two strings.
#Each string will be either "Rock", "Paper", or "Scissors".
#The first item in the 2-tuple will represent what Player 1
#chooses in each round, and the second item in the 2-tuple
#will represent what Player 2 chooses in each round.
#
#find_winner should return the string "Player 1 wins!" if
#Player 1 wins more games than Player 2. It should return the
#string "Player 2 wins!" if Player 2 wins more games than
#Player 1. It should return the string "It's a tie!" if the
#two players win an equal number of times. 
#
#The number of times the two players tie is irrelevant to the
#result: all that matters is who wins more rounds than the
#other.
#
#For example:
#
# find_winner([("Rock", "Rock"), ("Rock", "Scissors"),
#              ("Paper", "Rock"), ("Scissors", "Rock")])
#
#...would return "Player 1 wins!" because Player 1 wins
#two round and Player 2 wins one round.


#Write your function here!

def find_winner(tuple_list):
    player1_score = 0
    player2_score = 0

    for round in tuple_list:
        result = gamerule(round)     
        if result == 1:
            player1_score += 1
        elif result == 2:
            player2_score += 1

    if player1_score > player2_score:
        return ("Player 1 wins!")
    elif player1_score < player2_score:
        return ("Player 2 wins!")
    else:
        return ("It's a tie!")
    
def gamerule(a_tuple):
    
    gamerule_dict = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }

    player1 = a_tuple[0]
    player2 = a_tuple[1]

    if player1 == player2:
        return 0
    elif gamerule_dict[player1] == player2:
        return 1
    else:
        return 2


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Player 1 wins!
#Player 2 wins!
#It's a tie!

p1_wins = [("Rock", "Rock"), ("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Rock")]
p2_wins = [("Paper", "Rock"), ("Paper", "Paper"), ("Paper", "Scissors"), ("Rock", "Paper")]
itsatie = [("Paper", "Paper"), ("Paper", "Rock"), ("Rock", "Paper"), ("Scissors", "Scissors")]
print(find_winner(p1_wins))
print(find_winner(p2_wins))
print(find_winner(itsatie))
