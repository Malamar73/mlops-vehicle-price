from model import predict_price


def test_good_condition():
    result = predict_price(2022, 50000, "good")
    assert result == 34800.0

def test_excellent_condition():
    result = predict_price(2022, 50000, "excellent")
    assert result == 38280.0


def test_fair_condition():
    result = predict_price(2022, 50000, "fair")
    assert result == 29580.0


def test_price_cannot_be_negative():
    result = predict_price(2010, 300000, "good")
    assert result == 0