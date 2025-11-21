# per hour cost 0.51$ and we want find per day, per week,per month and 918$  
# 918/0.51 = x hours
perHoursCost = 0.51
per_daycost = 0.51 * 24
print("per day cost",per_daycost)
per_month = perHoursCost * per_daycost
per_week = per_daycost * 7
give_amount = 918
hours_for_given_amount = give_amount/perHoursCost
day_for_give_amount = hours_for_given_amount/24
print("Per week cost:", per_week)
print("per month cost:",per_month)
print("for the given amount the server will run for:", day_for_give_amount)