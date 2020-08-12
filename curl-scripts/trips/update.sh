#!/bin/bash

curl "http://localhost:8000/trips/${ID}" \
  --include \
  --request PATCH \
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
