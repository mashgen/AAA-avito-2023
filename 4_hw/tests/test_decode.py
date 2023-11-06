import pytest

from morse import decode


@pytest.mark.parametrize(
    "morse_message,decoded_morse_message",
    [
        ("... --- ...", "SOS"),
        ("-- .- .-. .. .-", "MARIA"),
        ("", ""),
    ],
)
def test_decode(morse_message, decoded_morse_message):
    assert decode(morse_message) == decoded_morse_message
