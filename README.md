# Hubtel SMS Python API Example

## Overview

This repository contains a simple Python script demonstrating how to send text messages from one phone number to another using the Hubtel SMS API. Hubtel provides a reliable SMS gateway that allows you to integrate SMS functionality into your applications.

## Prerequisites

- Python 3.x
- [Requests](https://pypi.org/project/requests/) library (install with `pip install requests`)
- Hubtel Account with API Key and Secret (get it from [Hubtel Developer Portal](https://unity.hubtel.com))

## Usage

1. **Clone this repository:**

    ```bash
    git clone https://github.com/yourusername/hubtel-sms-python.git
    cd hubtel-sms-python
    ```

2. **Open `send_sms.py` in a text editor.**

3. **Replace the following placeholders with your Hubtel API Key, API Secret, and the desired sender and recipient phone numbers:**

    ```python
    clientid = "your_hubtel_api_key"
    clientsecret = "your_hubtel_api_secret"
    from = "your_sender_phone_number"
    to = "recipient_phone_number"
    content = "message to the recipient"
    ```

4. **Save the file.**

5. **Run the script:**

    ```bash
    python send_sms.py
    ```

## Additional Information

- Hubtel API Documentation: [Hubtel Developer Documentation](https://developers.hubtel.com/docs)
- Customize the message in the `send_sms.py` file according to your needs.

Feel free to fork, modify, and adapt this example for your specific use case. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.
