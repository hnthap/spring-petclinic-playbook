#!/usr/bin/env python3

import json
import os

BUILD_SERVERS_IP_ADDR = os.environ["BUILD_SERVERS_IP_ADDR"]
SHARED_SERVICES_IP_ADDR = os.environ["SHARED_SERVICES_IP_ADDR"]
PRODUCTION_APP_IP_ADDR = os.environ["PRODUCTION_APP_IP_ADDR"]

inventory = {  # pyright: ignore[reportUnknownVariableType]
    "_meta": {"hostvars": {}},
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
