#!/bin/bash

curl "http://localhost:8000/trips/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
