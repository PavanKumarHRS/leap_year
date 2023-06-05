while True:
    year = input("Enter Your year = ")
    try:
        year_number = int(year)
        if len(str(year_number)) == 4:
            if year_number % 4 == 0:
                print(f'{year_number} is a Leap Year')
            elif year_number % 100 == 0:
                print(f'{year_number} is a Leap Year')
            elif year_number % 400 == 0:
                print(f'{year_number} is a Leap Year')
            else:
                print(f'{year_number} is a not Leap Year')
        else:
            print("Enter 4 Digit Number")
        exits = input("Do you Want Continue yes or no = ")
        if exits == 'yes':
            continue
        else:
            break
    except:
        print("Enter Number Only")
        exits = input("Do you Want Continue yes or no = ")
        if exits == 'yes':
            continue
        else:
            break
