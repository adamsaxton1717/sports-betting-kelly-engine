import pandas as pd 
from payouts import get_payout_prizepicks
from data_generator import calculate_slip_ev

#read in csv file
df = pd.read_csv(data/synthetic_props.csv)

#find 3 best player props from data set
top_3_props = df.sort_values(by = "ev_pct", ascending = False).head(3)

#create list of the best 3 player props
leg_probs = top_3_props["p_true_over"].tolist()

#get 3 leg parlay payout structure 
payout_map = get_payout_prizepicks(n_legs = 3, strategy = "flex")

#calculate slip ev
result = calculate_slip_ev(leg_probs, payout_map)