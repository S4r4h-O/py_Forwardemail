import requests
from requests.auth import HTTPBasicAuth
from typing import Dict, Optional, Any, Union, List

class forwardemail:
    # Basic data for auth and headers
    def __init__(self, api_key: str, domain):
        self.base_url = "https://api.forwardemail.net/v1"
        self.auth = HTTPBasicAuth(api_key, "")
        self.headers = {"Accept": "application/json"}
        self.domain = domain
        
        
    # Retrieve account info
    def get_account(self) -> requests.Response:
        url = f"{self.base_url}/account"
        r = requests.get(url, auth=self.auth, headers=self.headers)
        r.raise_for_status()
        return r
    
    
    # List aliases by domain
    def aliases(
        self,
        q: Optional[str] = None,
        name: Optional[str] = None,
        recipient: Optional[str] = None,
        sort: Optional[str] = None,
        pagination: Optional[bool] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None
    ) -> requests.Response:
        
        url = f"{self.base_url}/domains/{self.domain}/aliases"
        
        params: Dict[str, Any] = {
            "q": q,
            "name": name,
            "recipient": recipient,
            "sort": sort,
            "pagination": pagination,
            "page": page,
            "limit": limit
        }
        
        params = {k:v for k, v in params.items() if v is not None}
        
        r = requests.get(
            url=url,
            auth=self.auth,
            headers=self.headers,
            params=params
        )
        
        r.raise_for_status()
        return r
    
    
    # Update domain alias
    def update_alias(
        self,
        alias_id: str,
        name: Optional[str] = None,
        recipients: Optional[List[str]] = None,
        description: Optional[str] = None,
        labels: Optional[Union[str, List[str]]] = None,
        has_recipient_verification: Optional[bool] = None,
        is_enabled: Optional[bool] = None,
        error_code_if_disabled: Optional[int] = None,
        has_imap: Optional[bool] = None,
        has_pgp: Optional[bool] = None,
        public_key: Optional[str] = None,
        max_quota: Optional[str] = None,
        vacation_responder_is_enabled: Optional[bool] = None,
        vacation_responder_start_date: Optional[str] = None,
        vacation_responder_end_date: Optional[str] = None,
        vacation_responder_subject: Optional[str] = None,
        vacation_responder_message: Optional[str] = None    
    ) -> requests.Response:
        
        url = f"{self.base_url}/domains/{self.domain}/aliases/{alias_id}"
        
        payload: Dict[str, Any] = {
            "name": name,
            "recipients": recipients,
            "description": description,
            "labels": labels,
            "has_recipient_verification": has_recipient_verification,
            "is_enabled": is_enabled,
            "error_code_if_disabled": error_code_if_disabled,
            "has_imap": has_imap,
            "has_pgp": has_pgp,
            "public_key": public_key,
            "max_quota": max_quota,
            "vacation_responder_is_enabled": vacation_responder_is_enabled,
            "vacation_responder_start_date": vacation_responder_start_date,
            "vacation_responder_end_date": vacation_responder_end_date,
            "vacation_responder_subject": vacation_responder_subject,
            "vacation_responder_message": vacation_responder_message
        }
        
        payload = {k: v for k, v in payload.items() if v is not None}
        
        r = requests.put(url=url, auth=self.auth, headers=self.headers, json=payload)
        
        r.raise_for_status()
        
        return r