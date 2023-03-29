#!/usr/bin/env python3

import json
import requests
import sys
import time

GRAPH_VERSION = "v1.0"
BASE_URL = f"https://login.microsoft.com"

non_admin_graph_apis = """
{
"requiredResourceAccess": {
        "resourceAppId": "00000003-0000-0000-c000-000000000000",
        "resourceAccess": [
            {
                "id": "cd87405c-5792-4f15-92f7-debc0db6d1d6",
                "type": "Scope"
            },
            {
                "id": "14dad69e-099b-42c9-810b-d002981feec1",
                "type": "Scope"
            },
            {
                "id": "8d3c54a7-cf58-4773-bf81-c0cd6ad522bb",
                "type": "Scope"
            },
            {
                "id": "395dfec1-a0b9-465f-a783-8250a430cb8c",
                "type": "Scope"
            },
            {
                "id": "110e5abb-a10c-4b59-8b55-9b4daa4ef743",
                "type": "Scope"
            },
            {
                "id": "7ab1d787-bae7-4d5d-8db6-37ea32df9186",
                "type": "Scope"
            },
            {
                "id": "a4b8392a-d8d1-4954-a029-8e668a39a170",
                "type": "Scope"
            },
            {
                "id": "4ad84827-5578-4e18-ad7a-86530b12f884",
                "type": "Scope"
            },
            {
                "id": "3a1e4806-a744-4c70-80fc-223bf8582c46",
                "type": "Scope"
            },
            {
                "id": "f501c180-9344-439a-bca0-6cbf209fd270",
                "type": "Scope"
            },
            {
                "id": "9ff7295e-131b-4d94-90e1-69fde507ac11",
                "type": "Scope"
            },
            {
                "id": "570282fd-fa5c-430d-a7fd-fc8dc98a9dca",
                "type": "Scope"
            },
            {
                "id": "7427e0e9-2fba-42fe-b0c0-848c9e6a8182",
                "type": "Scope"
            },
            {
                "id": "9769c687-087d-48ac-9cb3-c37dde652038",
                "type": "Scope"
            },
            {
                "id": "89497502-6e42-46a2-8cb2-427fd3df970a",
                "type": "Scope"
            },
            {
                "id": "47607519-5fb1-47d9-99c7-da4b48f369b1",
                "type": "Scope"
            },
            {
                "id": "367492fc-594d-4972-a9b5-0d58c622c91c",
                "type": "Scope"
            },
            {
                "id": "818c620a-27a9-40bd-a6a5-d96f7d610b4b",
                "type": "Scope"
            },
            {
                "id": "bac3b9c2-b516-4ef4-bd3b-c2ef73d8d804",
                "type": "Scope"
            },
            {
                "id": "11d4cd79-5ba5-460f-803f-e22c8ab85ccd",
                "type": "Scope"
            },
            {
                "id": "64ac0503-b4fa-45d9-b544-71a463f05da0",
                "type": "Scope"
            },
            {
                "id": "dfabfca6-ee36-4db2-8208-7a28381419b3",
                "type": "Scope"
            },
            {
                "id": "615e26af-c38a-4150-ae3e-c3b0d4cb1d6a",
                "type": "Scope"
            },
            {
                "id": "371361e4-b9e2-4a3f-8315-2a301a3b0a3d",
                "type": "Scope"
            },
            {
                "id": "ed68249d-017c-4df5-9113-e684c7f8760b",
                "type": "Scope"
            },
            {
                "id": "9d822255-d64d-4b7a-afdb-833b9a97ed02",
                "type": "Scope"
            },
            {
                "id": "87f447af-9fa4-4c32-9dfa-4a57a73d18ce",
                "type": "Scope"
            },
            {
                "id": "5447fe39-cb82-4c1a-b977-520e67e724eb",
                "type": "Scope"
            },
            {
                "id": "17dde5bd-8c17-420f-a486-969730c1b827",
                "type": "Scope"
            },
            {
                "id": "8019c312-3263-48e6-825e-2b833497195b",
                "type": "Scope"
            },
            {
                "id": "89fe6a52-be36-487e-b7d8-d061c450a026",
                "type": "Scope"
            },
            {
                "id": "c5ddf11b-c114-4886-8558-8a4e557cd52b",
                "type": "Scope"
            },
            {
                "id": "88d21fd4-8e5a-4c32-b5e2-4a1c95f34f72",
                "type": "Scope"
            },
            {
                "id": "afb6c84b-06be-49af-80bb-8f3f77004eab",
                "type": "Scope"
            },
            {
                "id": "242b9d9e-ed24-4d09-9a52-f43769beb9d4",
                "type": "Scope"
            },
            {
                "id": "12466101-c9b8-439a-8589-dd09ee67e8e9",
                "type": "Scope"
            },
            {
                "id": "2b9c4092-424d-4249-948d-b43879977640",
                "type": "Scope"
            },
            {
                "id": "a367ab51-6b49-43bf-a716-a1fb06d2a174",
                "type": "Scope"
            },
            {
                "id": "5df07973-7d5d-46ed-9847-1271055cbd51",
                "type": "Scope"
            },
            {
                "id": "7b9103a5-4610-446b-9670-80643382c1fa",
                "type": "Scope"
            },
            {
                "id": "e1fe6dd8-ba31-4d61-89e7-88639da4683d",
                "type": "Scope"
            },
            {
                "id": "b4e74841-8e56-480b-be8b-910348b18b4c",
                "type": "Scope"
            },
            {
                "id": "b340eb25-3456-403f-be2f-af7a0d370277",
                "type": "Scope"
            },
            {
                "id": "024d486e-b451-40bb-833d-3e66d98c5c73",
                "type": "Scope"
            },
            {
                "id": "e383f46e-2787-4529-855e-0e479a3ffac0",
                "type": "Scope"
            },
            {
                "id": "465a38f9-76ea-45b9-9f34-9e8b0d4b0b42",
                "type": "Scope"
            },
            {
                "id": "1ec239c2-d7c9-4623-a91a-a9775856bb36",
                "type": "Scope"
            },
            {
                "id": "ff74d97f-43af-4b68-9f2a-b77ee6968c5d",
                "type": "Scope"
            },
            {
                "id": "d56682ec-c09e-4743-aaf4-1a3aac4caa21",
                "type": "Scope"
            },
            {
                "id": "10465720-29dd-4523-a11a-6a75c743c9d9",
                "type": "Scope"
            },
            {
                "id": "5c28f0bf-8a70-41f1-8ab2-9032436ddb65",
                "type": "Scope"
            },
            {
                "id": "df85f4d6-205c-4ac5-a5ea-6bf408dba283",
                "type": "Scope"
            },
            {
                "id": "863451e7-0667-486c-a5d6-d135439485f0",
                "type": "Scope"
            },
            {
                "id": "205e70e5-aba6-4c52-a976-6d2d46c48043",
                "type": "Scope"
            },
            {
                "id": "37f7f235-527c-4136-accd-4a02d197296e",
                "type": "Scope"
            },
            {
                "id": "64a6cdd6-aab1-4aaf-94b8-3cc8405e90d0",
                "type": "Scope"
            },
            {
                "id": "ba47897c-39ec-4d83-8086-ee8256fa737d",
                "type": "Scope"
            },
            {
                "id": "65e50fdc-43b7-4915-933e-e8138f11f40a",
                "type": "Scope"
            },
            {
                "id": "33b1df99-4b29-4548-9339-7a7b83eaeebc",
                "type": "Scope"
            },
            {
                "id": "02a5a114-36a6-46ff-a102-954d89d9ab02",
                "type": "Scope"
            },
            {
                "id": "948eb538-f19d-4ec5-9ccc-f059e1ea4c72",
                "type": "Scope"
            },
            {
                "id": "7f36b48e-542f-4d3b-9bcb-8406f0ab9fdb",
                "type": "Scope"
            },
            {
                "id": "ff91d191-45a0-43fd-b837-bd682c4a0b0f",
                "type": "Scope"
            },
            {
                "id": "f534bf13-55d4-45a9-8f3c-c92fe64d6131",
                "type": "Scope"
            },
            {
                "id": "9be106e1-f4e3-4df5-bdff-e4bc531cbe43",
                "type": "Scope"
            },
            {
                "id": "a65f2972-a4f8-4f5e-afd7-69ccb046d5dc",
                "type": "Scope"
            },
            {
                "id": "0e755559-83fb-4b44-91d0-4cc721b9323e",
                "type": "Scope"
            },
            {
                "id": "2b61aa8a-6d36-4b2f-ac7b-f29867937c53",
                "type": "Scope"
            },
            {
                "id": "ebf0f66e-9fb1-49e4-a278-222f76911cf4",
                "type": "Scope"
            },
            {
                "id": "26e2f3e8-b2a1-47fc-9620-89bb5b042024",
                "type": "Scope"
            },
            {
                "id": "652390e4-393a-48de-9484-05f9b1212954",
                "type": "Scope"
            },
            {
                "id": "d7b7f2d9-0f45-4ea1-9d42-e50810c06991",
                "type": "Scope"
            },
            {
                "id": "258f6531-6087-4cc4-bb90-092c5fb3ed3f",
                "type": "Scope"
            },
            {
                "id": "485be79e-c497-4b35-9400-0e3fa7f2a5d4",
                "type": "Scope"
            },
            {
                "id": "9d8982ae-4365-4f57-95e9-d6032a4c0b87",
                "type": "Scope"
            },
            {
                "id": "76bc735e-aecd-4a1d-8b4c-2b915deabb79",
                "type": "Scope"
            },
            {
                "id": "9c7a330d-35b3-4aa1-963d-cb2b9f927841",
                "type": "Scope"
            },
            {
                "id": "88e58d74-d3df-44f3-ad47-e89edf4472e4",
                "type": "Scope"
            },
            {
                "id": "ed11134d-2f3f-440d-a2e1-411efada2502",
                "type": "Scope"
            },
            {
                "id": "248f5528-65c0-4c88-8326-876c7236df5e",
                "type": "Scope"
            },
            {
                "id": "6a71a747-280f-4670-9ca0-a9cbf882b274",
                "type": "Scope"
            },
            {
                "id": "b81dd597-8abb-4b3f-a07a-820b0316ed04",
                "type": "Scope"
            },
            {
                "id": "6f2d22f2-1cb6-412c-a17c-3336817eaa82",
                "type": "Scope"
            },
            {
                "id": "3db89e36-7fa6-4012-b281-85f3d9d9fd2e",
                "type": "Scope"
            },
            {
                "id": "bf3fbf03-f35f-4e93-963e-47e4d874c37a",
                "type": "Scope"
            },
            {
                "id": "c395395c-ff9a-4dba-bc1f-8372ba9dca84",
                "type": "Scope"
            },
            {
                "id": "7825d5d6-6049-4ce7-bdf6-3b8d53f4bcd0",
                "type": "Scope"
            },
            {
                "id": "50f66e47-eb56-45b7-aaa2-75057d9afe08",
                "type": "Scope"
            },
            {
                "id": "328438b7-4c01-4c07-a840-e625a749bb89",
                "type": "Scope"
            },
            {
                "id": "633e0fce-8c58-4cfb-9495-12bbd5a24f7c",
                "type": "Scope"
            },
            {
                "id": "116b7235-7cc6-461e-b163-8e55691d839e",
                "type": "Scope"
            },
            {
                "id": "9547fcb5-d03f-419d-9948-5928bbf71b0f",
                "type": "Scope"
            },
            {
                "id": "5252ec4e-fd40-4d92-8c68-89dd1d3c6110",
                "type": "Scope"
            },
            {
                "id": "2219042f-cab5-40cc-b0d2-16b1540b4c5f",
                "type": "Scope"
            },
            {
                "id": "f45671fb-e0fe-4b4b-be20-3d3ce43f1bcb",
                "type": "Scope"
            },
            {
                "id": "cdcdac3a-fd45-410d-83ef-554db620e5c7",
                "type": "Scope"
            },
            {
                "id": "c37c9b61-7762-4bff-a156-afc0005847a0",
                "type": "Scope"
            },
            {
                "id": "38826093-1258-4dea-98f0-00003be2b8d0",
                "type": "Scope"
            },
            {
                "id": "5fa075e9-b951-4165-947b-c63396ff0a37",
                "type": "Scope"
            },
            {
                "id": "21f0d9c0-9f13-48b3-94e0-b6b231c7d320",
                "type": "Scope"
            },
            {
                "id": "e9fdcbbb-8807-410f-b9ec-8d5468c7c2ac",
                "type": "Scope"
            },
            {
                "id": "c3ba73cd-1333-4ac0-9eb6-da00cf298dad",
                "type": "Scope"
            },
            {
                "id": "f73fa04f-b9a5-4df9-8843-993ce928925e",
                "type": "Scope"
            },
            {
                "id": "fd5353c6-26dd-449f-a565-c4e16b9fce78",
                "type": "Scope"
            },
            {
                "id": "68a3156e-46c9-443c-b85c-921397f082b5",
                "type": "Scope"
            },
            {
                "id": "44e060c4-bbdc-4256-a0b9-dcc0396db368",
                "type": "Scope"
            },
            {
                "id": "60382b96-1f5e-46ea-a544-0407e489e588",
                "type": "Scope"
            },
            {
                "id": "b11fa0e7-fdb7-4dc9-b1f1-59facd463480",
                "type": "Scope"
            },
            {
                "id": "9084c10f-a2d6-4713-8732-348def50fe02",
                "type": "Scope"
            },
            {
                "id": "ba22922b-752c-446f-89d7-a2d92398fceb",
                "type": "Scope"
            },
            {
                "id": "4051c7fc-b429-4804-8d80-8f1f8c24a6f7",
                "type": "Scope"
            },
            {
                "id": "27608d7c-2c66-4cad-a657-951d575f5a60",
                "type": "Scope"
            }
        ]
    }
}
"""

