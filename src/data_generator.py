import numpy as np
import pandas as pd


#create rng for use
rng = np.random.default_rng()

#create 1000 values from 0.48 to 0.58
true_win_prob = rng.uniform(low = 0.48, high = 0.58, size = 1000)

#add (noise) sportsbook mispricing 4%
noise = rng.normal(loc = 0.0, scale = 0.04, size = 1000)

#raw sportsbook line before vig
p_book_raw = true_win_prob + noise

#allow conservative vig (4%)
p_over = np.clip(p_book_raw + 0.02, 0, 1.0)
p_under = np.clip((1 - p_book_raw) + 0.02, 0, 1.0)

#converts probability (p) to standard american odds
def prob_to_american(p): 
    if p >= 0.5:
        odds = -(p / (1 - p)) * 100
    else:
       odds = ((1 - p) / p) * 100
    return int(round(odds))

#convert adjusted win prob to standard american sportsbook odds 
dk_over_odds = [prob_to_american(p) for p in p_over]
dk_under_odds = [prob_to_american(p) for p in p_under]

#generate list to see if players are eligible for promo
prop_promo = rng.uniform(low = 0.0, high = 1.0, size = 1000)
is_promo_eligible = prop_promo >= 0.85

#create prop_ids and player names
prop_ids = [f"PROP_{i+1:04d}" for i in range(1000)]
player_names = [f"Player_{i+1}" for i in range(1000)]

# generate dataframe of players and potential promos
data = {
    'prop_id': prop_ids,
    'player_name': player_names,
    'p_true_over': np.round(true_win_prob,4),
    'dk_over_odds': dk_over_odds,
    'dk_under_odds': dk_under_odds,
    'is_promo_eligible': is_promo_eligible
}

#create df and print
df = pd.DataFrame(data)
#print(df.head())

#function that changes American odds into decimal probability
def american_to_decimal_odds(american_odds: int) -> float:
    if american_odds > 0:
        decimal_odds = (american_odds / 100) + 1
    else:
        decimal_odds = (100 / np.abs(american_odds)) + 1
    return decimal_odds

#add new column of american odds
df["dk_decimal_odds"] = [american_to_decimal_odds(x) for x in df["dk_over_odds"]]
df["dk_implied_prob"] = np.round(1 / df["dk_decimal_odds"], 4)

#calculate edge
df["edge"] = np.round(df["p_true_over"] - df["dk_implied_prob"],4)

#calculate ev
df["ev_pct"] = np.round(df["p_true_over"] * (df["dk_decimal_odds"]) - 1,4)

#calculate kelly 
def calculate_kelly(decimal_odds: float, p_true: float, factor: float = 0.5) -> float:
    b = decimal_odds - 1
    ev = (p_true * decimal_odds) - 1.0
    
    if ev <= 0 or b <= 0:
        return 0.0
    
    f_star= ((b * p_true) - (1 - p_true)) / b
    
    return max(0.0, round(f_star * factor,4))

#add kelly to df 
df["kelly_wager_pct"] = [calculate_kelly(d, p) for d,p in zip(df["dk_decimal_odds"], df["p_true_over"])]

#view best bets
print(df.sort_values(by="ev_pct", ascending = False).head())

df.to_csv("data/synthetic_props.csv", index=False)