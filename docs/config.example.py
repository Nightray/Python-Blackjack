#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Suits is a list of dictionaries containing data for describing four card suits which include suit names
# as well as codes for ascii symbols in both black and white versions.

# Example:
suits = [
    {
        "name": "Spades",
        "symbol_white": "\u2664",
        "symbol_black": "\u2660",
    },
]


# Values is a list of dictionaries containing data for describing thirteen card values which include both full and
# short names of the values.

# Example:
values = [
    {
        "name": "Ace",
        "short_name": "A",
    },
]

# Blackjack_point_values is a dictionary containing key-value pairs of lowercase full name of a card value and a list
# with number of points in Blackjack.

# Example
blackjack_point_values = {
    "ace": [10, 1]  # Since ace can be both 1 and 10 in Blackjack, all values are written as a list
}
