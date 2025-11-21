perHoursCost = 0.51
per_daycost = perHoursCost * 24
per_month = perHoursCost * per_daycost
per_week = per_daycost * 7
give_amount = 918
hours_for_given_amount = give_amount/perHoursCost
day_for_give_amount = hours_for_given_amount / 24

print("Per week cost:", per_week)
print("per month cost:",per_month)
print("per day cost",per_daycost)
print("for the given amount the server will run for:", day_for_give_amount)
