def get_user_choice():
    """get user choice"""
    try:
        choice = input("Enter your choice (1-6): ")
        int_choice = int(choice)
        if 1 <= int_choice <= 6:
            return str(int_choice)
        else:
            raise ValueError("Invalid choice. Try again:")
    except ValueError as err_msg:
        print(f"Error: {err_msg}")
        return get_user_choice