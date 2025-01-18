# CryptoTracker

CryptoTracker is a Python application that allows you to track the latest prices, 24-hour volume, and market capitalization of various cryptocurrencies using the CoinMarketCap API.

## Features

- Fetches real-time cryptocurrency data from CoinMarketCap.
- Displays data in a tabulated format.
- Supports multiple cryptocurrency symbols.

## Requirements

- Python 3.6+
- An API key from CoinMarketCap.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/jb700r/CryptoTracker.git
   cd CryptoTracker
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Copy the `.env.template` to `.env` and add your CoinMarketCap API key:

   ```sh
   cp .env.template .env
   ```

5. Edit the `.env` file and replace `YOUR_CMC_API_KEY` with your actual CoinMarketCap API key.

## Usage

1. Run the application:

   ```sh
   python CryptoTracker.py
   ```

2. Enter the cryptocurrency symbols you want to track (e.g., `BTC,ETH,XRP`).

3. The application will display the latest prices, 24-hour volume, and market capitalization for the entered cryptocurrencies.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

- [CoinMarketCap](https://coinmarketcap.com/) for providing the API.
- [Requests](https://docs.python-requests.org/en/latest/) for HTTP requests.
- [Tabulate](https://pypi.org/project/tabulate/) for table formatting.
- [Colorama](https://pypi.org/project/colorama/) for colored terminal text.
- [python-dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
