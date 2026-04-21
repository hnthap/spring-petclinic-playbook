#!/usr/bin/env python3

import json
import os

BUILD_SERVERS_IP_ADDR = os.environ.get("BUILD_SERVERS_IP_ADDR", "127.0.0.1")
SHARED_SERVICES_IP_ADDR = os.environ.get(
    "SHARED_SERVICES_IP_ADDR", "127.0.0.1"
)
PRODUCTION_APP_IP_ADDR = os.environ.get("PRODUCTION_APP_IP_ADDR", "127.0.0.1")

inventory = {
    "build_servers": {
        "hosts": [BUILD_SERVERS_IP_ADDR],
        "vars": {"ansible_user": "azureuser"},
    },
    "shared_services": {
        "hosts": [SHARED_SERVICES_IP_ADDR],
        "vars": {"ansible_user": "azureuser"},
    },
    "production_app": {
        "hosts": [PRODUCTION_APP_IP_ADDR],
        "vars": {"ansible_user": "azureuser"},
    },
}

print(json.dumps(inventory))
