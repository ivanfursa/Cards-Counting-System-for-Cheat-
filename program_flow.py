from classes import (GameSettings, CalcData, GameSimulation,
    EventsManager, ChancesTrack, HonestyRecord)

# Create objects.
settings = GameSettings()
calc_data = CalcData(advice_threshold)
game = GameSimulation()
events_manager = EventsManager(honesty)
chances = ChancesTrack()
honesty_rec = HonestyRecord()

# Initialization of all variables (Preparation).
settings.getSettings()
calc_data.createInitial(settings.values, settings.players)
game.distribDeck(settings.values, settings.players)
game.updateCalcData(calc_data)
events_manager.initEvents(settings.values, settings.players,
    settings.first)
chances.initAttributes(settings.values, settings.players)
chances.initialStates(calc_data.user, calc_user.sizes, 
    settings.values, settings.players)
honesty_rec.gameInfo(settings.values, settings.players)

# Game Loop.
while game.gameContinues(events_manager.current_event):
    # Generate event.
    events_manager.createEvent(events.contents, chances.advice)
    events_manager.describeEvent()
    events_manager.applyEvents()
    
    # Simulate event.
    game.doEvent(events_manager.current_event)
    game.updateCalcData(calc_data)
    game.printResults(events_manager.current_event)
    
    # Calculate chances.
    chances.calcForEvent(events_manager.current_event)
    chances.carryAdvice(events_manager.current_event)
    
    # Record Honesty.
    honesty_rec.record(events_manager.current_event, 
        calc_data.passed_record, calc_data.declared_record,
        calc_data.sizes, chances.chance_table)

# Print winner / loser.
game.printResults(events_manager.current_event)
    
    
