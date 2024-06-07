"""
This file contains general purpose functions.
"""
import time


def try_with_exponential_backoff(func: callable, *args, **kwargs) -> any:
    """
    Tries ten times to execute a function with exponential backoff

    PARAMETERS:
        func: function to execute
        args: arguments for the function
        kwargs: keyword arguments for the function

    RETURNS:
        result of the function

    RAISES:
        Exception: if the function fails to execute after 10 tries
    """
    tries = 0
    while tries < 10:
        tries += 1
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            print(f"Retrying...")
            time.sleep(2**tries)
    raise Exception(f"failed to execute {func.__name__} after 10 tries")
