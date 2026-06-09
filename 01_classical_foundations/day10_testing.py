#The Production Failure Test Suite
import pytest

# Imagine this is the function inside your app that extracts numbers from an AI payload
def extract_model_temperature(config_dict):
    """
    Extracts hyperparameter temperature settings. 
    Must be strictly between 0.0 and 1.0.
    """
    temp = config_dict.get("temperature", 0.7)
    if not (0.0 <= temp <= 1.0):
        raise ValueError("Temperature threshold is out of standard bounds!")
    return temp

# --- AUTOMATED TEST BATTERY ---

def test_extract_temperature_success():
    """
    Test that a valid standard payload processes correctly.
    """
    valid_payload = {"temperature": 0.2}
    # TODO: Step 1 - Call extract_model_temperature(valid_payload)
    # Assert that the returned output value is exactly equal to 0.2
    assert extract_model_temperature(valid_payload) == 0.2

def test_extract_temperature_boundary_failure():
    """
    Test that an invalid parameter payload correctly triggers a ValueError crash flag.
    """
    corrupt_payload = {"temperature": 4.5} # Invalid! Out of bounds
    
    
    # TODO: Step 2 - Use pytest's exception wrapper framework to assert a ValueError fires.
    # Hint: The pattern utilizes a context manager block:
    # with pytest.raises(ValueError):
    #     extract_model_temperature(corrupt_payload)
    with pytest.raises(ValueError):
        extract_model_temperature(corrupt_payload)

