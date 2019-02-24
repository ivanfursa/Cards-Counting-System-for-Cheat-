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
