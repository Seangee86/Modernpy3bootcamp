print("How many kilometers did you run today?")
kms = input() # Ask user for an input
miles = float(kms)/1.60934 # So user can be more accurate. EXP 45.87 instead of just 45 then divides by 1.06
miles = round(miles,2) # rounds the number and only shows 2 decimals
print(f"That equals to {miles} miles") # Prints out to miles
