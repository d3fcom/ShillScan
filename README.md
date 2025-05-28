
# ShillScan - Cryptocurrency Tracker /    By: Weis.    2025.


A Flask-based web application for tracking cryptocurrency prices and market data. This is a demo application (Abandoned project) that uses mock data for educational purposes.

## Features

- Real-time cryptocurrency price tracking (simulated)
- Search functionality for tokens (Non-Finished)
- Responsive web interface with Tailwind CSS
- Token detail pages
- Market cap and volume information

## Prerequisites

- Python 3.11 or higher
- Poetry (recommended) or pip for package management

## Installation & Setup

### Option 1: Using Poetry (Recommended)

1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   poetry install
   ```
4. Run the application:
   ```bash
   poetry run python main.py
   ```

### Option 2: Using pip

1. Clone or download this repository
2. Navigate to the project directory
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install flask
   ```
5. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Start the application using one of the methods above
2. Open your web browser and navigate to `http://localhost:5000`
3. Browse the cryptocurrency list on the main page
4. Use the search functionality to find specific tokens
5. Click on any token to view detailed information

## Project Structure

```
├── app.py              # Flask application setup
├── main.py             # Application entry point
├── models.py           # Token data model (in-memory)
├── routes.py           # API and web routes
├── utils.py            # Utility functions for data handling
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # Main page
│   └── token_detail.html # Token detail page
├── static/             # Static assets
│   ├── css/
│   ├── js/
│   └── img/
└── README.md           # This file
```

## API Endpoints

- `GET /` - Main page with token list
- `GET /api/tokens` - Get all tokens (JSON)
- `GET /api/tokens?search=<query>` - Search tokens (JSON)
- `GET /api/token/<symbol>` - Get specific token data (JSON)
- `GET /token/<symbol>` - Token detail page
- `GET /api/tokens/update` - Update token prices (simulated)
- `GET /generate-mock-data` - Regenerate mock data

## Configuration

This application runs with mock data by default. No external APIs or databases are required.

### Customizing Mock Data

To customize the cryptocurrency data, edit the `crypto_data` list in `utils.py`:

```python
crypto_data = [
    ('SYMBOL', 'Token Name', base_price),
    # Add more tokens here
]
```

## Development

The application includes:
- Debug mode enabled by default
- Automatic code reloading
- Comprehensive logging
- Mock data generation

## Production Considerations

For production deployment:
1. Set `debug=False` in `main.py`
2. Use a production WSGI server like Gunicorn
3. Consider implementing real API integration
4. Add proper error handling and logging
5. Implement caching for better performance

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS (Tailwind), JavaScript
- **Data Storage**: In-memory (no database required)
- **Charts**: Chart.js for data visualization

## License

This project is for educational purposes. Feel free to modify and use as needed.

## Contributing

This is a demo project, but suggestions and improvements are welcome!
