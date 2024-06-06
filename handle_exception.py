#Handle Exception...
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero. ({e})")
    finally:
        print("Execution of try/except block complete.")

divide(10, 0)
