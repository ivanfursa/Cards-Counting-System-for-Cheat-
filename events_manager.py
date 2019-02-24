import random
import sys
               
class EventsManager():
    ''' Generates game events. '''
    def __init__(self, honesty):
        # Variable controlling players' tendency to lie.
        # honesty is a float with 2 digits after decimal point.
        self.honesty = honesty
        self.behavior = ''
        # Events in order.
        self.current_event = {}
        self.next_event = {}
        self.future_event = {}
        # Chance of someone would check a player.
        self.check_chance = 0.25
        self.check_field = []
        
    def initEvents(self, values, opponents,
        contents, declared_record):
        ''' Initialize events for later transformation. 
            Current event of type 'empty'.
            Next event of type 'player to pile' fully described. '''
        players = opponents + ['user']
        
        self.getBehavior()
        
    def getBehavior(self):
        ''' Generate behaviour out of honesty. Behavior defines
            whether a player passes cards it declared. '''
            
        # Check that honesty score has no more
        # than 2 digits after the decimal point.
        honest_part = int(self.honesty * 100)
        dishonest_part = int( (1-self.honesty) * 100 )
        assert honest_part + dishonest_part == 100, "Space creation fail"
        
        # Generate a list of options 'honest'/'dishonest' in a
        # proportion that respresents probability.
        honesty_space = []
        for n in range(honest_part):
            honesty_space.append("honest")
        assert len(honesty_space) == honest_part, "Space creation fail"
        for n in range(dishonest_part):
            honesty_space.append("dishonest")
        assert len(honesty_space) == 100, "Space creation fail"
        
        self.behavior = random.choice(honesty_space)
        
    def setForCheck(self, opponents, advice):
        ''' Set description for player-checks-player
            event. '''
        players = opponents + ['user']
        
    def setForCarry(self):
        ''' Set description for pile-to-player event. '''
    
    def setForTermination(self):
        ''' Set description for termination event. '''
        
    def setForPass(self, values, opponents, contents):
        ''' Set description for player-to-pile event. '''
        players = opponents + ['user']
        
        self.getBehavior()
        
        # Identify cards to pass based on last declaration.
        if len(declared_record) == 0:
            if self.behaviour == "dishonest":
                value = random.choice(values)
            elif behaviour == "honest":
                value = random.choice(contents[player])
                
        else:
            last_ind = values.index(declared_record[-1])
            # Contains 3 values: smaller, same as and greater than the last_claimed
            can_pass = []
            
            # smaller than
            if last_ind == len(card_values)-1:
                greater = values[-1]
            else:
                smaller = values[last_ind - 1]
            can_pass.append(smaller)
            # same as
            same = values[last_ind]
            can_pass.append(same)
            # greater than
            if last_ind == len(values)-1:
                greater = values[0]
            else:
                greater = values[last_ind + 1]
            can_pass.append(greater)
            
            assert len(can_pass) == 3, 'Wrong definition of can_pass'
            
            # For dishonest behaviour: the player must declare a value,
            # so that they can pass any other value but the declared one.
            if behaviour == "dishonest":
                to_pass = []
                for card in contents[player]:
                    if card not in to_pass:
                        to_pass.append(card)
                if len(to_pass) == 1 and to_pass[0] in can_pass:
                    can_pass.remove(to_pass[0])
                value = random.choice(can_pass)
                    
            # For honest behaviour: check if a hand has the right cards
            # if it doesn't, make player lie about having a proper card
            elif behaviour == "honest":
                have = []
                for card in can_pass:
                    if card in contents[player]:
                        have.append(card)
                if len(have) == 0:
                    value = random.choice(can_pass)
                elif len(have) > 0:
                    value = random.choice(have)
                
            assert value in can_pass, 'Choice error'
    
    
        # Define number of cards to pass.
        if behaviour == "dishonest":
            num = random.randint(1, min(len(contents[player]), 4))
        elif behaviour == "honest":
            # If the player has to lie (does not have proper values)
            if len(have) == 0:
                num = random.randint(1, min(len(contents[player]), 4))
            # If the player has the proper value in its hands
            elif len(have) > 0:
                value_count = 0
                for card in contents[player]:
                    if card == value:
                        value_count += 1
                assert value_count >= 1, "Couning error"
                num = random.randint(1, value_count)
        
        assert num >= 1 and num <= 4, 'Wrong num of passing cards'
        
        # Constructing 'declared' dictionary.
        declared = {}
        declared[value] = num
        
    def describeEvent(self, contents, opponents, values, advice):
        ''' Fill future event with details based on its type. '''
        if future_event['type'] == 'player checks':
            self.setForCheck(opponents, advice)
        elif future_event['type'] == 'player to pile':
            self.setForPass(values, opponents, contents)
        elif future_event['type'] == 'pile to player':
            self.setForCarry()
        elif future_event['type'] == 'termination':
            self.setForTermination()
        else:
            print("Erroe: future event unknown type")
            sys.exit(0)
            
    # ~ def choiceField(self, field, chance, main, alternative):
        # ~ ''' Creates a choice field for controlled randomization. '''
        
    def createEvent(self, contents, advice, passed_record):
        ''' Create future event based on 3 criteria (in hierarchy):
            1. What is the preceding event?
            2. Is user adviced to carry?
            3. Do all players have cards?
            The event can also be of 'termination' type. '''
        if next_event['type'] == 'player checks':
            # If the player who was checked has no cards left,
            # the game is over.
            if len(contents[next_event['won']]) == 0:
                future_event['type'] = 'termination'
            else:
                future_event['type'] = 'pile to player'

        elif next_event['type'] == 'pile to player':
            future_event['type'] = 'player to pile'
            
        elif next_event['type'] == 'player to pile':
            if advice:
                future_event['type'] = 'player checks'            
            # If the player who's passed last has no cards left.
            elif len(contents[passed_record[-1]]) == 0:
                future_event['type'] = 'player checks'
            else:
                check = 100*self.check_chance
                passing = 100*(1-self.check_chance)
                self.check_field = ( ['player to pile'] * passing +
                    ['player checks'] * checks )
                future_event['type'] = random.choice(self.check_field)
            
    def applyEvents(self):
        ''' Makes next event current and future event next. '''
        self.current_event = self.next_event
        self.next_event = self.future_event
