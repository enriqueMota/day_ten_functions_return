# Functions with multiple returns


# Creating a function that transforms a name into PascalCase
def format_name(f_name: str, l_name: str):
    if f_name == "" or l_name == "":
        return "You didn't provide any input"
    # returning the capitalized names
    return f"{f_name.capitalize()} {l_name.capitalize()}"



print(format_name('eNrIqUE', 'mota'))