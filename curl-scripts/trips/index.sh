#!/bin/bash

curl "http://localhost:8000/trips" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
