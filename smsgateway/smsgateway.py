import requests


class Message:
    def __init__(self, phone_number: str, message: str, device_id: int):
        self.phone_number = phone_number
        self.message = message
        self.device_id = device_id


class SMSGateway:
    BASE_ENDPOINT = 'https://smsgateway.me/api/v4/'

    def __init__(self, api_key):
        self.api_key = api_key

    def _get_headers(self):
        return {'Authorization': self.api_key}

    def _make_get(self, endpoint):
        url = SMSGateway.BASE_ENDPOINT + endpoint
        return requests.get(url, headers=self._get_headers()).json()

    def _make_post(self, endpoint, body):
        url = SMSGateway.BASE_ENDPOINT + endpoint
        return requests.post(url, json=body, headers=self._get_headers()).json()

    def search_devices(self, filters=None):
        return self._make_post('device/search', filters)

    def get_device(self, device_id):
        url = 'device/{}'.format(device_id)
        return self._make_get(url)

    def send_sms(self, *messages: Message):
        body = [m.__dict__ for m in messages]
        return self._make_post('message/send', body)

    def cancel_sms(self, *ids: int):
        body = [{'id': sms_id} for sms_id in ids]
        return self._make_post('message/cancel', body)

    def get_sms(self, sms_id: int):
        url = 'message/{}'.format(sms_id)
        return self._make_get(url)

    def search_sms(self, filters=None):
        return self._make_post('message/search', filters)
