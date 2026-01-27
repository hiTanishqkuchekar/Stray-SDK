# Stellar Agent

A lightweight Python CLI tool for sending XLM payments on the Stellar blockchain network.

## Features

- 🚀 Simple interactive CLI for sending Stellar payments
- ✅ Input validation for addresses and amounts
- 🔒 Environment-based configuration for security
- 🧪 Testnet support out of the box

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stellar-agent.git
cd stellar-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Stellar credentials
```

## Configuration

Create a `.env` file with your Stellar credentials:

```env
SOURCE_SECRET=YOUR_TESTNET_SECRET_KEY_HERE
MONITOR_ACCOUNT_ID=YOUR_PUBLIC_KEY_HERE
HORIZON_URL=https://horizon-testnet.stellar.org
NETWORK_PASSPHRASE=Test SDF Network ; September 2015
```

## Usage

Run the CLI:
```bash
python main.py
```

Or install as a package:
```bash
pip install -e .
stellar-agent
```

Follow the prompts to send payments:
```
--- Stellar Agent ---
Enter destination public key (or type 'exit' to quit): GBRPYHIL2CI3FNQ4BXLFMNDLFJUNPU2HY3ZMFSHONUCEOASW7QC7OX2H
Enter amount to send (in XLM): 10
Sending 10 XLM to GBRPYHIL2CI3FNQ4BXLFMNDLFJUNPU2HY3ZMFSHONUCEOASW7QC7OX2H...
✅ Transaction Successful!
Transaction Hash: abc123...
```

## Development

### Running Tests

```bash
pytest tests/
```

### Project Structure

```
stellar-agent/
├── stellar_agent/          # Main package
│   ├── cli.py             # CLI interface
│   ├── client.py          # Stellar client
│   ├── config.py          # Configuration
│   └── utils/             # Utilities
├── tests/                 # Tests
├── main.py               # Entry point
└── requirements.txt      # Dependencies
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Disclaimer

This tool is for educational purposes. Always test on testnet before using on mainnet.
