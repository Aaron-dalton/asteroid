

def get_difficulty_settings(difficulty):

    if difficulty == "easy":
        ASTEROID_SPAWN_RATE = 0.6 # seconds
        PLAYER_SHOT_COOLDOWN = 0.2
        return ASTEROID_SPAWN_RATE, PLAYER_SHOT_COOLDOWN
    
    elif difficulty == "medium":
        ASTEROID_SPAWN_RATE = 0.4
        PLAYER_SHOT_COOLDOWN = 0.2
        return ASTEROID_SPAWN_RATE, PLAYER_SHOT_COOLDOWN

    elif difficulty == "hard":
        ASTEROID_SPAWN_RATE = 0.1 # seconds
        PLAYER_SHOT_COOLDOWN = 0.2
        return ASTEROID_SPAWN_RATE, PLAYER_SHOT_COOLDOWN

    else:
        raise ValueError("Invalid difficulty level")