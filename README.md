# TLDR;
This is a JOKE repository to operate [@okd_j](https://twitter.com/okd_j) as a bot.

# Version
v0.0.1 : Laptop edition

# Features
* Tweets "しねない"
* Auto-reply with "しねない" for mentions.
  * Note: Automatic replies will be sent to accounts that are mutual followers and are not blocked or muted by okd_j.

# Quick start
1. Set required key/secret/tokens to access twitter API as environment variable.
```
# Prepare env file
$ cat .env
export API_KEY="<Please obtain API key from twitter api>"
export API_SECRET="<Please obtain API secret from twitter api>"
export ACCESS_TOKEN="<Please obtain Access Token from twitter api>"
export ACCESS_TOKEN_SECRET="<Please obtain Access token secret from twit

export BEARER_TOKEN="<Please obtain Bearer Token secret from twitter api>


```

2. Run script
```
$ source <env file>
$ cd bin
$ ./run_all.sh
```

# Roadmap
* Load configuration from file.
* Docker/Kubernetes support
* AWS Labmda support
