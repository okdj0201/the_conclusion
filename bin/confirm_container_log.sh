docker ps -a | grep conclusion | awk '{print }' | xargs docker logs
