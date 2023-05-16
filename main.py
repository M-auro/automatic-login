import requests

login_url = 'https://example.com/login'
username = 'your_username'
password = 'your_password'

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
    # Continue with authenticated requests using the session object
    # For example, you can make subsequent requests to access protected resources
    # by using session.get(), session.post(), etc.
else:
    print("Login failed. Status code:", response.status_code)
