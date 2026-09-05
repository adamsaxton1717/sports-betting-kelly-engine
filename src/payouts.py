
# Prizepicks Payout Maps
# Key: (n_legs, strategy_type) -> Value: {num_hits: payout_multiplier}

PRIZEPICKS_PAYOUT_MAPS = {
    # Power Plays (Must hit all picks)
    (6, "power"): {6: 37.5, 5: 0.0, 4: 0.0, 3: 0.0, 2: 0.0, 1: 0.0, 0: 0.0},
    (5, "power"): {5: 20.0, 4: 0.0, 3: 0.0, 2: 0.0, 1: 0.0, 0: 0.0},
    (4, "power"): {4: 10.0, 3: 0.0, 2: 0.0, 1: 0.0, 0: 0.0},
    (3, "power"): {3: 6.0, 2: 0.0, 1: 0.0, 0: 0.0},
    (2, "power"): {2: 3.0, 1: 0.0, 0: 0.0},

    # Flex Plays (Tiered payouts)
    (6, "flex"): {6: 25.0, 5: 2.0, 4: 0.4, 3: 0.0, 2: 0.0, 1: 0.0, 0: 0.0},
    (5, "flex"): {5: 10.0, 4: 2.0, 3: 0.4, 2: 0.0, 1: 0.0, 0: 0.0},
    (4, "flex"): {4: 6.0, 3: 1.5, 2: 0.0, 1: 0.0, 0: 0.0},
    (3, "flex"): {3: 3.0, 2: 1.0, 1: 0.0, 0: 0.0},
    (2, "flex"): {2: 2.0, 1: 0.5, 0: 0.0},
}

#function that returns all possible outcomes of a specific bet
def get_payout_prizepicks(n_legs: int, strategy: str = "flex") -> dict:
    """Returns the hit-to-multiplier mapping for a given entry type."""
    return PRIZEPICKS_PAYOUT_MAPS.get((n_legs, strategy.lower()), {})

