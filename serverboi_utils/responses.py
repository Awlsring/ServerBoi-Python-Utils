import requests


def post_temp_response(interaction_id: str, interaction_token: str):
    temp_response_url = f"https://discord.com/api/v8/interactions/{interaction_id}/{interaction_token}/callback"
    temp_response = {"type": 5, "data": {"flags": 64}}
    post_temp_response = requests.post(temp_response_url, json=temp_response)
    print(f"Temp Response: {post_temp_response}")


def edit_response(application_id: str, interaction_token: str, data: dict):
    print(f"Data: {data}")
    update_url = f"https://discord.com/api/webhooks/{application_id}/{interaction_token}/messages/@original"
    response = requests.patch(update_url, json=data)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Edit Response: {response}.")


def post_new_reponse(application_id: str, interaction_token: str, data: dict):
    print(f"Data: {data}")
    update_url = (
        f"https://discord.com/api/webhooks/{application_id}/{interaction_token}"
    )
    response = requests.post(update_url, json=data)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Edit Response: {response}.")


def form_response_data(**kwargs) -> dict:
    print(kwargs)
    embeds = kwargs.get("embeds")
    content = kwargs.get("content")
    components = kwargs.get("components")

    data = {"flags": 64}

    if embeds:
        data["embeds"] = []
        for embed in embeds:
            embed_dict = embed.to_dict()
            data["embeds"].append(embed_dict)

    if content:
        data["content"] = content

    if components:
        if components == "server":
            data["components"] = _server_components()

    return data

    if components and server_id:
        if components == "server":
            data["components"] = _server_components(server_id)

    return data


def _server_components(server_id: str) -> list:
    return [
        {
            "type": 1,
            "components": [
                {
                    "type": 2,
                    "label": "Start",
                    "style": 1,
                    "custom_id": f"{server_id}.start",
                    "emoji": {"id": None, "name": "🟢"},
                },
                {
                    "type": 2,
                    "label": "Stop",
                    "style": 1,
                    "custom_id": f"{server_id}.stop",
                    "emoji": {"id": None, "name": "🔴"},
                    "disabled": False,
                },
                {
                    "type": 2,
                    "label": "Reboot",
                    "style": 1,
                    "custom_id": f"{server_id}.restart",
                    "emoji": {"id": None, "name": "🔁"},
                    "disabled": False,
                },
            ],
        },
    ]
