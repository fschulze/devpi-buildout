devpi buildout
==============

This buildout sets up `devpi-server`_.
It will run on ``http://localhost:8141``.

On OS X you can symlink ``etc/devpi-server.plist`` into ``~/Library/LaunchAgents/`` with::

  ln -s $(pwd)/etc/devpi-server.plist ~/Library/LaunchAgents/

and then use::

  launchctl load -w ~/Library/LaunchAgents/devpi-server.plist

to let it run automatically.

On systems with cron you can also use the line generated in ``etc/crontab.devpid``

.. _`devpi-server`: http://devpi.net
