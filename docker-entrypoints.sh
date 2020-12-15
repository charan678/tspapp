#!/bin/bash

if [ $1 == 'publisher' ]; then
    echo "Running publisher command"
    sleep 15s
    python -m  tspapp.publish.publisher_api
elif [ $1 == 'consumer' ]; then
    echo "Running Consumer command"
    sleep 10s
    python -m tspapp.consumer.consumer
else
    echo "invalid command"
fi