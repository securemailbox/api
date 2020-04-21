#!/bin/bash
docker save securemailbox:latest > securemailbox.tar
sshpass -e scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null securemailbox.tar root@${DEPLOYMENT_TARGET}:/root/securemailbox.tar
sshpass -e ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@${DEPLOYMENT_TARGET} "docker load -i securemail.tar"
sshpass -e ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@${DEPLOYMENT_TARGET} "docker stop securemailbox"
sshpass -e ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@${DEPLOYMENT_TARGET} "docker run -d --name securemailbox --network host -e DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB} securemailbox:latest"
