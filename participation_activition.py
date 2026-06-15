# This program makes sandwiches from a list of orders
# moves them to finished list
# Jonathan Dotse, 06/13/2026

# Defining values

sandwich_orders = ['Reuben', 'Cheesesteak', 'Melt', 'Panini', 'Clubmarine', 'Croque Monsieur']
finished_sandwihes = []

# Initializing the loop
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwihes.append(current_sandwich)

print("\nThe finished sandwiches are:")
for sandwich in finished_sandwihes:
    print(sandwich)
