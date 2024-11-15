import os
from dotenv import load_dotenv
from fastapi import FastAPI
from clerk_backend_api import Clerk, models

app = FastAPI()
load_dotenv()

# Initialize the Clerk instance
client = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

@app.get("/")
async def root():
    # Make a Clerk call to retrieve a list of users
    users = client.users.list()
    return {"users": users}

    # res = None
    # try:
    #     res = client.clients.verify(request={
    #         "token": "eyJhbGciOiJSUzI1NiIsImNhdCI6ImNsX0I3ZDRQRDExMUFBQSIsImtpZCI6Imluc18yb3RWZlV4d01GdUNQQjMwa3FramJ1ZUw5VjMiLCJ0eXAiOiJKV1QifQ.eyJhenAiOiJodHRwOi8vbG9jYWxob3N0OjUxNzMiLCJleHAiOjE3MzE2OTc3ODIsImlhdCI6MTczMTY5NzcyMiwiaXNzIjoiaHR0cHM6Ly9tZWFzdXJlZC1wb3Jwb2lzZS05Ni5jbGVyay5hY2NvdW50cy5kZXYiLCJuYmYiOjE3MzE2OTc3MTIsInNpZCI6InNlc3NfMm90bWFObW0waFJuT0tUdFN0RVRZdEh2a01UIiwic3ViIjoidXNlcl8yb3RtYVF2U2ZKQXNDTE1zSzd5ckhHTmFSbXgifQ.iwnTA3cAQkbejZHXJ2NJ-f5lzLdrg-kwp4YDa41V3v0t2kD9WYngsmOs07Gn3YeNAVI5gSnZOdwQTT5q3-uCXl_KAU4oc5Qr7dcyjcFsA_0v_EnNlQJIHA8MxTPI46lrl8_AqrmrLfjKnbZROM32Xi0-92fm_GyheWmrjJGy5H8yTLjb9eEnIn4ZmN2v9gvfeFp7mwGO62KtNDYjioly75ipXK3GreGKnfYTA8Pup_wNlw-biNGOW0QmGp8D1vAfdS-to48QWcQJLNe28iHhyPoeI2Ddz0c-IbsQ46bhojSO104wSTyPqeaVsWgwW_3Z8m_0gu_42575tvHnYxcz2A",
    #     })

    #     if res is not None:
    #         return res
    #         pass

    # except models.ClerkErrors as e:
    #     # handle e.data: models.ClerkErrorsData
    #     raise(e)
    # except models.SDKError as e:
    #     # handle exception
    #     raise(e)