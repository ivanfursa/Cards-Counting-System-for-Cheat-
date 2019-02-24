
class GameSettings():
    ''' Contains properties of the game,
        which are set by a user at the start. '''
    def __init__(self):
        self.players = 0
        self.first = 0
        self.values = 0
        
    def getSettings():
        ''' Takes number of players, player who goes
        first and number of cards values
        (values themselves will be generated accordingly).
        Sets the class' arguments. '''
        
        self.player = 
        self.first =
        
        all_values = 
        self.values = 
        
        
class CalcData():
    ''' Data that is used foe chances calculations and
        honesty records. '''
    def __init__(self):
        # Cards oned by user.
        self.user = {}
        # Number of cards each other player owns.
        self.sizes = {}
        # Players in order of passing cards to pile. 
        self.passed_record = []
        # Declarations in order of passing to pile.
        self.declared_record = []
    
    # Setters and getters for the attributes.
    def updateUser(self, new_user):
        self.user = new_user
    def updateSizes(self, new_sizes):
        self.sizes = new_sizes
    def updatePassRecord(self, new_passed_record):
        self.passed_record = new_passed_record
    def emptyPassRecord(self):
        self.passed_record = []
    def updateDeclaredRecord(self, new_declared_record):
        self.declared_record = new_declared_record
    def emptyDeclaredRecord(self):
        self.declared_record = []

class GameSimulation():
    ''' Simulates game: changes contents of players'
        hands dependent on events that are generated
        by EventManager. '''
    def __init__(self):
        # Owned cards for each hand.
        self.contents = {}
    def distribDeck(self, values, players):
        ''' Generates players' hands contents in 
            a randomizes fashion. '''
        self.contents = 
    def doEvent(self, event_type):
        ''' Calls an appropriate function depending on
            the event description received '''
    def playerToPile(self, player, declared, passed):
        ''' Simulating player putting cards to pile.
            Updates contents. '''
    def playerChecks(self, checks, checked):
        ''' Simulating player checking cards put by
            another player. Updates contents. '''
    def pileToPlayer(self, lost, won):
        ''' Simulating player taling all cards from pile.
            Updates contents. '''
    def updateCalcData(self, calc_data):
        ''' Update the CalcData attributes based. '''
    def printResults(self, event_id):
        ''' Prints event description and the result
            of the event on players' hands. '''
    
    def gameContinues(self, event_id):
        ''' Checks if current event is 'termination'.
            Return false if is, return true in isnt. '''
    
class EventsManager():
    ''' Generates game events. '''
    def __init__(self, honesty):
        # Variable controlling players' tendency to lie.
        self.honesty = honesty
        # Events in order.
        self.current_event = {}
        self.next_event = {}
        self.future_event = {}
    def initEvents(self, values, players, first):
        ''' Initialize events for later transformation. '''
        
    def setForCheck(self, players):
        ''' Set description for player-checks-player
            event. '''
    def setForCarry(self):
        ''' Set description for pile-to-player event. '''
    def setForPass(self, values, players):
        ''' Set description for player-to-pile event. '''
        
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
    
    def initAttributes(self, values, players):
        ''' Initialize blank storages for states and
            chances. Updates states_reg and chance_table. '''
    def initialStates(self, user, sizes, values, players):
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
        self.recrd_file = None
    def gameInfo(self, values, players):
        ''' Append description of the game before
            registering the cases of honesty. '''
    def record(self, event_id, passed_record,
        declared_record, sizes, chance_table):
        ''' Records the game state, players involved,
            their sizes, chance of happening and 
            result: lie or truth. '''
