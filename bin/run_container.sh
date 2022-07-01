#!/bin/bash
echo ${ENV_FILE}
if [ ! -z ${ENV_FILE} -a -e ${ENV_FILE} ]; then
	echo "Starting Container with --env-file ${ENV_FILE}"
elif [ -e ../.env_file ]; then
	ENV_FILE="../.env_file"
	echo "Argument not found but ../env_file found. Starting container with --env-file ${ENV_FILE}"
else
	echo "Neither argument and default env-file found. Exitting..."
	exit 1
fi

docker rm -f  conclusion ; docker run --env-file=${ENV_FILE}  --name conclusion  -d okadajn0201/the_conclusion
