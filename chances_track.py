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
