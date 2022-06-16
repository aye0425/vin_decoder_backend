# VIN Decoding Server

Simple FastAPI backend to decode VINs, powered by the vPIC API and backed by a SQLite cache.

## Description

This is a fastAPI backend with three routes:

`/lookup`

This route will first check the SQLite database to see if a cached result is available. If so, it should be returned
from the database.

The response object will contain the following elements:

- Input VIN Requested (string, exactly 17 alphanumeric characters)
- Make (String)
- Model (String)
- Model Year (String)
- Body Class (String)
- Cached Result? (Boolean)

`/remove`

This route will remove a entry from the cache.

`/export`

This route will export the SQLite database cache and return a binary file (parquet format) containing the data in the
cache.

### Dependencies

Python Version: 3.8.13
### Installing

Run 'pip install -r requirements.txt' to get all libraries used

### Executing program

Run 'python -m app.main' in terminal to start server

Run 'pytest' to execute tests

Run 'pytest --cov=app tests/' to get a coverage report