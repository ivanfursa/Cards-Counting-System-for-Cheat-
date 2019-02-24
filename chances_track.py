import states_init as init
import chance_calc as calc

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
    
    def initAttributes(self, values, sizes, opponents, user):
        ''' Initialize blank storages for states and
            chances. Updates states_reg and chance_table. '''
        # Creating chances register (in a format of minimum ownership.
        self.chance_table = {}
        for opponent in opponents:
            chances_for_hand = {}
            for value in values:
                chances_for_qty = {}
                for qty in range(1, 4+1):
                    chances_for_qty[str(qty)] = 0
                chances_for_hand[value] = chances_for_qty
            self.chance_table[opponent] = chances_for_hand
                
    def initialStates(self, user, sizes, values, opponents):
        ''' Get the initial game states.
            Updates states register. '''
        # Creating game states register for every value.
        self.states_to_value = init.init_states(user, values, sizes)
        
    def calcForEvent(self, event, user, values, passed_record):
        ''' Identifies which kind of calculations for
            states to produce. '''
        if event['type'] == 'player to pile':
            if event['player'] == 'user':
                self.userToPile(event['declared'])
            else:
                self.stateSplit(user, sizes[event['player']], values, event['declared'])
        elif event['type'] == 'pile to player':
            if event['lost'] == 'user':
                self.pileToUser()
            elif event['won'] == 'user':
                self.foundLie()
            elif event['won'] == passed_record[-1]
                self.carryHint()
            else:
                self.pileToPlayer()
        self.normalizeStates()
        self.mergeStates()
        self.updateChanceTable()
    
    def new_scenario(old_scenario, chance, hand, passed, stayed, value, card_values):
        ''' FIX IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! '''
        # Creating a scenario template (IF DICTIONARY).
        scenario = {}
        scenario['chance'] = chance
        for ind in range(1, len(table)-1):
            if ind == hand:
                scenario[str(ind)] = stayed
            else:
                scenario[str(ind)] = old_scenario[str(ind)]
        scenario['pile'] = old_scenario['pile']
        scenario['pile history'] = old_scenario['pile history']
        # Pile is a list of values passed to it each turn of a scenario.
        scenario['pile'].append(passed)
        scenario['pile history'].append(hand)
        
        return scenario
    
    def stateSplit(self, user, size, values, declared):
        ''' Get child states from a state.
            Updates states register. 
            
            FIX IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
            
        # Find a state to split. split it.
        num_owns = state[str(hand)]
        size = len(table[hand])
        
        scenarios = []
        
        if num_owns < qty_passing:
            # impossible scenario
            return scenarios
            
        # Calculate the chances for each possible qty to pass
        else:
            for passing in range(num_owns+1):
                chance = calc.get_chance(size, qty_passing, num_owns, passing) * scenario['chance']
                new_scen = new_scenario(scenario, chance, hand, passing, num_owned-passed, value, card_values)
                scenarios.append(new_scen)
        
        return scenarios
        
    def pileToUser(self):
        ''' Update all game states based on passing
            of user to pile. Updates states register.
            FIX IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
        for turn in range(len(received)):
            
            for value, qty in received[turn]:
                scenes_c = scenes_to_value[value].copy()
                for scenario in scenes_c:
                    assert len(received) == len(scenario['pile'])
                    if scenario['pile'][turn] != qty:
                        scenes_to_value[value].remove(scenario)
        
        return scenes_to_value
        
    def carryHint(self):
        ''' Remove unprobable states based on a hint
            from a pile-to-player game event.
            Updates states register. 
            FIX IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
        for value, qty in passed:
            scenes_c = scenes_to_value[value].copy()
            for scenario in scenes_c:
                if scenario['pile'][-1] != qty:
                    scenes_to_value[value].remove(scenario)
        
        return scenes_to_value
        
    def foundLie(self):
        ''' Remove unprobable states of game based
            on a hint from user checking player.
            Updates states register. 
            FIX IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! '''
        for value, qty in passed:
            scenes_c = scenes_to_value[value].copy()
            for scenario in scenes_c:
                if scenario['pile'][-1] != qty:
                    scenes_to_value[value].remove(scenario)
        
        return scenes_to_value
            
    def userToPile(self, declared):
        ''' Updates states register. 
            FIX IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
        
        qty = len(passed)
        value = passed[0]
        
        for scenario in scenes_to_value[value]:
            scenario['pile'].append(qty)
            scenario['pile history'].append('user')
        
        values_c = card_values.copy()
        values_c.remove(value)
        for value_ in values_c:
            for scenario in scenes_to_value[value_]:
                scenario['pile'].append(0)
                scenario['pile history'].append('user')
        return scenes_to_value
    
    def pileToPlayer(table, value, scenario, hand, qty_passing, card_values):
        ''' Given a scenario, cleans a pile, by passing all the cards of the value
            to a specific hand. DO SIZES GET UPDATED?
            Returns a modified scenario.
            FIX IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
        assert len(scenario['pile history']) == len(scenario['pile'])
        
        for hand in scenario['pile history']:
            scenario[str(hand)] += scenario['pile'][0]
            del scenario['pile'][0]
        scenario['pile history'] = []
        
        assert len(scenario['pile']) == 0
        
        return scenario
        
    def normalizeStates(self):
        ''' Normalize chances of the game states after
            removal of some. Updates states register. '''
        for states in self.states_to_value.values():
            assert len(states) != 0
            
            chances_sum = 0
            for state in states:
                chances_sum += state['chance']
            assert chances_sum <= 1
            
            if chances_sum != 1:
                for state in states:
                    old_chance = state['chance']
                    new_chance = old_chance / chances_sum
                    assert old_chance < new_chance
                    state['chance'] = round(new_chance, 5)
        return self.states_to_value
        
    def mergeStates(self):
        ''' Merge the same game states into one with
            a combined chance. Updates states register. '''
        for states in self.states_to_value.values():
            states_c = states.copy()
            for state in states_c:
                del states_c['chances']
            length = len(states_c)
            
            for ind in range(length):
                for ind2 in range(length-ind):
                    if states_c[ind] == states_c[ind2]:
                        states[ind]['chance'] += states[ind2]['chance']
                        del states[ind2]
        return self.states_to_values
        
    def updateChanceTable(self):
        ''' Updating chance table based on game
            states chances. '''
        # First, complete the chance table for having exactly n cards.
        for value, states in self.states_to_value.items():
            for state in states:
                for opponent in self.chance_table.keys():
                    qty = state[opponent]
                    if qty != 0:
                        chance_table[opponent][value][qty] += state['chance']
        
        # Second, turn into having n+ format.
        for opponent in chance_table.keys():
            for value in chance_table[opponent].keys():
                chances_c = self.chance_table[opponent][value].copy()
                for qty, chance in self.chance_table[opponent][value].items():
                    chances_c[qty] = 0
                    for i in range(1, int(qty)):
                        chances_c[qty] += chance
        
        return self.chance_table
        
    def carryAdvice(self, event):
        ''' Based on the chance-threshold, 
            decides whether user is advised to check
            passed cards. Updates advice. '''
        if event['type'] == 'player to pile':
            player = event['player']
            value = list(event['declared'].keys())[0]
            qty = list(event['declared'].values())[0]
            chance = self.chance_table[player][value][qty]
            if chance < self.advise_threshold:
                self.advice = True
            else:
                self.advice = False
