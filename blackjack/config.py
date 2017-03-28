#!/usr/bin/env python
# -*- coding: utf-8 -*-

suits = [
    {
        "name": "Spades",
        "symbol_white": "\u2664",
        "symbol_black": "\u2660",
    },
    {
        "name": "Diamonds",
        "symbol_white": "\u2662",
        "symbol_black": "\u2666",
    },
    {
        "name": "Clubs",
        "symbol_white": "\u2667",
        "symbol_black": "\u2663",
    },
    {
        "name": "Hearts",
        "symbol_white": "\u2661",
        "symbol_black": "\u2665",
    },
]

values = [
    {
        "name": "Ace",
        "short_name": "A",
    },
    {
        "name": "Two",
        "short_name": "2",
    },
    {
        "name": "Three",
        "short_name": "3",
    },
    {
        "name": "Four",
        "short_name": "4",
    },
    {
        "name": "Five",
        "short_name": "5",
    },
    {
        "name": "Six",
        "short_name": "6",
    },
    {
        "name": "Seven",
        "short_name": "7",
    },
    {
        "name": "Eight",
        "short_name": "8",
    },
    {
        "name": "Nine",
        "short_name": "9",
    },
    {
        "name": "Ten",
        "short_name": "10",
    },
    {
        "name": "Jack",
        "short_name": "J",
    },
    {
        "name": "Queen",
        "short_name": "Q",
    },
    {
        "name": "King",
        "short_name": "K",
    },
]

blackjack_point_values = {"ace": [10, 1], "two": [2], "three": [3], "four": [4], "five": [5], "six": [6], "seven": [7],
                          "eight": [8], "nine": [9], "ten": [10], "jack": [10], "queen": [10], "king": [10]}
