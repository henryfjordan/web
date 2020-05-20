import json
import sys
import requests
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.form.get('acknowledged') == "1":
        r = requests.post(
            "https://<REPLACE ME>/slack/interactive",
            data={
                "payload": json.dumps({
                    "type": "dialog_submission",
                    "action_ts": datetime.timestamp(datetime.utcnow()),
                    "user": {
                        "id": "<REPLACE ME>",
                        "name": "<REPLACE ME>"
                    },
                    "channel": {
                        "id": "<REPLACE ME>"
                    },
                    "submission": {
                        "type": "iced",
                        "drink_type": "latte",
                        "shot_count": "2",
                        "syrup": None,
                        "milk": "dairy"
                    }
                })
            }
        )
        print("response", r.status_code, r.text, file=sys.stderr)
    
    return 'success'
