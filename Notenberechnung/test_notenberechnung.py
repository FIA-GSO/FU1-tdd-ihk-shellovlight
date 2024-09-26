from Notenberechnung.notenberechnung import schriftliche_note_bestimmen
import pytest

def test_schriftliche_note_bestimmen__schmerzen():
    # Arrange
    soll_ergebnis = "sehr gut"

    # Act
    ist_ergebnis = schriftliche_note_bestimmen(100)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_schriftliche_note_bestimmen__over_100_raises_error():
    # Arrange
    testwert = 101

    # Act
    with pytest.raises(ValueError):
        schriftliche_note_bestimmen(testwert)

def test_schriftliche_note_bestimmen__negative_number_raises_error():
    # Arrange
    testwert = -1

    # Act
    with pytest.raises(ValueError):
        schriftliche_note_bestimmen(testwert)