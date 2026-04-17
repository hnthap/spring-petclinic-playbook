#!/usr/bin/env python3

import json
import os


CONTROL_IP_ADDR  = os.environ.get("CONTROL_IP_ADDR", "localhost")
TARGET_IP_ADDR = os.environ.get("TARGET_IP_ADDR", "192.168.56.10")

inventory = {
  "control": {
    "hosts": [CONTROL_IP_ADDR],
    "vars": { "ansible_connection": "local" }
  },
  "target": {
    "hosts": [TARGET_IP_ADDR],
    "vars": { "ansible_user": "jwynn" }
  }
}

print(json.dumps(inventory))
