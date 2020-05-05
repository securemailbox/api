#!/bin/bash

# check for necessary env variables
if [[ -z "${POSTGRES_USER}" ]]; then
  echo "POSTGRES_USER not set"
  exit 1
elif [[ -z "${POSTGRES_PASSWORD}" ]]; then
  echo "POSTGRES_PASSWORD not set"
  exit 1
elif [[ -z "${POSTGRES_HOST}" ]]; then
  echo "POSTGRES_HOST not set"
  exit 1
elif [[ -z "${POSTGRES_PORT}" ]]; then
  echo "POSTGRES_PORT not set"
  exit 1
elif [[ -z "${POSTGRES_DB}" ]]; then
  echo "POSTGRES_DB not set"
  exit 1
elif [[ -z "${DEPLOY_TARGET}" ]]; then
  echo "DEPLOY_TARGET not set"
  exit 1
elif [[ -z "${DEPLOY_USER}" ]]; then
  echo "DEPLOY_USER not set"
  exit 1
fi

SSH="sshpass -e ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
SCP="sshpass -e scp -r -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
PROJECT=securemailboxes

# build flaskapp image defined in docker-compose.yml
docker-compose --project-name ${PROJECT} build --no-cache --parallel flaskapp

# Save image to a tar bundle
docker save $(docker image ls --format '{{ .Repository }}' | grep -oE "^${PROJECT}_\\w+\$") -o ${PROJECT}_deploy.tar

# Copy project files (namely: `docker-compose.yml`)
${SCP} docker-compose.yml ${DEPLOY_USER}@${DEPLOY_TARGET}:/

# Copy image to remote host
${SCP} ${PROJECT}_deploy.tar ${DEPLOY_USER}@${DEPLOY_TARGET}:/tmp/

# Load image on remote host
${SSH} ${DEPLOY_USER}@${DEPLOY_TARGET} "docker load --input /tmp/${PROJECT}_deploy.tar"

# Run container
${SSH} ${DEPLOY_USER}@${DEPLOY_TARGET} "export POSTGRES_USER=${POSTGRES_USER} && \
                                        export POSTGRES_PASSWORD=${POSTGRES_PASSWORD} && \
                                        export POSTGRES_HOST=${POSTGRES_HOST} && \
                                        export POSTGRES_PORT=${POSTGRES_PORT} && \
                                        export POSTGRES_DB=${POSTGRES_DB} && \
                                        docker-compose -p ${PROJECT} -f /docker-compose.yml up --no-deps -d flaskapp"

# make sure container has time to start up
sleep 2

# check container is running
CONTAINER=${PROJECT}_flaskapp_1
running=$( ${SSH} ${DEPLOY_USER}@${DEPLOY_TARGET} "docker inspect -f {{.State.Running}} ${CONTAINER}" )
if [[ $running = "true" ]]
then
  echo "Container now running" && exit 0
else
  echo "Expected container running state to be 'true' got '${running}'" && exit 1
fi

