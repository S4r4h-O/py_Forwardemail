from modules import forwardemail
from yaml import dump

client = forwardemail.forwardemail(api_key="44386d4569a9798ed23aee77", domain="hash.fyi")

test = client.aliases(pagination=True)
data = test.json()

print(dump(data=data[0]))