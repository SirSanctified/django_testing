import pytest
import time

def test_example():
    assert 1 == 1

# marking
@pytest.mark.slow # custom marker
def test_slow_function():
    time.sleep(5)
    assert "sleep" == "sleep"

@pytest.mark.xfail
def test_failing_function():
    assert "fail" == "xfail"

@pytest.mark.skip
def test_skipped_function():
    assert "skipped" == "skipped"
