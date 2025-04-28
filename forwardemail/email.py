import requests
from requests.auth import HTTPBasicAuth
from typing import Dict, Optional, Any, Union, List
from .contants import base_url, encoded_headers, headers


class emails:
    def __init__(self, api_key: str):
        self.email_url = base_url + "/emails"
        self.email_auth = HTTPBasicAuth(username=api_key, password="")
        
        
    def email_limit(self):
        
        url = self.email_url + "/limit"
        
        headers = {"Accept": "application/json"}
        
        r = requests.get(
            url = url,
            auth=self.email_auth,
            headers=headers
        )
        
        r.raise_for_status()
        
        return r
    
    def list_emails(
        self,
        q: Optional[str] = None,
        domain: Optional[str] = None,
        sort: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None
    )-> requests.Response:
        
        params: Dict[str, Any] = {
            "q": q,
            "domain": domain,
            "sort": sort,
            "page": page,
            "limit": limit
        }
        
        params = {k:v for k,v in params.items() if v is not None}
        
        r = requests.get(
            url=self.email_url,
            auth=self.email_auth,
            params=params,
            headers=headers
        )
        
        r.raise_for_status()
        
        return r
    
    def create_email(
        self,
        from_addr: Optional[str] = None,
        to_addr: Optional[Union[str, List[str]]] = None,
        cc: Optional[Union[str, List[str]]] = None,
        bcc: Optional[Union[str, List[str]]] = None,
        subj: Optional[str] = None,
        txt: Optional[str] = None,
        html: Optional[str] = None,
        attach: Optional[List] = None,
        sender: Optional[str] = None,
        replyTo: Optional[str] = None,
        inReplyTo: Optional[Union[str, List[str]]] = None,
        references: Optional[Union[str, List[str]]] = None,
        attachDataUrls: Optional[bool] = None,
        watchHtml: Optional[str] = None,
        amp: Optional[str] = None,
        icalEvent: Optional[Dict[str, Any]] = None,
        alternatives: Optional[List] = None,
        encoding: Optional[str] = None,
        raw: Optional[Union[str, bytes]] = None,
        textEncoding: Optional[str] = None,
        priority: Optional[str] = None,
        headers: Optional[Union[Dict[str, Any], List[str, Any]]] = None,
        messageId: Optional[str] = None,
        date: Optional[str] = None,
        list: Optional[Dict[str, Any]] = None
    )-> requests.Response:
        
        params: Dict[str, Any] = {
        "from":             from_addr,
        "to":               to_addr,
        "cc":               cc,
        "bcc":              bcc,
        "subject":          subj,
        "text":             txt,
        "html":             html,
        "attach":           attach,
        "sender":           sender,
        "replyTo":          replyTo,
        "inReplyTo":        inReplyTo,
        "references":       references,
        "attachDataUrls":   attachDataUrls,
        "watchHtml":        watchHtml,
        "amp":              amp,
        "icalEvent":        icalEvent,
        "alternatives":     alternatives,
        "encoding":         encoding,
        "raw":              raw,
        "textEncoding":     textEncoding,
        "priority":         priority,
        "headers":          headers,
        "messageId":        messageId,
        "date":             date,
        "list":             list,
        }
        
        params = {k:v for k,v in params.items() if v is not None}
        
        r = requests.post(
            url=self.email_url,
            headers=encoded_headers,
            json=params,
            auth=self.email_auth
        )
        
        r.raise_for_status()
        
        return r
    
    
    def get_email(self, email_id: str)-> requests.Response:
        
        url = self.email_url + f"/{email_id}"
        
        r = requests.get(url=url, auth=self.email_auth, headers=headers)
        
        r.raise_for_status
        
        return r
    
    
    def delete_email(self, email_id: str) -> requests.Response:
        
        url = self.email_url + f"/{email_id}"
        
        r = requests.delete(
            url=url,
            headers=headers,
            auth=self.email_auth
        )