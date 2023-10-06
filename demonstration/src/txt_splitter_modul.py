import re

def split_blocks(string):
    
    """ function to split a string on an arbitrary number of empty lines """

    # regular expression is introduced by 'r'
    # here, a minimum of two subsequent linebreaks (\n) are defined as pattern
    regex = r"(?:\n){2,}"
    
    # re.split is a method of the re package to directly split according to the defined pattern
    # analoguously to str.split()
    # strip the string before splitting
    return re.split(regex, string.strip())
