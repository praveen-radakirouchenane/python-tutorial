briyani_price_in_aud = {
    "chicken briyani": 18,
    "goat briyani": 20
}

briyani_price_in_usd = { briyani:f"${price*0.50:.2f} USD" for briyani, price in briyani_price_in_aud.items()}


print(briyani_price_in_usd)