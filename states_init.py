import chance_calc as calc

def scenarios_by_qty(sizes, range_max, hands_num, hand_ind=0):
    ''' Get all the dictionary options for initial qties of 
        values that hands might have on them.
        Chances will be counted by another function.
        
        Scenarios is a list of dictionaries that are being filled in. '''
        
    hand_ind += 1
    if hand_ind != hands_num:
        range_max_c = range_max
        scenarios = []
        
        for i in range( min(sizes[str(hand_ind)]+1, range_max+1) ):
            range_max = range_max_c - i
            
            scenarios_a = scenarios_by_qty(sizes, range_max, hands_num, hand_ind)
            for scenario in scenarios_a:
                scenario[str(hand_ind)] = i
            scenarios += scenarios_a
        
        return scenarios
                
    elif hand_ind == hands_num:
        scenario = {}
        scenario[str(hand_ind)] = range_max
        
        return [scenario]

def add_chances(scenarios, sizes, total_in_deck):
    ''' Associate a chance to each of the scenario
        (adds a new key 'chance' to each dictionary and calculates a value for it)
        Returns a list of updated dictionaries. '''
        
    total_cards = 0
    for qty in sizes.values():
        total_cards += qty
    
    total_combos = calc.calc_combo(total_cards, total_in_deck)
    
    summ = 0
    for scenario in scenarios:
        combos = 1
        for hand, qty in scenario.items():
            combo = calc.calc_combo(sizes[hand], qty)
            combos *= combo
        chance = combos/total_combos
        summ += chance
        
        scenario['chance'] = round(chance, 5)
        
    assert round(summ) == 1
    return scenarios

def add_pile(scenarios):
    ''' Adds pile-related keys to every scenario: 'pile' and 'pile history' '''
    for scenario in scenarios:
        scenario['pile'] = []
        scenario['pile history'] = []
    return scenarios

def init_states(user, card_values, sizes):
    ''' Creates initial lists of scenarios for all values depending on
        user's contents, card values used in the game and hands' sizes. 
        Returns a complete scenes_to_value
        (a dictionary where key is a card value and value is a list of scenarios). 
    '''
    scenes_to_value = {}
    for value in card_values:
        cards_of_value = 4 - user[value]
        hands_num = len(sizes)
        scenarios = scenarios_by_qty(sizes, cards_of_value, hands_num)
        scenarios = add_chances(scenarios, sizes, cards_of_value)
        scenarios = add_pile(scenarios)
        
        scenes_to_value[value] = scenarios
    
    return scenes_to_value

# ~ card_values = ['J', 'Q', 'K', 'A']
# ~ user = {'J':1, 'Q':2, 'K':0, 'A':1}
# ~ sizes = {'1':3, '2':4, '3':5}

# ~ scenes_to_value = init_scenarios(user, card_values, sizes)
# ~ for value in card_values:
    # ~ print("")
    # ~ for scenario in scenes_to_value[value]:
        # ~ print(scenario)
        

