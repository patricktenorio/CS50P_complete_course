# Coke amount in cents
balance = 50

# Loop until statement is True
while balance > 0:
    # Show the balance amount
    print(f"Amount due: {balance}")
    # Prompts the user to insert a coin until True
    coin_inserted = int(input("Insert Coin: "))

    # Check if input is in this list
    if coin_inserted in [5, 10, 25]:
        # deduct the amount of coin inserted
        balance -= coin_inserted

# updated balance as our change in Absolute value
change = abs(balance)
# Output the change owed
print(f"Change owed: {change}")