from ast import Dict
import requests
from forwardemail import forwardemail

class encrypt:
    def encrypt(self, input: str):
        headers = {"Accept": "application/json","Content-Type": "application/x-www-form-urlencoded"}
        url = "https://api.forwardemail.net/v1/encrypt"
        r = requests.post(
            url=url,
            headers=headers,
            data={"input": input}
        )
        
        r.raise_for_status()
        
        return r.text