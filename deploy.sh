#!/bin/bash
if [[ -z "$POSTGRES_USER" ]]; then
  echo "POSTGRES_USER not set"
  exit 1
elif [[ -z "$POSTGRES_PASSWORD" ]]; then
  echo "POSTGRES_PASSWORD not set"
  exit 1
elif [[ -z "$POSTGRES_HOST" ]]; then
  echo "POSTGRES_HOST not set"
  exit 1
elif [[ -z "$POSTGRES_PORT" ]]; then
  echo "POSTGRES_PORT not set"
  exit 1
elif [[ -z "$POSTGRES_DB" ]]; then
  echo "POSTGRES_DB not set"
  exit 1
fi
SSH="sshpass -e ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
SCP="sshpass -e scp -r -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"

${SCP} securemailbox.tar root@${DEPLOYMENT_TARGET}:/root/securemailbox.tar
${SSH} root@${DEPLOYMENT_TARGET} "docker stop securemailbox"
${SSH} root@${DEPLOYMENT_TARGET} "docker rm securemailbox"
${SSH} root@${DEPLOYMENT_TARGET} "docker load -i securemailbox.tar"
${SSH} root@${DEPLOYMENT_TARGET} "docker run -d --name securemailbox --network host -e DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB} securemailbox:latest"
sleep 2
running=$( ${SSH} root@${DEPLOYMENT_TARGET} "docker inspect -f {{.State.Running}} securemailbox" )
if [[ $running = "true" ]]
then
  exit 0
else
  exit 1
fi
