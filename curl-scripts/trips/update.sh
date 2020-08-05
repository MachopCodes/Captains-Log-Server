#!/bin/bash

curl "http://localhost:8000/trips/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "trip": {
      "tripStart": "'"${START}"'",
      "tripEnd": "'"${END}"'",
      "location": "'"${loc}"'"
    }
  }'

echo
