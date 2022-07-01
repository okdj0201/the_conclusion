docker ps -a | grep conclusion | awk '{print $2}' | xargs docker logs
