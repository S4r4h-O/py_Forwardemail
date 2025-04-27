from modules import forwardemail

client = forwardemail.forwardemail(api_key="5eae8218db054ee2130180d4", domain="asnone.org")

x = client.update_alias(
    alias_id="680d4cb9ca537d8b36bddb69",
    description="alias_update"
)