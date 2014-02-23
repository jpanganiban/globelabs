import requests
import urllib
from decimal import Decimal


class Globe(object):

    portal_base_url = "http://developer.globelabs.com.ph"
    api_base_url = "http://devapi.globelabs.com.ph"

    def __init__(self, app_id=None, app_secret=None, redirect_uri=None,
                 portal_base_url=None, api_base_url=None, access_token=None,
                 subscriber_number=None, shortcode=None, last_reference_code=None):
        """@todo: Constructur

        :app_id: @todo
        :app_secret: @todo
        :redirect_uri: @todo
        :portal_base_url: @todo
        :api_base_url: @todo
        :access_token: @todo
        :subscriber_number: @todo
        :shortcode: @todo
        :last_reference_code: @todo

        """
        self.app_id = app_id
        self.app_secret = app_secret

        self.redirect_uri = redirect_uri
        self.portal_base_url = portal_base_url or self.portal_base_url
        self.api_base_url = api_base_url or self.api_base_url

        self.access_token = access_token
        self.subscriber_number = subscriber_number
        self.shortcode = shortcode

        self.last_reference_code = None

    def get_auth_url(self):
        """@todo: Docstring for get_auth_url.

        :returns: @todo

        """
        return self.portal_base_url + "/dialog/oauth?%s" % \
            urllib.urlencode({'app_id': self.app_id})

    def get_access_token(self, code):
        """@todo: Docstring for get_access_token.

        :code: @todo
        :returns: @todo

        """
        data = {
            'app_id': self.app_id,
            'app_secret': self.app_secret,
            'code': code,
        }
        response = requests.post(self.portal_base_url + "/oauth/access_token", data=data)
        if response.status_code == 200:
            r_data = response.json()
            self.access_token = r_data['access_token']
            self.subscriber_number = r_data['subscriber_number']
        return response

    def send_sms(self, message, subscriber_number=None, access_token=None):
        """Sends an sms to a subscriber

        :message: @todo
        :subscriber_number: @todo
        :access_token: @todo
        :returns: @todo

        """
        data = {
            'message': message,
            'address': subscriber_number or self.subscriber_number,
            'access_token': access_token or self.access_token,
        }
        url = self.api_base_url + "/smsmessaging/v1/outbound/%s/requests" % \
            self.shortcode
        return requests.post(url, data=data)

    def charge(self, amount, reference_code=None, subscriber_number=None,
               access_token=None, description=None):
        """Charge a subscriber wallet

        :amount: @todo
        :reference_code: @todo
        :subscriber_number: @todo
        :access_token: @todo
        :description: @todo
        :returns: @todo

        """
        data = {
            'access_token': access_token or self.access_token,
            'amount': "%.2f" % Decimal(amount),
            'description': description,
            'endUserId': subscriber_number or self.subscriber_number,
            'referenceCode': reference_code or self.last_reference_code + 1,
            'transactionOperationStatus': 'Charged',
        }
        print data
        url = self.api_base_url + "/payment/v1/transactions/amount"
        response = requests.post(url, data=data)
        if response.status_code == 201:
            self.last_reference_code = data['referenceCode']
        return response
