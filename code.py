# Name: Fernando Bezerra
# Student Number: 041100707

from adafruit_circuitplayground import cp
import time

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3


while True:
    
    # Show the menu to the user
    try:
        print("Choose an option from 1 to 3 to change the colors of the LEDs:")
        print("1. Red:")
        print("2. Green:")
        print("3. Blue:")
        print("Press 'q' or 'Q' to exit the program.\n")
                
        # Maximum variable initialized
        max = 255;
        
        # Get the option from the user.
        option = input("Enter the option: ").lower()
        print("")
        
        # Check if the user wants to exit from the program
        if option == 'q' or option == 'Q':
            
            while max > 0:
                for i in range(10):
                    cp.pixels[i] = (0, 0, 0) 
                cp.pixels.show()
                
                max = max -1
                
            print("Program ended.")
            break   
        
        # Cast a string to an integer.
        option = int(option)
        
        # Option that turns the lights in red 
        if option == 1:
            
            while max > 0:
                for i in range(10):
                    cp.pixels[i] = (max, 0, 0) 
                cp.pixels.show()
                time.sleep(0.010)

                max = max - 1
        
        # Option that turns the lights in green       
        elif option == 2:
            
                while max > 0:
                    
                    for i in range(10):
                        cp.pixels[i] = (0, max, 0) 
                    cp.pixels.show()
                    time.sleep(0.010)

                    max = max - 1
        
        # Option that turns the lights in blue    
        elif option == 3:
        
                while max > 0:
                    
                    for i in range(10):
                        cp.pixels[i] = (0, 0, max) 
                    cp.pixels.show()
                    time.sleep(0.010)

                    max = max - 1
                         
        else:
            # Message when the user trying to enter with a unavailable choice
            print("Number out of range. Please enter an option from 1 to 3.\n")

    # Exception created in case the value entered is no available.    
    except:
        # Message when the user type a letter instead of a number
        print('That was a no valid choice!\n')
