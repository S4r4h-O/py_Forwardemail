import requests
from requests.auth import HTTPBasicAuth
from typing import Dict, Optional, Any, Self, Union, List, final
from forwardemail import forwardemail

class aliases(forwardemail):
    def __init__(self, api_key: str, domain: str):
        super().__init__(api_key, domain)
        
        self.alias_url = f"{self.base_url}/domains/{self.domain}/aliases/"

    
    def generate_alias_password(
        self,
        alias_id: str,
        new_password: Optional[str] = None,
        password: Optional[str] = None,
        is_override: Optional[bool] = None,
        emailed_instructions: Optional[str] = None
    ) -> requests.Response:
        
        url = f"{self.alias_url}{alias_id}/generate-password"
        
        params: Dict[str, Any] = {
            "new_password": new_password,
            "password": password,
            "is_override": is_override,
            "emailed_instruction": emailed_instructions
        }
        
        params = {k:v for k, v in params.items() if v is not None}
        
        r = requests.post(
            url=url,
            auth=self.auth,
            headers=self.headers,
            params=params
        )
        
    
    # List domain aliases
    def get_aliases(
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
    
    
    # Create new domain alias
    def new_alias(
        self,
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
        
        url = f"{self.base_url}/domains/{self.domain}/aliases"
        
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
        
        r = requests.post(url=url, auth=self.auth, headers=self.headers, json=payload)
        
        r.raise_for_status()
        
        print(f"{name} was added successfuly")
        
        return r
    
    
    # Retrieve domain alias by ID or name
    def retrieve_alias(
        self,
        alias_id: Optional[str] = None,
        alias_name: Optional[str] = None
    ) -> requests.Response:
        
        url = f"{self.base_url}/domains/{self.domain}/aliases/"
        
        if alias_id is not None:
            try:
                r = requests.get(
                    url=url+alias_id,
                    headers=self.headers,
                    auth=self.auth
                )
                
            finally:
                print(r.json())
            
        elif alias_name is not None:
            try:
                r = requests.get(
                    url=url+alias_name,
                    headers=self.headers,
                    auth=self.auth
                )
                
            finally:
                print(r.json())
                
        else:
            print("No parameters provided")
            
            
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
        
        print(f"{alias_id} updated")
        
        return r
    
    
    # Delete domain alias
    def delete_alias(
        self,
        alias_id: str
    ) -> requests.Response:
        
        url = self.alias_url+alias_id
        
        r = requests.delete(
            url=url,
            headers=self.headers,
            auth=self.auth
        )
        
        r.raise_for_status()
        
        return r