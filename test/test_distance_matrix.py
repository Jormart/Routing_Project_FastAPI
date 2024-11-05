# tests/test_distance_matrix.py
import pytest
from app.services.distance_matrix import get_distance_matrix

def test_get_distance_matrix(mocker):
    mock_response = {
        "distances": [[0, 10], [10, 0]],
        "durations": [[0, 15], [15, 0]]
    }
    mocker.patch("app.services.distance_matrix.requests.post", return_value=mocker.Mock(json=lambda: mock_response))
    locations = [[40.4168, -3.7038], [39.4699, -0.3757]]
    result = get_distance_matrix(locations)
    assert "distances" in result
    assert result["distances"][0][1] == 10
