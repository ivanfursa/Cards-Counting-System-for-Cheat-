lass GameSettings():
    ''' Contains properties of the game,
        which are set by a user at the start. '''
    def __init__(self):
        self.opponents = []
        self.first = ''
        self.values = []
        
    def getSettings():
        ''' Takes number of opponents, player who goes
        first and number of card values
        (values themselves will be generated accordingly).
        Sets the class' arguments. '''
        
        # Get number of opponents.
        opponents_num = None
        while type(opponents_num) != int:
            try:
                opponents_num = int(input("Type-in the number of players (2-52): "))
            except ValueError:
                print("Input integers only\n")
        
        if type(opponents_num) == int and (opponents_num+1 < 2 or opponents_num+1 > 13):
            print("Number of players out of range\n")
            oponents_num = get_number_of_players()
            
        print("")
        
        # Get list of opponents.
        for opponent in range(1, opponents_num+1):
            self.opponents.append(str(opponent))
    
        # Get card values. 
        all_values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        print("Type-in the number of card values possible in this game. \
            \nEx.\tif you type '2' (min), possible cards values are 2 and 3 \
            \n\tif you type '13' (max), cards values are from 2 to A. \
            \nIn this game, a standard 52-cards deck is used: \
            \ni.e. no Jokers, possible values are from 2 to A. \
            \nA minimum number you can input depends on a number of players.")
        
        values_num = None
        while type(values_num) != int:
            try:
                values_num = int(input("Number of possible card values: "))
            except ValueError:
                print("Input integers only\n")
            if type(num_values) == int:
                if values_num*4 < opponents_num+1:
                    print("Too few card values for the game with that many players\n")
                    values_num = None
                elif values_num < 2 or values_num > 13:
                    print("Number out of range (2-13)\n")
                    num_values = None
        
        self.values = all_values[:values_num]
        
        # Get first player to pass.
        self.first = input("Who goes first? \
            ('user' for user, number for an opponent's index): ")
        while (self.first != 'user' and
            self.first not in self.opponents):
            self.first = input("Wrong input. Enter again: ") 
