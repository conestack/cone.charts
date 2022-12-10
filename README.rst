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
``cone.app``.

* Currently version v4.0.1 of ``Chart.js`` is included.

* For building time and date based charts,
  `Luxon <https://github.com/moment/luxon/>`_ v3.0.3 is included.

* For ``Luxon`` integration into ``Chart.js``,
  `chartjs-adapter-luxon <https://github.com/chartjs/chartjs-adapter-luxon>`_
  is required which is included in version v1.2.1.


Resources
---------

The following ``cone.charts`` related application configuration options are
available:

- **cone.charts.luxon**: Flag whether ``Luxon`` resources are delivered to
  browser. Defaults to `false`.


Chart Tile
----------

Some chart basic tiles are available in ``cone.charts``.

The following example shows how to implement a linechart:

.. code-block:: python

    from cone.charts.browser.chart import chart_tile
    from cone.charts.browser.chart import LineChartTile

    @chart_tile(
        name='my_linechart',
        interface=MyModel,
        permission='view')
    class MyLineChart(LineChartTile):

        @staticmethod
        def chart_data(model, request):
            return {
                'labels': ['Label 1', 'Label 2'],
                'datasets': [{
                    'data': [10, 20],
                    'borderColor': 'rgb(255,0,0)',
                    'tension': 0.3,
                    'label': 'Dataset Label',
                }],
            }

Please refer to the source code in ``cone.charts.browser`` package for
available chart tiles.


Contributors
============

- Robert Niederreiter
- Torben Baumgartner
- Lena Daxenbichler
