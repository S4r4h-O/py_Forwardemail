import requests
from requests.auth import HTTPBasicAuth
from typing import Dict, Optional, Any, Union, List

class logs:
    def get_logs(
        self,
        api_key: str,
        domain: Optional[str] = None,
        q: Optional[str] = None,
        bounce_category: Optional[str] = None,
        response_code: Optional[int] = None
    )-> requests.Response:
        
        auth = HTTPBasicAuth(username=api_key, password="")
        
        headers = {"Accpet": "application/json"}
        
        url = "https://api.forwardemail.net/v1/logs/download"

        params: Dict[str, Any] = {
            "domain": domain,
            "q": q,
            "bounce_category": bounce_category,
            "response_code": response_code
        }
        
        params = {k:v for k, v in params.items() if v is not None}
        
        r = requests.get(
            url=url,
            auth=auth,
            params=params,
            headers=headers
        )
        
        r.raise_for_status
        
        return r.text