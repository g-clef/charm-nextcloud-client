from charms.reactive import when_not, set_flag
from charmhelpers.fetch import configure_sources, apt_install
from charmhelpers.core.hookenv import config
from charmhelpers.core.host import mkdir, write_file, chownr
import subprocess


@when_not('nextcloud-client.installed')
def install_nextcloud_client():
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    configure_sources(update=True)
    apt_install("nextcloud-client")
    username = config().get('username')
    password = config().get("password")
    directory = config().get("directory")
    url = config().get("url")
    target_dir = "/home/ubuntu/{}".format(directory)
    mkdir(target_dir, perms=0o755)
    chownr(target_dir, "ubuntu", "ubuntu", chowntopdir=True)

    shell_script = """#!/bin/bash
/usr/bin/nextcloudcmd --user {} --password {} /home/ubuntu/{} {}
""".format(username, password, directory, url)

    write_file("/home/ubuntu/nextcloud-client.sh", shell_script, owner="ubuntu", group="ubuntu", perms=0o755)
    crontab = "0 * * * * /home/ubuntu/nextcloud-client.sh"
    command = "/bin/echo '{}' | /usr/bin/crontab - ".format(crontab)
    subprocess.call(["su", "ubuntu", "-c", command])
    set_flag('nextcloud-client.installed')
