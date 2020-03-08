# Overview

This charm installs the client to the Nextcloud file sharign system (https://nextcloud.com)

# Usage

If you are building this from source, checkout the source and run
```
charm build
```

If you are deploying it locally:
```
juju deploy /tmp/charm-builds/nextcloud-client --username <your nextcloud username> --password <your nextcloud password> --url <the url of your nextcloud installation>
```

If you are deploying it from the charm store (which may not exist...I may not submit this)

```
juju deploy ~g-clef/nextcloud-client
```


# Configuration

This charm will attempt to automatically configure the nextcloud client to connect to your nextcloud instance.
You should either include your username, password, and URL on the command line installation if you want this
to happen. If you don't, you'll have to ssh into the machine that it's installed on and reconfigure the client yourself.


# Contact Information

This charm was written by Aaron Gee-Clough <aaron (at) g-clef.net>

## Upstream Project Name

  - https://github.com/g-clef/charm-nextcloud-client

