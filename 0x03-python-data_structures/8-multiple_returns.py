#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns length and first character of string"""

    s_len = 0
    s_first_char = None

    if not sentence:
        return (tuple(s_len,s_first_char))
    else:
        s_len = len(sentence)
        s_first_char = sentence[0]
        return (tuple(s_len, s_first_char))
