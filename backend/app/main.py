from typing import Optional
from fastapi import FastAPI, HTTPException
import os
import requests

app = FastAPI()

HETZNER_API_URL = "https://dns.hetzner.com/api/v1/"
HETZNER_DNS_API_KEY = os.environ["HETZNER_DNS_API_KEY"]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q, "test_q": True}


@app.get("/update-dns/")
def update_dns(ip: str):
    return {ip}


@app.get("/info/")
def info():
    response = requests.get(
        url=f"{HETZNER_API_URL}zones",
        headers={
            "Auth-API-Token": HETZNER_DNS_API_KEY,
        },
    )
    print(f"Response HTTP Status Code: {response.status_code}")
    print(f"Response HTTP Response Body: {response.content}")
    if response.status_code != 200:
        print("HTTP Request failed")
        raise HTTPException(
            status_code=response.status_code, detail=f"{response.content}"
        )
    return response.content.decode("utf-8")
