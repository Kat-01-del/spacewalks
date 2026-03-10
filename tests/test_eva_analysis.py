from eva_data_analysis import calculate_crew_size, text_to_duration
import pytest

def test_text_to_duration_integer():
    """
    Test that the text_to_duration function with an integer duration.

    """
    assert text_to_duration("10:00") == 10

def test_text_to_duration_float():
    """
    Test that the text_to_duration function with a float value for typical non-zero minute durations.

    """
    assert text_to_duration("10:20") == pytest.approx(10.333333)  



@pytest.mark.parametrize("input_value, expected_result", [
    ("Mary;", 1),
    ("Mary; Jane; Charlie;", 3),
    ("", None)
])

def test_calculate_crew_size(input_value, expected_result):
    """
    Test that the calculate_crew_size function returns the correct crew size for typical crew entries.
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result 

