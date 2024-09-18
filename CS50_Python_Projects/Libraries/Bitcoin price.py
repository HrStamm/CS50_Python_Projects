# Bitcoin Price Indicator

# Libraries:
import requests
import json
import sys

# main code:
def main():
    try:
        amount = float(input("Amount of Bitcoins: "))
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price_in_usd = data["bpi"]["USD"]["rate_float"]
        price_in_total = price_in_usd * amount
        print("The current marketprice of 1 bitcoin is equal to: " f"${price_in_usd:,.4f}")
        print(f"The current marketprice of {amount} bitcoins is equal to: ${price_in_total:,.4f}")
    except requests.RequestException:
        print("Sorry i didn't quite catch that, try again please")
    except ValueError:
        print("Please enter a numeric value")
    
if __name__ == "__main__":
    main()