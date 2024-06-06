#Write python program that user to enter only odd numbers, else will raise an exception
class NotOddNumberError(Exception):
    pass

def get_odd_number():
    while True:
        try:
            num = int(input("Please enter an odd number: "))
            if num % 2 == 0:
                raise NotOddNumberError("The number entered is not odd.")
            print(f"Thank you for entering an odd number: {num}")
            break
        except NotOddNumberError as e:
            print(e)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

get_odd_number()
