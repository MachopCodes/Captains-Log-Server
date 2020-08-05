#!/bin/bash

curl "http://localhost:8000/trips/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
