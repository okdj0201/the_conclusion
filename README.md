# TLDR;
This is a JOKE repository to operate [@okd_j](https://twitter.com/okd_j) as a bot.

# Version
v0.0.1 : Laptop support

# Features
* Tweets "しねない"
* Auto-reply with "しねない" for mentions.
  * Note: Automatic replies will be sent to accounts that are mutual followers and are not blocked or muted by okd_j.
* Auto favorite latest tweet of [@kinnnikun0917](https://twitter.com/kinnikun0917)

# Quick start
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

# Roadmap
* Refactor
* Load configuration from file.
* Docker/Kubernetes support
* AWS Labmda support
