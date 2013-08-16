devpi buildout
==============

This buildout sets up `devpi-server`_.
It will run on ``http://localhost:8141``.

On OS X you can then use ``launchctl load -w etc/devpi-server.plist`` to let it run automatically.

On systems with cron you can also use the line generated in ``etc/crontab.devpid``

.. _`devpi-server`: http://devpi.net
