from charms.reactive import when, when_not, set_flag
from charmhelpers.fetch import configure_sources, apt_install


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
    set_flag('nextcloud-client.installed')
