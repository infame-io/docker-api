import docker
import json

client = docker.from_env()
events = client.events()

while True:
    for event in events:
        _event = json.loads(event.decode("utf-8"))

        action = _event.get("Action")
        if action and action in ["die", "start", "tag", "destroy", "create", "kill", "stop"]:
            print(_event)
