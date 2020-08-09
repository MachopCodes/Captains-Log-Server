#!/bin/bash

curl "http://localhost:8000/trips" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "trip": {
      "launchDate": "'"${START}"'",
      "latitude": "'"${LAT}"'",
      "longitude": "'"${LON}"'"
    }
  }'

echo
