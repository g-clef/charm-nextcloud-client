# Overview

This charm installs the client to the Nextcloud file sharing system (https://nextcloud.com). 

# Usage

If you are building this from source, checkout the source and run
```
charm build
```

If you are deploying it locally:
```
juju deploy /tmp/charm-builds/nextcloud-client --config username=<your nextcloud username> --config password=<your nextcloud password> --config url=<the url of your nextcloud installation>
```

If you are deploying it from the charm store (which may not exist...I may not submit this)

```
juju deploy ~cs:g-clef/nextcloud-client
```
You'll want to use the same options as above.

# Configuration

This charm will attempt to automatically configure the nextcloud client to connect to your nextcloud instance.
You should either include your username, password, and URL on the command line installation if you want this
to happen. If you don't, you'll have to ssh into the machine that it's installed on and reconfigure the client 
cron job manually.

`--username` is the username the system will use to log in to your nextcloud installation
`--password` is for the password used to log into 
`--url` is the URL of your nextcloud installation
`--directory` is the directory to save file in to (default `~/nextcloud`)

Note: the vanilla nextcloud client wants a GUI (which it won't have here) and the command-line
client won't re-run periodically., so this charm installs a cron job to run the nextcloud command 
client periodically. This means your username & password will be visibile
in a `ps` command on the server, as it's required by the `nextcloudcmd` executable.

# Contact Information

This charm was written by Aaron Gee-Clough <aaron (at) g-clef.net>

## Upstream Project Name

  - https://github.com/g-clef/charm-nextcloud-client

