#!/bin/sh

docker-compose -f ../docker-compose.e2e.yml down -v
docker-compose -f ../docker-compose.e2e.yml up --build