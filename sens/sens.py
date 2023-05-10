import hashlib
import hmac
import base64
import time

from sens.settings import settings_access, settings_secret, settings_uri, settings_url, settings_from_phone, setting_to_phone


timestamp = int(time.time() * 1000)
timestamp = str(timestamp)

access_key = settings_access			# access key id (from portal or Sub Account)
secret_key = settings_secret			# secret key (from portal or Sub Account)

car = "carcrush"

url = settings_url
uri = settings_uri

def	make_signature():
    global secret_key
    global access_key
    global timestamp
    global url
    global uri
    secret_key = bytes(secret_key, 'UTF-8')
    method = "POST"

    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
    return signingKey

header = {
    "Content-Type": "application/json; charset=utf-8",
    "x-ncp-apigw-timestamp": timestamp,
    "x-ncp-iam-access-key": access_key,
    "x-ncp-apigw-signature-v2": make_signature()
}
class send_sms_area():
    data = {
        "type":"MMS",
        "contentType":"COMM",
        "countryCode":"82",
        "from":settings_from_phone,
        "messages":[
            {
                "to":setting_to_phone,
            }
        ]
    }

