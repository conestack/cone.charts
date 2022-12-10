cone.charts
===========

**Chart.js intergration into cone.app**

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


Chart Tiles
-----------

Charts are implemented as chart
`tiles <https://github.com/conestack/cone.tile/>`_. Base classes for different
types chart types can be found in ``cone.charts.browser`` package.

For chart tile registration, an extended tile decorator is used, which
additionally to the tile registers a JSON view where the chart data gets
fetched from.

The following example shows how to implement a line chart:

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


API
---

Base Chart Tile
~~~~~~~~~~~~~~~

.. autoclass:: cone.charts.browser.chart.chart_tile
   :members:

.. autoclass:: cone.charts.browser.chart.ChartTile
   :members:


LineChart
~~~~~~~~~

.. autoclass:: cone.charts.browser.line.LineChartTile
   :members:


BarChart
~~~~~~~~

.. autoclass:: cone.charts.browser.bar.BarChartTile
   :members:


Polarchart
~~~~~~~~~~

.. autoclass:: cone.charts.browser.polar.PolarChartTile
   :members:


RadarChart
~~~~~~~~~~

.. autoclass:: cone.charts.browser.radar.RadarChartTile
   :members:


DoughnutChart
~~~~~~~~~~~~~

.. autoclass:: cone.charts.browser.doughnut.DoughnutChartTile
   :members:


PieChart
~~~~~~~~

.. autoclass:: cone.charts.browser.pie.PieChartTile
   :members:


ScatterChart
~~~~~~~~~~~~

.. autoclass:: cone.charts.browser.scatter.ScatterChartTile
   :members:


BubbleChart
~~~~~~~~~~~

.. autoclass:: cone.charts.browser.bubble.BubbleChartTile
   :members:


Javascript
----------

.. js:autoclass:: ChartTile
   :members:
        initialize,
        load,
        unload,
        destroy,
        on_before_load,
        on_data_loaded,
        create_chart


Source Code
-----------

The sources are in a GIT DVCS with its main branches at
`github <http://github.com/conestack/cone.charts>`_.


Copyright
---------

- Copyright (c) 2022 Cone Contributors


Table of Contents
-----------------

.. toctree::
    :maxdepth: 3


Contributors
------------

- Robert Niederreiter
- Torben Baungartner
- Lena Daxenbichler
