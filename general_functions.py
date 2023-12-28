"""
function that are used in the main file not specific to encrypt or decrypt
"""


def mode_select() -> str:
    """
    function to select the mode of the program
    :return: the name of the mode
    """
    mode = input("decrypt or encrypt").lower()
    if mode != "decrypt" or mode != "encrypt":
        return mode_select()
    return mode
