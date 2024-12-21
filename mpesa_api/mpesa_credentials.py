import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class MpesaC2bCredential:
    consumer_key = 'hIc8At31Guf1z3hA2pGWEgbTrQs4JAGujMxJAoJ0G7kCNkeO'
    consumer_secret = 'bSmCGcuKDAs4G3c6k85JG34e4QWl9ynRIG3tDEiwQGWhW8rKk3UMGDJPwWcSxNSO'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    Test_c2b_shortcode = "600344"
    passkey = 'Xsiu6BfKGOX8PUbw+KqOdJYJYKxcjj9GgxnZTT3iBN4R6ns3kDPIfO3PUdPFpTGperWuiYdgNAU4O9+ipwqA7OhPlSKqzetaRHCabHA7MYf0DTmzTh2M4xz4Pn1AphrdgoUBT207wh4FjDh/S+eDRIV5+WS437brXobiXVvER2iK5xVdulNV4h54am80sk8fDT2xlEUCDbdAVZq9VfNBt2SSMkMzX6hu0R55+N/m3TJhCSr8BaW6bFUgl4JMLxerLaIm640n8OBOyXhcWZcsyuKsc5KJ5uZ9NU+zbcvrkyPcFK4loMo3L7+sZtwGAcpBKMXqLZkRVaNrDZDqAfi5Yw=='

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')

