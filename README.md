Python API wrapper for https://forwardemail.net/ .

TODO:
- [ ] Update some variables
- [ ] Refine the code
- [ ] Review this documentation

---- 
## Documentation

This documentation is AI generated (because I'm too lazy) and reviwed by me. Also, notice that this project is under development (for indeterminate time), and if you have any doubts, ask me or refer to the official API documentation.

# ForwardEmail API Client Documentation

## Overview
A Python client library for interacting with the [ForwardEmail](https://forwardemail.net) API. This module simplifies managing email accounts, aliases, encryption, logs, and sending emails programmatically.

---

## Features
- **Account Management**: Create, retrieve, and update user accounts.
- **Alias Operations**: Create, list, update, and delete domain aliases.
- **Email Handling**: Send emails, check limits, and manage email history.
- **Encryption**: Encrypt sensitive data using ForwardEmail's API.
- **Logs**: Retrieve service logs for debugging and analysis.

---

## Installation
```bash
Under development.
```

---

## Usage Examples

### 1. Account Management
```python
from forwardemail import account

# Initialize with API key
acc = account(api_key="your_api_key")

# Create a new account
response = acc.create_account(email="user@example.com", password="secure_password")

# Retrieve account details
account_info = acc.get_account().json()
print(account_info)
```

---

### 2. Alias Management
```python
from forwardemail import aliases

# Initialize with API key and domain
alias_client = aliases(api_key="your_api_key", domain="example.com")

# Create a new alias
response = alias_client.new_alias(
    name="support",
    recipients=["admin@example.com"],
    description="Support team alias"
)

# List all aliases
aliases_list = alias_client.get_aliases().json()
print(aliases_list)
```

---

### 3. Sending Emails
```python
from forwardemail import emails

# Initialize with API key
email_client = emails(api_key="your_api_key")

# Send an email
response = email_client.create_email(
    from_addr="noreply@example.com",
    to_addr="recipient@example.com",
    subj="Hello!",
    txt="This is a test email."
)

print(response.status_code)  # 200 indicates success
```

---

### 4. Encryption
```python
from forwardemail import encrypt

encryptor = encrypt()
encrypted_data = encryptor.encrypt(input="sensitive_data")
print(f"Encrypted: {encrypted_data}")
```

---

### 5. Retrieving Logs
```python
from forwardemail import logs

log_client = logs()
response = log_client.get_logs(
    api_key="your_api_key",
    domain="example.com",
    response_code=404
)

print(response)  # Returns log data as text
```

---

## Class Reference

### `account`
- **Methods**:
  - `create_account(email, password)`: Creates a new account.
  - `get_account()`: Retrieves account details.
  - `update_account(...)`: Updates account fields (email, name, etc.).

### `aliases` (inherits from `forwardemail`)
- **Methods**:
  - `new_alias(...)`: Creates a domain alias.
  - `get_aliases(...)`: Lists aliases with filters.
  - `retrieve_alias(...)`: Retrieve certain alias by ID.
  - `generate_alias_password(...)`: Generates password for alias.
  - `update_alias(...)`: Self explanatory.
  - `delete_alias(...)`: Self explanatory.
  - `delete_alias(alias_id)`: Deletes an alias by ID.

### `emails`
- **Methods**:
  - `create_email(...)`: Sends an email with attachments/headers.
  - `list_emails(...)`: Retrieves email history.
  - `delete_email(email_id)`: Deletes a sent email.
  - `email_limit(...)`: Returns the limit for sending email.
  - `get_email(...)`: Returns a specific email by ID.

### `encrypt`
- **Methods**:
  - `encrypt(input)`: Returns encrypted string of `input`.

### `logs`
- **Methods**:
  - `get_logs(...)`: Fetches logs filtered by domain/status code.

---

## Design Notes
- **Authentication**: Uses `HTTPBasicAuth` with the API key.
- **Modularity**: Each API resource (e.g., accounts, aliases) has a dedicated class.
- **Error Handling**: Methods raise `requests.HTTPError` on API failures.

---

## Flow Diagram
```
[User Code] → [Class Method]
                   ↓
           [HTTP Request to ForwardEmail API]
                   ↓
           [Response Handling] → Return JSON/Text
```
---

## Notes
- **Dependencies**: Requires `requests`.
- **Typo Alert**: In `logs.py`, fix `headers = {"Accepet": "application/json"}` → `"Accept"`.
- **Testing**: Add unit tests for each class (not included here).

Update documentation as new features are added or APIs change. Contributions welcome!

I am not vinculated or affiliated to Forwardemail, this is just a personal project and a way of contributing to the open source community.
