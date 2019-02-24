import random

class GameSettings():
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
        
        
class CalcData():
    ''' Data that is used foe chances calculations and
        honesty records. '''
    def __init__(self):
        # Cards oned by user.
        self.user = {}
        # Number of cards each opponent owns.
        self.sizes = {}
        # Players in order of passing cards to pile. 
        self.passed_record = []
        # Declarations in order of passing to pile.
        self.declared_record = []
    
    def createInitial(self, values, opponents):
        ''' Gives all the attributes blank initial form. '''
        for value in values:
            self.user[value] = 0
        for opponent in opponents:
            self.sizes[opponent] = 0
            

class GameSimulation():
    ''' Simulates game: changes contents of players'
        hands dependent on events that are generated
        by EventManager. '''
    def __init__(self):
        # Owned cards for each hand.
        self.contents = {}
        
    def distribDeck(self, values, opponents):
        ''' Generates players' and pile's cards in 
            a randomizes fashion. '''
                
        # Get a shuffled deck.
        deck = values * 4
        random.shuffle(deck)
        
        # Create a list for each player, user and pile.
        for opponent in opponents:
            self.contents[opponent] = []
        self.contents['user'] = []
        self.contents['pile'] = []
        assert (len(self.contents) == len(opponents)+2,
            "Initialization fail")
    
        # Hand-out the cards to all players.
        players = opponents + ['user']
        random.shuffle(players)
        c = 0
        while c < len(deck):
            for player in players:
                if c < len(deck):
                    self.contents[player].append(deck[c])
                    c += 1
                else:
                    break
    
        # Check if distribution is successful.
        all_cards = 0
        for cards in contents.values():
            all_cards += cards
        assert ( sorted(all_cards) = sorted(deck), 
            'Deck distribution fail' )
 
        
    def doEvent(self, event_id):
        ''' Calls an appropriate function depending on
            the event description received '''
        assert 'type' in event_id
        
        if event_id['type'] == 'player to pile':
            self.playerToPile()
            
        elif event_id['type'] == 'player checks':
            pass
            
        elif event_id['type'] == 'pile to player':
            self.pileToPlayer()
            
        elif event_id['type'] == 'termination':
            print('Error in doEvent(): \
                Accepting "termination" event')
            sys.exit()
            
        else:
            print('Error in doEvent(): Invalid event type')
            sys.exit()
        
    # Action for each game event (except termination).
    def playerToPile(self, player, passed):
        ''' Simulating player putting cards to pile.
            Updates contents. '''
        for card in passed:
            self.contents[player].remove(card)
            self.contents['pile'].append(card)
    
    def pileToPlayer(self, lost):
        ''' Simulating player taling all cards from pile.
            Updates contents. '''
        for card in self.contents['pile']:
            self.contents[lost].append(card)
        
    def updateCalcData(self, calc_data):
        ''' Update the CalcData attributes based. '''
        calc_data.user = {}
        calc_data.sizes = {}
        self.passed_record = []
        self.declared_record = []
        
    def printResults(self, event_id):
        ''' Prints event description and the result
            of the event on players' hands. '''
        print('After', event_id, ':')
        for element in self.contents.keys():
            if element != 'user' or element != 'pile':
                pass
            else:
                print('opponent', end=' ')
            print(element, self.contents[element])
    
    def gameContinues(self, event_id):
        ''' Checks if current event is 'termination'.
            Return false if is, return true in isnt. '''
        if event_id['type'] == 'termination':
            return False
        else:
            return True
    
class EventsManager():
    ''' Generates game events. '''
    def __init__(self, honesty):
        # Variable controlling players' tendency to lie.
        self.honesty = honesty
        # Events in order.
        self.current_event = {}
        self.next_event = {}
        self.future_event = {}
        
    def initEvents(self, values, opponents, first):
        ''' Initialize events for later transformation. '''
        players = opponents + ['user']
        
    def setForCheck(self, opponents):
        ''' Set description for player-checks-player
            event. '''
        players = opponents + ['user']
        
    def setForCarry(self):
        ''' Set description for pile-to-player event. '''
        
    def setForPass(self, values, opponents):
        ''' Set description for player-to-pile event. '''
        players = opponents + ['user']
        
    def describeEvent(self):
        ''' Fill future event with details. '''
    def createEvent(self, contents, advice):
        ''' Create future event. The event can also be of 
            'termination' type. '''
    def applyEvents(self):
        ''' Makes next event current and future event next. '''
        
    
    
class ChancesTrack():
    ''' Calculates chances for each player to have
        1, 2, 3, and 4 cards of each value. 
        For this, all possible states of the game
        are accounted for.
        Also sends advies signal for user to check
        passing of a player based on plausibility. '''
    def __init__(self, advice_threshold):
        # Possible states of the game. Each consists of ..
        self.states_reg = {}
        # Chances for each player for each set of cards.
        self.chance_table = {}
        # Controls when user is advised to check passing.
        self.advice_threshold = 0
        # Advice to carry.
        self.advice = False
    
    def initAttributes(self, values, opponents):
        ''' Initialize blank storages for states and
            chances. Updates states_reg and chance_table. '''
    def initialStates(self, user, sizes, values, opponents):
        ''' Get the initial game states.
            Updates states register. '''
    
    def calcForEvent(self, event_id):
        ''' Identifies which kind of calculations for
            states to produce. '''
        stateSplit()
        pileToUser()
        carryHint()
        foundLie()
        userToPile()
        
        normalizeStates()
        mergeStates()
        
        updateChanceTable()
        
    def stateSplit(self, user, sizes, values):
        ''' Get child states from a state.
            Updates states register. '''
    def pileToUser(self):
        ''' Update all game states based on passing
            of user to pile. Updates states register. '''
    def carryHint(self):
        ''' Remove unprobable states based on a hint
            from a pile-to-player game event.
            Updates states register. '''
    def foundLie(self):
        ''' Remove unprobable states of game based
            on a hint from user checking player.
            Updates states register. '''
    def userToPile(self, pass_record):
        ''' Remove unprobable states of game based
            on contents of pile and pass-to-pile
            records. Updates states register. '''
            
    def normalizeStates(self):
        ''' Normalize chances of the game states after
            removal of some. Updates states register. '''
    def mergeStates(self):
        ''' Merge the same game states into one with
            a combined chance. Updates states register. '''
    
    def updateChanceTable(self):
        ''' Updating chance table based on game
            states chances. '''
            
    def carryAdvice(self, event_id):
        ''' Based on the chance-threshold, 
            decides whether user is advised to check
            passed cards. Updates advice. '''
            
class HonestyRecord():
    ''' Records data about instances where 
        players lie and tell truth. '''
    def __init__(self):
        self.record_file = ''
        self.passed_record = []
        self.declared_record = []
        
    def gameInfo(self, values, opponents):
        ''' Append description of the game before
            registering the cases of honesty. '''
        # IN PROGRESS
        info = '\nNew game \n' 
        info += 'Number of opponents: ' + str(len(opponents)) + '\n'
        info += 'Number of values: ' + str(len(values)) + '\n'
        with open(self.record_file, 'a') as record:
            record.write(info)
            
    def record(self, event_id, passed_record,
        declared_record, sizes, chance_table):
        ''' Records the game state, players involved,
            their sizes, chance of happening and 
            result: lie or truth. '''
        # IN PROGRESS
        if event_id['type'] == 'player checks player':
            self.passed_record = passed_record.copy()
            self.declared_record = declared_record.copy()
            
        elif event_id['type'] == 'pile to player':
            if event_id['lost'] == 'user':
                
            else:
                self.declared_record[-1]
            
        
        
