from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from tabulate import tabulate
from colorama import Fore, Style
from dotenv import load_dotenv
import os

load_dotenv()
CMC_API_KEY = os.getenv("CMC_API_KEY")
if not CMC_API_KEY:
    print("Error: CMC_API_KEY is not set in the .env file.")
    exit(1)


def get_user_input_choice():
    return input("Enter the crypto symbols (e.g., BTC,ETH,XRP): ").strip()


def call_api(ids):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {
        'id': ",".join(map(str, ids))
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': CMC_API_KEY,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)

        if response.status_code != 200:
            print(f"Error: API responded with status code {response.status_code}")

        data = response.json()
        print_crypto_table(data, ids)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def get_crypto_ids(symbols):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    parameters = {
        'symbol': ",".join(symbols)
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': CMC_API_KEY,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = response.json()

        if "data" not in data:
            print("Error: API response does not contain 'data'.")
            return []

        ids = []
        for symbol in symbols:
            matches = [crypto["id"] for crypto in data["data"] if crypto["symbol"] == symbol]
            if matches:
                ids.append(matches[0])
            else:
                print(f"Warning: No data found for symbol '{symbol}'.")

        return ids
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def format_value(value):
    return f"{value:,.2f}" if value is not None else "N/A"
        

def print_crypto_table(data, crypto_ids):
    try:
        headers = [
            f"{Fore.RED}Name{Style.RESET_ALL}",
            f"{Fore.RED}Price (USD){Style.RESET_ALL}",
            f"{Fore.RED}24h Volume (USD){Style.RESET_ALL}",
            f"{Fore.RED}Market Cap (USD){Style.RESET_ALL}",
        ]
        rows = []

        for crypto_id in crypto_ids:
            crypto = data["data"][str(crypto_id)]
            name = crypto["name"]
            price = crypto['quote']['USD'].get('price', None)
            volume_24h = crypto['quote']['USD'].get('volume_24h', None)
            market_cap = crypto['quote']['USD'].get('market_cap', None)

            rows.append([  # This line should be inside the for loop
                f"{Fore.WHITE}{name}{Style.RESET_ALL}",
                f"{Fore.WHITE}{format_value(price)}{Style.RESET_ALL}",
                f"{Fore.WHITE}{format_value(volume_24h)}{Style.RESET_ALL}",
                f"{Fore.WHITE}{format_value(market_cap)}{Style.RESET_ALL}",
            ])

        print(tabulate(rows, headers=headers, tablefmt="grid"))

    except KeyError as e:
        print(f"Error: Missing key in data - {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def main():
    while True:
        symbols = [symbol.strip() for symbol in get_user_input_choice().split(",")]
        crypto_ids = get_crypto_ids(symbols)

        if crypto_ids:
            call_api(crypto_ids)
        else:
            print("Could not retrieve cryptocurrency IDs. Please check your input.")

        while True:
            user_input = input("Do you want to continue? (y/n): ").lower()
            if user_input == "n":
                print("Exiting...")
                return
            elif user_input == "y":
                break
            else:
                print("Enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()
