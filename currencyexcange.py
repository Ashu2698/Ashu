import requests

def get_exchange_rate(base_currency, target_currency):
    api_key = 'ab8f88ad456b70223abc931b'  # Replace 'YOUR_API_KEY' with your actual API key
    url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * rate
    return converted_amount

def main():
    amount = float(input("Enter amount to convert: "))
    base_currency = input("Enter base currency: ").upper()
    target_currency = input("Enter target currency: ").upper()

    converted_amount = convert_currency(amount, base_currency, target_currency)
    print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()
