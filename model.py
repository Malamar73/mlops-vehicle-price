# Vehicle Price Prediction - Version 2

def predict_price(year, mileage):
    age = 2026 - year
    base_price = 45000

    depreciation = age * 1800
    mileage_penalty = mileage * 0.06

    price = base_price - depreciation - mileage_penalty

    return max(price, 0)


print(predict_price(2022, 50000))0))