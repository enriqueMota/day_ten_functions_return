# Functions with multiple returns


# Creating a function that transforms a name into PascalCase
def format_name(f_name: str, l_name: str):
    """Takes a first name and last name and 
    formats it into PascalCase

    Args:
        f_name (str): first name
        l_name (str): last name

    Returns:
        str: formated first and last name
    """
    if f_name == "" or l_name == "":
        return "You didn't provide any input"
    # returning the capitalized names
    return f"{f_name.capitalize()} {l_name.capitalize()}"

format_name

print(format_name('eNrIqUE', 'mota'))