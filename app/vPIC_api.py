import httpx
from . import schemas

HOSTNAME = 'https://vpic.nhtsa.dot.gov/api/vehicles/'

# Access external vPIC API to decode vin input
def decode_vin(vin: str) -> list:
  params = {'format': 'json'}
  # vPIC API callout
  try:
    response = httpx.get(HOSTNAME + 'DecodeVin/' + vin, params=params)
  except httpx.RequestError as exc:
    print(f"An error occurred while requesting {exc.request.url!r}.")
  except httpx.HTTPStatusError as exc:
    print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
  
  results = response.json()
  return results['Results']

# Process and extract necessary information from decoded vin results
def process_decoded_vin(vin: str, response: dict) -> schemas.VehicleCreate:
  data = {}
  data['vin'] = vin
  data['in_cache'] = False
  
  for result in response:
    if result['Variable'] == 'Make':
      data['make'] = result['Value']
    elif result['Variable'] == 'Model':
      data['model'] = result['Value']
    elif result['Variable'] == 'Model Year':
      data['year'] = result['Value']
    elif result['Variable'] == 'Body Class':
      data['body'] = result['Value']
  
  data = schemas.VehicleCreate
  data.vin = vin

  for result in response:
    if result['Variable'] == 'Make':
      data.make = result['Value']
    elif result['Variable'] == 'Model':
      data.model = result['Value']
    elif result['Variable'] == 'Model Year':
      data.year = result['Value']
    elif result['Variable'] == 'Body Class':
      data.body = result['Value']
    
  return data

