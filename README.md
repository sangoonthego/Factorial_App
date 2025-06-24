# Factorial_App

A simple web application for calculating factorials with user authentication, built using Streamlit.

## Features

- User login system (username-based)
- Only registered users can access the factorial calculator
- Friendly greeting for unregistered users
- Calculates factorial for large numbers (limited only by system memory)

## How to Run

1. Install requirements:
    ```
    pip install -r requirements.txt
    ```

2. Run the app:
    ```
    streamlit run app.py
    ```

3. Add usernames (one per line) to `users.txt` in the project folder.

## File Structure

- `app.py` - Main Streamlit application
- `factorial.py` - Factorial calculation logic
- `requirements.txt` - Python dependencies
- `users.txt` - List of allowed usernames

## License

This project is for educational purposes.