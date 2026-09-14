#%%
# turn american odds into implied probability (p)
def american_to_implied_probability(odds):
    if odds == 0:
        raise ValueError("Odds equal to 0 are not valid")
    elif odds < 0:
        return abs(odds) / (abs(odds) + 100)
    else:
        return 100 / (odds + 100)
    
print(american_to_implied_probability(-110))

# %%
print(american_to_implied_probability(-110))
print(american_to_implied_probability(-110))
print(american_to_implied_probability(-110) + american_to_implied_probability(-110))
# %%
raw_over = american_to_implied_probability(-150)
raw_under = american_to_implied_probability(+130)
overround = raw_over + raw_under
devig_over = raw_over / overround
devig_under = raw_under / overround

print(raw_over)
print(raw_under)
print(overround)
print(devig_over)
print(devig_under)
