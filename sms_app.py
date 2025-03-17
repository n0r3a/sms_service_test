from bottle import route, run, request, template
import requests
import os

# Make use of route method from bottle and show the index.html
@route('/')
def index():
    return template('index.html')

# Send sms function. Use the request library to pass input from the html page
#+ api_username and api_password are using the os library and are currently stored in environment variables.
#+ I need to update this and make it more secure

@route('/send_sms', method='POST')
def send_sms():
    from_number = request.forms.get('from_number')
    to_number = request.forms.get('phone_number')
    message = request.forms.get('message')

    api_username = os.environ.get("SMS_API_USERNAME")
    api_password = os.environ.get("SMS_API_PASSWORD")

# If statement for authentication
    if not api_username or not api_password:
        return template('index.html', message="Error: API credentials not found.")

# try statement with post request, this is the part where we send the sms (using the example from the API provider.
    try:
        response = requests.post(
            'https://example.api.com/sms',
            auth=(api_username, api_password),
            data={
                'from': from_number,
                'to': to_number,
                'message': message,
            },
        )

# Check if everything went ok or if an error occurred and return it to the webpage
#+ make use of except. I got some help from google here and it works, needs some improvement 
        
        response.raise_for_status()
        return template('index.html', message="SMS sent successfully!")
    except requests.exceptions.RequestException as e:
        return template('index.html', message=f"Error sending SMS: {e}")

# Run bottle and serve it locally on port 8080 and communitcate with the webserver (nginx)
run(host='127.0.0.1', port=8080, debug=True)
