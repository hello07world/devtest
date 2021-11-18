import requests

ALLIANZ_API_ENDPOINT = "https://apigw-dev.allianz.de/ldm/api/leads"
ALLIANZ_ACCESS_TOKEN_ENDPOINT = ("https://si-cim.allianz.de/auth/oauth2/realms/root/realms/eu1/access_token")
ALLIANZ_CLIENT_ID = "ppis1hqpgr2a7o9mks7kn6poih6vy83jbjbqh182"
ALLIANZ_CLIENT_SECRET = "r9w58r4yg03rdqwfqk2i"


def fetch_access_token():
    response = requests.post(
        (
            f"{ALLIANZ_ACCESS_TOKEN_ENDPOINT}"
            "?grant_type=client_credentials"
            "&scope=clientauth"
            f"&client_id={ALLIANZ_CLIENT_ID}"
            f"&client_secret={ALLIANZ_CLIENT_SECRET}"
        )
    )

    response = response.json()
    access_token = response.get("access_token", False)
    

    return access_token


access_token = fetch_access_token()

print(access_token)