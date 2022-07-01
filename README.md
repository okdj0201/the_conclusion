# TLDR;
This is a JOKE repository to operate [@okd_j](https://twitter.com/okd_j) as a bot.

# Version
v1.0.1 : Docker / Container support

# Features
* Tweets "しねない"
* Auto-reply with "しねない" for mentions.
  * Note: Automatic replies will be sent to accounts that are mutual followers and are not blocked or muted by okd_j.
* Auto favorite latest tweet of [@kinnnikun0917](https://twitter.com/kinnikun0917)

# Run with laptop Python
1. Set required key/secret/tokens to access twitter API as environment variable.
```
# Prepare env file
$ cat .env
export API_KEY="<Please obtain API key from twitter api>"
export API_SECRET="<Please obtain API secret from twitter api>"
export ACCESS_TOKEN="<Please obtain Access Token from twitter api>"
export ACCESS_TOKEN_SECRET="<Please obtain Access token secret from twitter>"
export BEARER_TOKEN="<Please obtain Bearer Token secret from twitter api>"

# Or create ~/.tweet_api.yml
api_key: "<Please obtain API key from twitter api>"
api_secret: "<Please obtain API secret from twitter api>"
api_access_token: "<Please obtain Access Token from twitter api>"
access_token_secret: "<Please obtain Access token secret from twitter>"
bearer_token: "<Please obtain Bearer Token secret from twitter api>"

```

2. Run script
```
$ source <env file>
$ cd bin
$ ./run_bot.sh
```

3. Kill bot(Optional)
```
$ cd bin
$ ./kill_bot.sh
```

# Run with Docker container
1. Prepare key/secret/tokens to access twitter API as environment variable.
```
# Prepare env file
# Note that You should remove double quote(") from environment file
$ cat ./.env_file
API_KEY=<Please obtain API key from twitter api>
API_SECRET=<Please obtain API secret from twitter api>
ACCESS_TOKEN=<Please obtain Access Token from twitter api>
ACCESS_TOKEN_SECRET=<Please obtain Access token secret from twitter>
BEARER_TOKEN=<Please obtain Bearer Token secret from twitter api>
```
2. Run container

```
$ cd bin
$ ./run_container.sh
```

3. You can find logs with container log.
```
$ cd bin
$ ./confirm_container_log.sh
```

# Run with Kubernetes
1. Edit yaml/pod.yaml
```
$ vim yaml/pod.yaml
..(snip)..
# Update here
+     env:
+       - name: API_KEY
+         value: <Please obtain API key from twitter api>
+       - name: API_SECRET
+         value: <Please obtain API secret from twitter api>
+       - name: ACCESS_TOKEN
+         value: <Please obtain Access Token from twitter api>
+       - name: ACCESS_TOKEN_SECRET
+         value: <Please obtain Access token secret from twitter>
+       - name: BEARER_TOKEN
+         value: <Please obtain Bearer Token secret from twitter api>
..(snip)..
```

2. Run
```
kubectl create -f yaml/pod.yaml
```

* If you are highly motivated, better to create ConfigMap of Secrets.

# Roadmap
* ~~Refactor~~ : Done
* ~~Load configuration from file.~~ : Done
* ~~Docker/Kubernetes support~~: Done
* AWS Labmda support
