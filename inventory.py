#!/usr/bin/env python3

import json
import os

BUILD_SERVERS_IP_ADDR = os.environ.get("BUILD_SERVERS_IP_ADDR", "localhost")
SHARED_SERVICES_IP_ADDR = os.environ.get(
    "SHARED_SERVICES_IP_ADDR", "192.168.56.10"
)

inventory = {
    "build_servers": {
        "hosts": [BUILD_SERVERS_IP_ADDR],
        "vars": {"ansible_user": "jwynn"},
    },
    "shared_services": {
        "hosts": [SHARED_SERVICES_IP_ADDR],
        "vars": {"ansible_user": "jwynn"},
    },
}

print(json.dumps(inventory))
