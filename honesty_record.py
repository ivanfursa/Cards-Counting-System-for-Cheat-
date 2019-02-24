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
