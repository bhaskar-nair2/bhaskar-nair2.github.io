import requests
import discord

url = "https://discordapp.com/api/webhooks/464540951793238017IMYLlnN9CYIvcHzLZ30NQDbRg41vclv5RX6tZzl8zTeg9EuTJqcWqhmyD3EceSxiNzNh"

xyz={
    "username": "New Message!!",
    "avatar_url": "https://cdn4.iconfinder.com/data/icons/flatron-2000-set-1/512/envelope-512.png",
    "content": "Subject",
    "embeds": [{
        "color": 15258703,
        "fields": [{
            "name": "From: Email ID",
            "value": "User's Message"
        }],
        "footer": {
            "text": "From www.bhaskarnair.me"
        }
    }]
}

WebString = discord.utils.to_json(xyz)
r = requests.post(url=url, json=WebString)
print(r.status_code, r.reason, r.content)
