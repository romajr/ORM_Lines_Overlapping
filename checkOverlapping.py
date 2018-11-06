#!/usr/bin/env python
# -*- coding: utf-8
"""
##################### Q1 Question A - ORMUCO ####################
#-------------------------- Luiz Roma --------------------------#
#
# This code implements a two-lines (x-axis) overlapping check
#
# QUESTION ENUMERATION
# Your goal for this question is to write a program that accepts
# two lines (x1,x2) and (x3,x4) on the x-axis and returns whether
# they overlap. As an example, (1,5) and (2,6) overlaps
# but not (1,5) and (6,8).
#
#---------------------------------------------------------------#
#################################################################
"""

import argparse

def set_organize(a: tuple, b: tuple):
    """
    ORGANIZE TUPLES TO WORK BETTER
    setOrganize takes the 2 tuples in entry and sort them
    this helps the other functions to work properly
    :param a: 1st tuple input by user
    :param b: 2nd tuple input by user
    :return: the lists a, b ordered to follow x-axis
    """
    a = sorted(a)
    b = sorted(b)
    return a, b

def check_overlap(a: tuple, b: tuple) -> bool:
    """
    SIMPLE COORDINATE INTERSECTION
    checkOverlap considers 2 entries as tuples and returns a boolean value
    it simply checks if line 'a' contains at least one extremity of 'b' line
    :param a: 1st tuple input by user
    :param b: 2nd tuple input by user
    :return: True/False if tuples overlapps or not
    """
    return (a[0] <= b[0] <= a[1]) or (a[1] >= b[1] >= a[0])

def check_twins(a: tuple, b: tuple) -> bool:
    """
    TWINS IN BOTH LINES
    checkTwins looks to same numbers in both lines range
    If there is the same number in both lines, lines are overlapped
    NOTE: It only works with integers
    :param a: 1st tuple input by user
    :param b: 2nd tuple input by user
    :return: True/False if there are same numbers in the range of each tuple
    """
    for number in range(a[1], a[0], -1):
        for spy in range(b[0], b[1], 1):
            return number == spy
    return 0

def get_distance(a: tuple, b: tuple) -> int:
    """
    GET DISTANCE BETWEEN 2 DIFFERENT LINES
    getDistance identifies 2 lines with no intersection by calling other functions
    and calculates the distance between them
    :param a: 1st tuple input by user
    :param b: 2nd tuple input by user
    :return: the distance between the 2 lines if they are not coincident
    """
    if(not check_overlap(a, b) and not check_twins(a, b)):
        if(a[0] + a[1] > b[0] + b[1]):
            return a[0] - b[1]
        else:
            return b[0] - a[1]
    return -1
