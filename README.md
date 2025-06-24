# Factorial_App

A simple web application for calculating factorials with user authentication, built using Streamlit.

## Features

- User registration and login system (username-based)
- Only registered users can access the factorial calculator
- Friendly greeting for unregistered users
- Calculates factorial for large numbers (limited only by system memory)

## Demo

Try the app here: [https://factorialapp-jkpdg9xu8txviidqrrvmve.streamlit.app](https://factorialapp-jkpdg9xu8txviidqrrvmve.streamlit.app)

## How to Run Locally

1. **Clone the repository:**
    ```
    git clone https://github.com/sangoonthego/Factorial_App.git
    cd Factorial_App
    ```

2. **Install requirements:**
    ```
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```
    streamlit run app.py
    ```

4. **User management:**
    - Users can register directly on the web app.
    - Usernames are stored in `users.txt` (created automatically).

## File Structure

- `app.py` - Main Streamlit application
- `factorial.py` - Factorial calculation logic
- `requirements.txt` - Python dependencies
- `users.txt` - List of registered usernames (auto-generated)
- `README.md` - Project description

## License

This project is for educational purposes.