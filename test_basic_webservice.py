import pytest
import numpy as np
from basic_webservice import calcDistance


@pytest.mark.parametrize("a, b, distance", [
    ([1, 1], [1, 1], 0),
    ([1, 2], [2, 3], np.sqrt(2)),
])
def test_calcDistance(a, b, distance):
    assert calcDistance(a, b) == distance
