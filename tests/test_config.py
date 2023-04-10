import pytest

class NotInRange(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 4
    with pytest.raises(NotInRange):
        if a not in range(5,10):
            raise NotInRange
        else:
            assert 5 <= a < 10