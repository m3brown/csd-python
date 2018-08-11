import pytest
from vending_machine import VendingMachine

def test_release_change_when_no_payment_expects_0_change():
    # Arrange
    vending_machine = VendingMachine()

    # Act
    result = vending_machine.release_change()

    # Assert
    assert result == 0
    assert 0 == result



