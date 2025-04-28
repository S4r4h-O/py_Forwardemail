import requests
from requests.auth import HTTPBasicAuth
from typing import Dict, Any, Optional

class account:
    def __init__(self, api_key: str):
        self.account_url = "https://api.forwardemail.net/v1/account"
        self.acc_auth = HTTPBasicAuth(username=api_key, password="")
        
        
    def create_account(self, email: str, password: str) -> requests.Response:
        data: Dict[str, Any] = {
            "email": email,
            "password": password
        }
        
        headers: Dict[str, Any] = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }
        
        r = requests.post(
            url=self.account_url,
            auth=self.acc_auth,
            headers=headers,
            data=data
        )
        
        
        r.raise_for_status
        print("Account created")
        return r
    
    
    # Retrieve account info
    def get_account(self) -> requests.Response:
        r = requests.get(url=self.account_url, auth=self.acc_auth)
        r.raise_for_status()
        return r
    
    
    def update_account(
        self,
        email: Optional[str] = None,
        given_name: Optional[str] = None,
        family_name: Optional[str] = None,
        avatar_url: Optional[str] = None
    )-> requests.Response:
        
        headers: Dict[str, Any] = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }
        
        data: Dict[str, Any] = {
            "email": email,
            "given_name": given_name,
            "family_name": family_name,
            "avatar_url": avatar_url
        } 
        
        data = {k:v for k,v in data.items() if v is not None}
        
        r = requests.put(
            url=self.account_url,
            auth=self.acc_auth,
            headers=headers,
            data=data
        )
        
        for k,v in data.items():
            if v is not None:
                print(f"Item updated: {k, v}")
        
        return r