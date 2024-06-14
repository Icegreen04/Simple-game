class Warrior:
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.attack = 0
        self.defense = 0
        self.health = 0
        self.medicine = 0
        self.playstate = 0
        self.choice = "default"
        self.match_status = "default"
        self.stats_init()
        
    def stats_init(self):
        if self.type == 'warrior':
            self.attack = 6
            self.defense = 1
            self.health = 12
            self.medicine = 1
        
        elif self.type == 'defender':
            self.attack = 3
            self.defense = 6
            self.health = 14
            self.medicine = 1
            
        else:
            self.attack = 2
            self.defense = 2
            self.health = 14
            self.medicine = 3
        
        print("Here are your stats: ")
        print(self.name, ": ", self.type)
        print("Health: ", self.health)
        print("Attack: ", self.attack)
        print("Defense: ", self.defense)
        print("Amount of medicine available: ", self.medicine)
        
    def make_choice(self):
        global game_state
        if self.choice == "attack":
            
            if player1.playstate == 1:
                health_loss = player1.attack - player2.defense / 2
                if health_loss<0:
                    health_loss=0.5
                player2.health = player2.health - health_loss
                player1.playstate = 0
                player2.playstate = 1
                self.choice="default"
                
                if player2.health <= 0:
                    game_state = 0
                    player1.match_status = "winner"
                    player2.match_status = "loser"
                else:
                    print(player2.name, " survives! It is ", player2.name, "'s turn")
            
            else:
                health_loss = player2.attack - player1.defense / 2
                if health_loss<0:
                    health_loss=0.5
                player1.health = player1.health - health_loss
                player1.playstate = 1
                player2.playstate = 0
                self.choice="default"
                
                if player1.health <= 0:
                    game_state = 0
                    player1.match_status = "loser"
                    player2.match_status = "winner"
                
                else:
                    print(player1.name, " survives! It is ", player1.name, "'s turn")
        
        elif self.choice == "heal":
            if player1.playstate == 1:
                if player1.medicine == 0:
                    print("You have no medicine!!! You are forced to attack")
                    player1.choice = "attack"
                    player1.make_choice()
                else:
                    player1.medicine = player1.medicine - 1
                    player1.health = player1.health + 7
                    player1.playstate = 0
                    player2.playstate = 1
                    self.choice="default"
            else:
                if player2.medicine == 0:
                    print("You have no medicine!!! You are forced to attack")
                    player2.choice = "attack"
                    player2.make_choice()
                else:
                    player2.medicine = player2.medicine - 1
                    player2.health = player2.health + 7
                    player1.playstate = 1
                    player2.playstate = 0
                    self.choice="default"


# Initialize players
player1 = Warrior(input("Player1, please give your name: "), input("Player1, please give your type: "))
player2 = Warrior(input("Player2, please give your name: "), input("Player2, please give your type: "))

# Set game state
global game_state
game_state = 1

print("Player1 starts!")   
player1.playstate = 1
player2.playstate = 0

while game_state == 1:
    print("\nSTATS ARE: ")
    print(player1.name, ": ", player1.health, "HP")
    print("Attack: ", player1.attack, "  Defense: ", player1.defense, "   Medicine available: ", player1.medicine)
    print("")
    print(player2.name, ": ", player2.health, "HP")
    print("Attack: ", player2.attack, "  Defense: ", player2.defense, "   Medicine available: ", player2.medicine)
    
    if player1.playstate == 1:
        print("\n", player1.name)
        player1.choice = input("What will you do this turn, attack or heal: ").strip().lower()
        player1.make_choice()
    
    else:
        print("\n", player2.name)
        player2.choice = input("What will you do this turn, attack or heal: ").strip().lower()
        player2.make_choice()

if player1.match_status == "winner":
    print(player1.name, " WINS!!! ", player2.name, " is dead!")
else:
    print(player2.name, " WINS!!! ", player1.name, " is dead!")

print("\nFINAL STATS: ")
print(player1.name, ": ", player1.health, "HP")
print("Attack: ", player1.attack, "  Defense: ", player1.defense, "   Medicine available: ", player1.medicine)
print("")
print(player2.name, ": ", player2.health, "HP")
print("Attack: ", player2.attack, "  Defense: ", player2.defense, "   Medicine available: ", player2.medicine)
