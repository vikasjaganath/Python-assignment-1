employees = {}
while True:
    name = input("Enter employee name(type 'stop' to finish):").strip()
    if name.lower() == "stop":
        break
    try:
        basic = float(input(f"Enter basic salary for {name}:"))
        if basic < 0:
            print("salary cannot be negative. try again.")
            continue

    expcet ValueError:
          print("Invalid input.please enter a number .")
          continue 
    hra = 0.20*basic
    da = 0.10*basic
    total_salary = basic + hra + da
    employees[name] = toatal_salary
    print("\n--- Employee total salary Details---")
    for name,total in employees.items():
        print(F"{name}:Rs{total : 2f}")
    
