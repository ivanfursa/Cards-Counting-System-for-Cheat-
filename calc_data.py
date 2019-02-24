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
