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

def test_release_change_with_payment_expects_change_returned():
    # Arrange
    vending_machine = VendingMachine()
    vending_machine.insert_coin(1)

    # Act
    result = vending_machine.release_change()

    # Assert
    assert result > 0

@pytest.mark.skip("buy_product now returns an exception")
def test_buy_product_with_no_payment_expects_nothing():
    # Arrange
    vending_machine = VendingMachine()

    # Act
    result = vending_machine.buy_product()

    # Assert
    assert result is None

def test_buy_product_with_payment_expects_product():
    # Arrange
    vending_machine = VendingMachine()
    vending_machine.insert_coin(1)

    # Act
    result = vending_machine.buy_product()

    # Assert
    assert result is not None

def test_buy_product_with_no_payment_expects_exception():
    # Arrange
    vending_machine = VendingMachine()

    # Act
    with pytest.raises(RuntimeError):
        vending_machine.buy_product()

    # Assert
    # an exception should be raised

def test_get_message_returns_success_message_with_successful_purchase():
    # Arrange
    vending_machine = VendingMachine()
    vending_machine.insert_coin(1)

    # Act
    vending_machine.buy_product()

    # Assert
    assert vending_machine.message == "Enjoy!"

def test_get_message_returns_insert_money_message_when_purchase_fails():
    # Arrange
    vending_machine = VendingMachine()

    # Act
    try:
        vending_machine.buy_product()
        assert False, "buy_product should have failed with exception"
    except:
        # Assert
        assert vending_machine.message == "Please insert money"
