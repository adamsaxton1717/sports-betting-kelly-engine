import numpy as np
import pandas as pd


#create rng for use
rng = np.random.default_rng()

#create 1000 values from 0.48 to 0.58
true_win_prob = rng.uniform(low = 0.48, high = 0.58, size = 1000)

#allow conservative vig (4%)
p_over = true_win_prob + 0.02
p_under = (1 - true_win_prob) + 0.02

#converts probability (p) to standard american odds
def prop_to_american(p): 
    if p >= 0.5:
        odds = -(p / (1 - p)) * 100
    else:
       odds = ((1 - p) / p) * 100
    return int(round(odds))

#convert adjusted win prob to standard american sportsbook odds 
dk_over_odds = [prop_to_american(p) for p in p_over]
dk_under_odds = [prop_to_american(p) for p in p_under]

#generate list to see if players are eligible for promo
prob_promo = rng.uniform(low = 0.0, high = 1.0, size = 1000)
is_promo_eligible = prob_promo >= 0.85


# generate dataframe of players and potential promos
data = {
    'prob_id':,
    'player_name':,
    'p_true_over': round(true_win_prob,4),
    'dk_over_odds': dk_over_odds,
    'dk_under_odds': dk_under_odds,
    'is_promo_eligible': is_promo_eligible
}

df = print(df.head())