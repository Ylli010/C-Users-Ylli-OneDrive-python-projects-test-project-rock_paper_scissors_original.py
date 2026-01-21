player1= input("Enter your choice player1.")
while player1 !="rock" and player1 != "scissor" and player1 != "paper":
    player1 = input("Enter your choice player1.")

player2= input("Enter your choice player2.")
while player2 !="rock" and player2 != "scissor" and player2 != "paper":
    player2 = input("Enter your choice player2.")
    
if player1=="rock":
    if player2=="rock":
        print("tie")
    elif player2== "scissor":
        print ("Player1 Won.")
    elif player2== "paper":
        print ("Player2 won.")
    

if player1=="scissor":
    if player2=="scissor":
        print("tie")
    elif player2== "paper":
        print ("Player1 Won.")
    elif player2== "rock":
        print ("Player2 won.")
    
        

if player1=="paper":
    if player2=="paper":
        print("tie")
    elif player2== "rock":
        print ("Player1 Won.")
    elif player2== "scissor":
        print ("Player2 won.")
  
        
