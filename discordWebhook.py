import requests
import json

url = "https://discordapp.com/api/webhooks/464540951793238017/IMYLlnN9CYIvcHzLZ30NQDbRg41vclv5RX6tZzl8zTeg9EuTJqcWqhmyD3EceSxiNzNh"
urlz = 'https://discordapp.com/api/oauth2/authorize?client_id=464565547208671242&permissions=64512&scope=bot'
API_ENDPOINT = 'https://discordapp.com/api/v6'
head = {"key": "IMYLlnN9CYIvcHzLZ30NQDbRg41vclv5RX6tZzl8zTeg9EuTJqcWqhmyD3EceSxiNzNh"}

xyz = {
    "Client ID": 464565547208671242,
    "Client Secret": "ie_GLq0-msOk0r3h5RcV4_nRhUjH88L0",
    "username": "New Message!!",
    "avatar_url": "https://cdn4.iconfinder.com/data/icons/flatron-2000-set-1/512/envelope-512.png",
    "content": "Subject"
}

data = {
    'client_id': 464565547208671242,
    'client_secret': "ie_GLq0-msOk0r3h5RcV4_nRhUjH88L0",
    'grant_type': 'authorization_code',
    'code': "No Clue"
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

WebString = json.dumps(xyz)
r = requests.post('%s/oauth2/token' % API_ENDPOINT, data, headers)
r.raise_for_status()

# {
# 	"username": "New Message!!",
# 	"avatar_url": "https://cdn4.iconfinder.com/data/icons/flatron-2000-set-1/512/envelope-512.png",
# 	"content": "Subject",
# 	"embeds": [{
# 		"color": 15258703,
# 		"fields": [{
# 			"name": "From: Email ID",
# 			"value": "User's Message"
# 		}],
# 		"footer": {
# 			"text": "From www.bhaskarnair.me"
# 		}
# 	}]
# }
