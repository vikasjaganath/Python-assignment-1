def process_purchase_file(filename):
    items = []     # list to store purchased items
    prices = []    # list to store item prices
    free_items = 0

    # Read file
    with open(filename, "r") as f:
        for line in f:
            if line.strip():  # skip empty lines
                parts = line.split()
                item_name = " ".join(parts[:-1])
                price = int(parts[-1])
                
                items.append(item_name)
                prices.append(price)

                if price == 0:
                    free_items += 1

    # Calculations
    total_items = len(items)
    amount_to_pay = sum(prices)
    discount = free_items * 40   # Example: each free item = Rs.40 discount
    final_amount = amount_to_pay - discount

    # Display results
    print(f"File: {filename}")
    print(f"No of items purchased: {total_items}")
    print(f"No of free items: {free_items}")
    print(f"Amount to pay: {amount_to_pay}")
    print(f"Discount given: {discount}")
    print(f"Final amount paid: {final_amount}")
    print("-" * 40)


# Test on both files
process_purchase_file("purchase-1.txt")
process_purchase_file("purchase-2.txt")