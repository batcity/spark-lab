#!/usr/bin/env bash

PORT=9999

echo "Listening on localhost:$PORT..."

i=0
while (( i < 100 )); do
    echo "$i"
    ((i += 10))
    sleep 1
done | nc -l -p $PORT