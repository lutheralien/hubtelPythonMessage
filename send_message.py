import requests

def sendMessage(content, number):
    api_url = 'https://devp-sms03726-api.hubtel.com/v1/messages/send'

    # Define the query parameters
    query_parameters = {
        'clientid': '',
        'clientsecret': '',
        'from': '',
        'to': f"233{number}",
        'content': content
    }

    response = requests.get(api_url, params=query_parameters)

    if response.status_code == 201:
        # Print the response from the API
        print("Response from API:")
        print(response.text)
        print(response.status_code)
    else:
        print(f"Request failed with status code: {response.status_code}")