def authenticate_device_code_flow(tenant_id:str, client_id:str, scope:str):

    device_code_url = f"{BASE_URL}/{tenant_id}/oauth2/v2.0/devicecode"
    token_url = f"{BASE_URL}/{tenant_id}/oauth2/v2.0/token"

    headers = {}
    headers['Content-Type'] = "application/x-www-form-urlencoded"

    payload = {}
    payload['client_id'] = client_id
    payload['scope'] = scope

    try:
        dc_resp = requests.post(device_code_url, headers=headers, data=payload)
        
        verification_data = json.loads(dc_resp.content)
        try:
            polling_interval_seconds = verification_data['interval']
            verification_uri = verification_data['verification_uri']
            user_code = verification_data['user_code']
            device_code = verification_data['device_code']
        except KeyError as e:
            print("[!] Missing expected keys")
            print(dc_resp.content)

        auth_body = {}
        auth_body['grant_type'] = "urn:ietf:params:oauth:grant-type:device_code"
        auth_body['client_id'] = client_id
        auth_body['device_code'] = device_code

        print(verification_data['message'])

        while (True):
            print("[*] Waiting for device code")
            time.sleep(int(polling_interval_seconds))

            try:
                resp = requests.post(token_url, headers=headers, data=auth_body)
                if resp.status_code == 200:
                    return json.loads(resp.content)
                elif resp.status_code == 400:
                    continue
                else:
                    print(resp)
            except requests.exceptions.HTTPError as e:
                print(e)
                return
            

    except requests.exceptions.HTTPError as e:
        print(f"[!] Error getting device code: {str(e)}")

