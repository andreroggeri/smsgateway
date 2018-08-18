# SMSGateway.me Client for API v4
Recently the implementation of the smsgateway.me for sending/receiving SMS's has changed
and broke the library that I was using, so I decided to make my own version

# Usage

## Token
Get your API Token in the [settings page](https://smsgateway.me/dashboard/settings)

## Client initalization
Before starting is necessary to create the client with the token as parameter
```
from smsgateway import SMSGateway, Message
client = SMSGateway('your-api-token-here-keep-it-secret')
```

## Device lookup
Sending messages requires the device id, so its necessary to get it
```
devices = client.search_devices()
if len(devices['results']) == 0:
  raise Exception('No device found on your account')
  
did = devices['results'][0]['id']
```
> Its possible to pass a filter object as parameter as [specified on the docs](https://smsgateway.me/sms-api-documentation/devices/searching-android-devices)

## Sending messages
```
message1 = Message('12345678', 'Message 1 body', did)
message2 = Message('12345678', 'Message 2 body', did)
status = client.send_message(message1, message2)
print(status)
```

# Support
I decided to implement only the endpoints that I need, but if you need anything else, please make a PR :)

Below what is already implemented and what's not:

## Devices
 - :heavy_check_mark: Get devices information
 - :heavy_check_mark: Search for devices

## Messages
 - :heavy_check_mark: Sending a message
 - :heavy_check_mark: Canceling a message
 - :heavy_check_mark: Getting a message information
 - :heavy_check_mark: Searching for messages

## Contacts
 - :x: Creating a contact
 - :x: Updating an existing contact
 - :x: Adding a phone to an existing contact
 - :x: Remove a phone from an existing contact
 - :x: Getting a contact information
 - :x: Searching for contacts

## Callbacks
 - :x: Creating a callback
 - :x: Updating an existing callback
 - :x: Getting callback information
 - :x: Searching for callbacks

# Tests
TBD

# Contributing
PR's are welcome
