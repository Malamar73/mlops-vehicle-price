# Vehicle Price Prediction - Version 3

def predict_price(year, mileage, condition):
    age = 2026 - year
    base_price = 45000

    depreciation = age * 1800
    mileage_penalty = mileage * 0.06

    price = base_price - depreciation - mileage_penalty

    if condition == "excellent":
        price *= 1.10
    elif condition == "good":
        price *= 1.00
    elif condition == "fair":
        price *= 0.85
    else:
        raise ValueError("Invalid vehicle condition")

    return max(price, 0)


if __name__ == "__main__":
    prediction = predict_price(2022, 50000, "good")
    print("Predicted vehicle price:", prediction)