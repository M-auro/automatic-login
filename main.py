## Python code for automatic login to a website using requests library

import requests

def login_to_website(login_url, username, password):
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
    username = 'your_username'
    password = 'your_password'

    session = login_to_website(login_url, username, password)
    if session:
        # Continue with authenticated requests using the session object
        pass
