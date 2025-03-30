import requests
import os

# need to change this and make it more secure
def send_sms(from_number, to_number, message):
    api_username = os.environ.get("SMS_API_USERNAME")
    api_password = os.environ.get("SMS_API_PASSWORD")

    if not api_username or not api_password:
        print("Error: API credentials not found.")
        return

    try:
        response = requests.post(
            'https://api.provider.com/sms',
            auth=(api_username, api_password),
            data={
                'from': from_number,
                'to': to_number,
                'message': message,
            },
        )
        response.raise_for_status()
        print("SMS sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending SMS: {e}")

if __name__ == '__main__':
    from_number = input("Enter from number: ")
    to_number = input("Enter to number: ")
    message = input("Enter message: ")
    send_sms(from_number, to_number, message)
