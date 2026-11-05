import pytest
from main import CountStepsP1, CountStepsP2


def test_count_steps_input_1():
    """Test CountStepsP2 with input 1"""
    
    test = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82"
    ]
    count_p1 = CountStepsP1(test)
    count_p2 = CountStepsP2(test)
    assert count_p1 == 3
    assert count_p2 == 6


def test_count_steps_input_2():
    """Test CountStepsP2 with no movement that crosses zero"""
    
    test = [
        "R10",
        "R10",
        "L5"
    ]
    count_p1 = CountStepsP1(test)
    count_p2 = CountStepsP2(test)
    assert count_p1 == 0
    assert count_p2 == 0


def test_count_steps_input_3():
    """Test CountStepsP2 with no movement that crosses zero"""
    
    test = [
        "R1000",
        "L1000",
        "L50",
        "R1",
        "L1",
        "L1",
        "R1",
        "R100", 
        "R1"
    ]
    count_p2 = CountStepsP2(test)
    assert count_p2 == 24

def test_count_steps_input_reddit():
    """Test CountStepsP2 with no movement that crosses zero"""
    
    test = [
        "R1000",
        "L1000",
        "L50",
        "R1",
        "L1",
        "L1",
        "R1",
        "R100", 
        "R1"
    ]
    count_p2 = CountStepsP2(test)
    assert count_p2 == 24