def authenticate_client_credentials_flow(tenant_id, client_id, client_secret, assertion, obo=True, backend_scope="https://graph.microsoft.com/.default"):
    token_url = f"{BASE_URL}/{tenant_id}/oauth2/v2.0/token"
    headers = {}
    headers['Content-Type'] = "application/x-www-form-urlencoded"

    body = {}
    body['client_id'] = client_id
    body['client_secret'] = client_secret
    
    body['scope'] = f"{backend_scope} offline_access"
    if obo:
        body['requested_token_use'] = "on_behalf_of"
        body['assertion'] = assertion
        body['grant_type'] = "urn:ietf:params:oauth:grant-type:jwt-bearer"
    else:
        body['refresh_token'] = assertion
        body['grant_type'] = "refresh_token"


    try:
        auth_resp = requests.post(token_url, headers=headers, data=body)
        if auth_resp.status_code == 200:
            creds = json.loads(auth_resp.content)
            return creds
        else:
            print(auth_resp.content)
    except requests.exceptions.HTTPError as e:
        print(f"[!] Error OBO Auth: {str(e)}")
        return None

def obo_existing_application(tenant_id, client_id, client_secret):

    frontend_creds = authenticate_device_code_flow(tenant_id, client_id, f"{client_id}/.default")
    token = frontend_creds['access_token']
    backend_creds = authenticate_client_credentials_flow(tenant_id, client_id, client_secret, token)
    return backend_creds
