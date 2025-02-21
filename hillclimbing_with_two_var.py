def hill_climbing_2d(func, start_x, start_y, step=0.01, max_iter=1000):  
    x, y = start_x, start_y  
    for _ in range(max_iter):  
        fxy = func(x, y)  
        fxy_x_positive = func(x + step, y)  
        fxy_x_negative = func(x - step, y)  
        fxy_y_positive = func(x, y + step)  
        fxy_y_negative = func(x, y - step)  

        # Check for improvement in x direction  
        if fxy_x_positive > fxy and fxy_x_positive >= fxy_x_negative:  
            x += step  
        elif fxy_x_negative > fxy and fxy_x_negative > fxy_x_positive:  
            x -= step  

        # Check for improvement in y direction  
        if fxy_y_positive > fxy and fxy_y_positive >= fxy_y_negative:  
            y += step  
        elif fxy_y_negative > fxy and fxy_y_negative > fxy_y_positive:  
            y -= step  

        # If no improvement in either direction, stop  
        if (fxy_x_positive <= fxy and fxy_x_negative <= fxy and  
            fxy_y_positive <= fxy and fxy_y_negative <= fxy):  
            break  
    return (x, y), func(x, y)  

if __name__ == "__main__":  
    while True:  
        try:  
            func_str = input("Enter a function of x and y (e.g., -(x-2)**2 - (y-3)**2 + 10): ")  
            func = eval(f"lambda x, y: {func_str}")  # Convert string to function  
            func(0, 0)  # Test the function with x = 0, y = 0  
            break  
        except Exception as e:  
            print(f"Invalid function. Please try again. Error: {e}")  

    while True:  
        try:  
            start_x = float(input("Enter the starting value for x (e.g., 0): "))  
            break  
        except ValueError:  
            print("Invalid input. Please enter a valid number.")  

    while True:  
        try:  
            start_y = float(input("Enter the starting value for y (e.g., 0): "))  
            break  
        except ValueError:  
            print("Invalid input. Please enter a valid number.")  

    (max_x, max_y), max_val = hill_climbing_2d(func, start_x, start_y)  
    print(f"Maxima found at (x, y) = ({max_x}, {max_y})")  
    print(f"Maximum value = {max_val}")
