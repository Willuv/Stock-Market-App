# Stock Market Web App

This project is a web application built using Django that allows users to search for stock information and store it using the Tiingo API. The application leverages Django models to manage and store stock data efficiently.

## Features

- Search for stock information using the Tiingo API.
- Store and manage stock data using Django's built-in models.
- User-friendly web interface for interacting with the stock market data.
- Secure and scalable architecture using Django.

## Requirements

- Python 3.8+
- Django 3.2+
- Tiingo API key
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/stock-market-web-app.git
    cd stock-market-web-app
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up your Tiingo API key:

    - Obtain your API key from [Tiingo](https://api.tiingo.com/)
    - Create a `.env` file in the project root and add your API key:

        ```env
        TIINGO_API_KEY=your_api_key_here
        ```

5. Apply migrations:

    ```sh
    python manage.py migrate
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000` in your browser to view the app.

## Usage

1. **Search for Stocks:**
   - Use the search functionality on the home page to look up stock information.
   - Enter the stock ticker symbol and submit the form to retrieve stock data from the Tiingo API.

2. **Store Stock Information:**
   - Save the retrieved stock information to the database by clicking the "Save" button.
   - View and manage your stored stocks from the "My Stocks" page.

## Project Structure

- `stock_market/`: Django project directory.
- `stocks/`: Django app for managing stock data.
- `templates/`: HTML templates for the web interface.
- `static/`: Static files (CSS, JS, images).
- `requirements.txt`: List of Python dependencies.
- `manage.py`: Django management script.

## Configuration

- **Settings:**
  - Adjust Django settings in `stock_market/settings.py` as needed.
  - Configure database settings, allowed hosts, and other environment-specific variables.

- **Environment Variables:**
  - Store sensitive information like API keys and secret keys in the `.env` file.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   
    ```sh
    git checkout -b feature/your-feature-name
    ```

3. Make your changes and commit them:

    ```sh
    git commit -m "Add your commit message here"
    ```

4. Push to your branch:

    ```sh
    git push origin feature/your-feature-name
    ```

5. Create a pull request to the main repository.
