from ConfigParser import RawConfigParser
import os
import sys


def read_config(path):
    config = RawConfigParser()
    config.optionxform = lambda s: s
    config.read(path)
    return config


def check_setuptools(port):
    path = os.path.expanduser('~/.pydistutils.cfg')
    url = 'http://localhost:%i' % port
    host = 'localhost:%i' % port
    failure = False
    if not os.path.exists(path):
        print "~/.pydistutils.cfg doesn't exist."
    else:
        config = read_config(path)
        if config.has_option('easy_install', 'index_url'):
            value = config.get('easy_install', 'index_url')
            if not value.startswith(url):
                print "ERROR: The index_url '%s' in the easy_install section of ~/.pydistutils.cfg doesn't start with '%s'." % (value, url)
                failure = True
        if config.has_option('easy_install', 'allow_hosts'):
            value = config.get('easy_install', 'allow_hosts')
            if host not in value:
                print "ERROR: The allow_hosts setting '%s' in the easy_install section of ~/.pydistutils.cfg doesn't contain '%s'." % (value, host)
                failure = True
    if not os.path.exists(path) or (not config.has_option('easy_install', 'index_url') and not failure):
        print "If you want to let setuptools use this devpi server by default, add the following section to ~/.pydistutils.cfg."
        print "[easy_install]"
        print "index_url = %s/[devpi user name]/[index name]/+simple/" % url
        print "allow_hosts = %s" % host
    else:
        print "~/.pydistutils.cfg seems to be fine."
    print


def check_pip(port):
    path = os.path.expanduser('~/.pip/pip.conf')
    url = 'http://localhost:%i' % port
    failure = False
    if not os.path.exists(path):
        print "~/.pip/pip.conf doesn't exist."
    else:
        config = read_config(path)
        if config.has_option('global', 'index-url'):
            value = config.get('global', 'index-url')
            if not value.startswith(url):
                print "ERROR: The index-url '%s' in the global section of ~/.pip/pip.conf doesn't start with '%s'." % (value, url)
                failure = True
    if not os.path.exists(path) or (not config.has_option('global', 'index-url') and not failure):
        print "If you want to let pip use this devpi server by default, add the following section to ~/.pip/pip.conf."
        print "[global]"
        print "index-url = %s/[devpi user name]/[index name]/+simple/" % url
    else:
        print "~/.pip/pip.conf seems to be fine."
    print


def check_buildout(port):
    path = os.path.expanduser('~/.buildout/default.cfg')
    url = 'http://localhost:%i' % port
    failure = False
    if not os.path.exists(path):
        print "~/.buildout/default.cfg doesn't exist."
    else:
        config = read_config(path)
        if config.has_option('buildout', 'index'):
            value = config.get('buildout', 'index')
            if not value.startswith(url):
                print "ERROR: The index '%s' in the buildout section of ~/.buildout/default.cfg doesn't start with '%s'." % (value, url)
                failure = True
    if not os.path.exists(path) or (not config.has_option('buildout', 'index') and not failure):
        print "If you want to let pip use this devpi server by default, add the following section to ~/.buildout/default.cfg."
        print "[buildout]"
        print "index = %s/[devpi user name]/[index name]/+simple/" % url
    else:
        print "~/.buildout/default.cfg seems to be fine."
    print


def check_launch_agent(base):
    if sys.platform == 'darwin':
        dest = os.path.expanduser('~/Library/LaunchAgents/devpi-server.plist')
        src = os.path.join(base, 'etc', 'devpi-server.plist')
        link = "ln -s %s %s" % (src, dest)
        if not os.path.exists(dest):
            print "WARNING: The launch agent information isn't linked."
            print "You can link it with:"
            print "  %s" % link
            return
        if os.path.islink(dest) and not os.readlink(dest) == src:
            print "WARNING: '%s' isn't linked to '%s'."
            print "You can link it with:"
            print "  %s" % link
            return
        print "The launch agent link seems to be fine."
        print


def main():
    base = os.environ['BUILDOUT_BASE']
    port = int(os.environ['DEVPI_PORT'])
    failure = False
    failure = failure or check_setuptools(port)
    failure = failure or check_pip(port)
    failure = failure or check_buildout(port)
    failure = failure or check_launch_agent(base)
    if failure:
        sys.exit(1)
