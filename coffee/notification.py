import requests
import json

def get_order_count():
    return len(
        requests.get(
            "https://<REPLACE ME>/todo/json"
        ).json().get('orders', [])
    )

def notify_henry(order_count="Unknown"):
    return requests.post(
        "https://api.pushover.net/1/messages.json",
        headers={"Content-type": "application/json"},
        data=json.dumps({
            "token": "<REPLACE ME>",
            "user": "<REPLACE ME>",
            "message": "Would you like an Iced Latte? You would be #{} in line.".format(str(order_count + 1)),
            "priority": 2,
            "retry": 120,
            "expire": 60,
            "callback": "https://coffee.henryfjordan.com/webhook"
        })
    )

if __name__ == '__main__':
    print(json.dumps(notify_henry(get_order_count()).json()))
