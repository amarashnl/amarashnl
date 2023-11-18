while True:
    try:
        elements = int(input("Enter the number of elements: "))
        
        if 5 <= elements <= 10:
            user_elements = []

            
            for i in range(elements):
                value = int(input("Enter value: "))
                user_elements.append(value)

            largest_element = max(user_elements)

            
            print("Entered elements:", user_elements)
            print("Largest Element:", largest_element)

            break
        else:
            print("Error: Number of elements must be between 5 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
