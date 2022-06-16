from fastapi.testclient import TestClient
import json
import os

from app.main import app

DATA = {"vin": "1XP5DB9X7YN526158"}

PAYLOADS = [
  {"vin": "1XPWD40X1ED215307"},
  {"vin": "1XKWDB0X57J211825"},
  {"vin": "1XP5DB9X7YN526158"},
  {"vin": "4V4NC9EJXEN171694"},
  {"vin": "1XP5DB9X7XD487964"}
]

client = TestClient(app)

def test_read_main():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"healthCheck": "Server Running"}

def test_lookup():
  response = client.post("/lookup", json.dumps(DATA))
  assert response.status_code == 200
  assert response.json()['vin'] == '1Xp5Db9X7Yn526158'
  assert response.json()['make'] == 'PETERBILT'
  assert response.json()['model'] == '379'
  assert response.json()['year'] == '2000'
  assert response.json()['body'] == 'Truck-Tractor'

def test_invalid_length_lookup():
  data = {"vin": "1XP5DB9X7YN5261"}
  response = client.post("/lookup", json.dumps(data))
  assert response.status_code == 422
  assert response.json() == {
    "detail": [
        {
            "loc": [
                "body",
                "vin"
            ],
            "msg": "Must be 17 characters",
            "type": "value_error"
        }
    ],
    "body": {
        "vin": "1XP5DB9X7YN5261"
    }
  }

def test_not_alphanumeric_lookup():
  data = {"vin": "1XP5DB9X7YN52615!"}
  response = client.post("/lookup", json.dumps(data))
  assert response.status_code == 422
  assert response.json() == {
    "detail": [
        {
            "loc": [
                "body",
                "vin"
            ],
            "msg": "Must be alphanumeric",
            "type": "value_error"
        }
    ],
    "body": {
        "vin": "1XP5DB9X7YN52615!"
    }
}

def test_invalid_input_lookup():
  data = {"make": "1XP5DB9X7YN52615!"}
  response = client.post("/lookup", json.dumps(data))
  assert response.status_code == 422

def test_remove():
  client.post("/lookup", json.dumps(DATA))
  response = client.post("/remove", json.dumps(DATA))
  assert response.status_code == 200
  assert response.json() == {
    "vin": "1Xp5Db9X7Yn526158",
    "deleteSuccess": True
  }

def test_not_in_cache_remove():
  client.post("/lookup", json.dumps(DATA))
  invalid_data = {"vin": "1XP5DB9X7YN526157"}
  response = client.post("/remove", json.dumps(invalid_data))
  assert response.status_code == 404
  assert response.json() == {'detail': 'VIN not found'}

def test_export():
  for data in PAYLOADS:
    client.post("/lookup", json.dumps(data))
  
  response = client.get("/export")
  assert response.status_code == 200
  assert os.path.exists('vehicle_cache.parquet') == True