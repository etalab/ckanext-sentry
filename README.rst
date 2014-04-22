Sentry CKAN extension
======================

The Sentry CKAN extension add `Sentry`_ middleware from raven package into the CKAN middlewares.


To install the plugin, enter your virtualenv and load the source:

.. code-block:: bash

    $ pip install ckanext-sentry

Activate the plugin and add its configuration (prefixed by ``sentry.``) to your CKAN .ini file:

.. code-block:: ini

    ckan.plugins = sentry <other-plugins>
    sentry.dsn = https://xxxxxx:xxxxxx@sentry.domain.com/1


You can see a full list of parameters on the `official Raven documentation`_.


.. _Sentry: http://getsentry.com/
.. _official Raven documentation: http://raven.readthedocs.org/en/latest/
