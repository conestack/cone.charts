.. image:: https://img.shields.io/pypi/v/cone.charts.svg
    :target: https://pypi.python.org/pypi/cone.charts
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/cone.charts.svg
    :target: https://pypi.python.org/pypi/cone.charts
    :alt: Number of PyPI downloads

.. image:: https://github.com/conestack/cone.charts/actions/workflows/python-package.yml/badge.svg
    :target: https://github.com/conestack/cone.charts/actions/workflows/python-package.yml
    :alt: Package build

.. image:: https://coveralls.io/repos/github/bluedynamics/cone.charts/badge.svg?branch=master
    :target: https://coveralls.io/github/bluedynamics/cone.charts?branch=master

This package provides `Chart.js <https://www.chartjs.org/>`_ integration in to
cone.app.

* As maps library, `Leaflet JS <https://leafletjs.com/>`_ (v1.7.1) is included.

* For avoiding 1px gap between tiles,
  `Leaflet.TileLayer.NoGap <https://github.com/Leaflet/Leaflet.TileLayer.NoGap>`_
  `(ab4f107) <https://github.com/Leaflet/Leaflet.TileLayer.NoGap/commit/ab4f107fecb80e12ffbdc4ebbedf5f85b8da7173>`_ is included.
  
* As chartjs libary, `Chart.js <https://www.chartjs.org/>`_ (v3.9.1) is included.

* For building time and date based charts,
    `Luxon <https://github.com/moment/luxon/>`_ (v3.0.3)
    A library for working with dates and times in JS.

* Adapter for Luxon for Chart-js,
    `chartjs-adapter-luxon <https://github.com/chartjs/chartjs-adapter-luxon>`_ (v3.0.3).


Resources
---------

The following ``cone.charts`` related application configuration options are
available :

- **cone.charts.luxon**: Flag whether date and/or time based chats can be 
    generated. Defaults to `true`.

Contributors
============

- Robert Niederreiter
- Torben Baumgartner
