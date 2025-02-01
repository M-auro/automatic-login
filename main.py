## Python code for automatic login to a website using requests library

import os
import requests

def login_to_website(login_url, username, password):
    """
    Logs into a website using the provided credentials.

    Args:
        login_url (str): The URL of the login page.
        username (str): The username for login.
        password (str): The password for login.

    Returns:
        requests.Session: A session object if login is successful.
        None: If login fails.
    """
    # Create a session
    session = requests.Session()

    # Perform the login request
    login_data = {
        'username': username,
        'password': password
    }
    response = session.post(login_url, data=login_data)

    # Check if login was successful
    if response.status_code == 200:
        print("Login successful!")
        return session
    else:
        print("Login failed. Status code:", response.status_code)
        return None

if __name__ == "__main__":
    login_url = 'https://example.com/login'
    username = os.getenv('LOGIN_USERNAME')
    password = os.getenv('LOGIN_PASSWORD')

    session = login_to_website(login_url, username, password)
    if session:
        # Continue with authenticated requests using the session object
        pass
