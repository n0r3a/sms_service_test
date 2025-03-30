from bottle import request, post, run
import urllib.parse  


@post('/api/sms') 
def sms():
    # use request module and get the SMS data and use all available options
    sms_id = request.forms.get('id')
    from_number = request.forms.get('from')
    to_number = request.forms.get('to')
    message_encoded = request.forms.get('message')
    created = request.forms.get('created')
    direction = request.forms.get('direction')

    # decode url-encoded message
    message = urllib.parse.unquote(message_encoded)

    # print sms data 
    print(f"SMS ID: {sms_id}")
    print(f"From: {from_number}")
    print(f"To: {to_number}")
    print(f"Message: {message}")
    print(f"Created: {created}")
    print(f"Direction: {direction}")

    # automatic reply
	reply_message = "Thank you for your message! =)"

    # send the reply back
    return reply_message 

run(host='127.0.0.1', port=5501)
