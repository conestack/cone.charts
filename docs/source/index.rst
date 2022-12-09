cone.charts
===========

**Chart.js intergration into cone.app**


Overview
--------

Resources
^^^^^^^^^

The following ``cone.charts`` related application configuration options are
available:

- **cone.charts.luxon**: Flag whether ``Luxon`` resources are delivered to
  browser. Defaults to `false`.


Chart Tile
^^^^^^^^^^

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


API
---

Base Chart Tile
^^^^^^^^^^^^^^^

.. autoclass:: cone.charts.browser.chart.chart_tile
   :members:

.. autoclass:: cone.charts.browser.chart.ChartTile
   :members:


LineChart
^^^^^^^^^
.. autoclass:: cone.charts.browser.line.LineChartTile
   :members:


BarChart
^^^^^^^^
.. autoclass:: cone.charts.browser.bar.BarChartTile
   :members:


Polarchart
^^^^^^^^^^
.. autoclass:: cone.charts.browser.polar.PolarChartTile
   :members:


RadarChart
^^^^^^^^^^
.. autoclass:: cone.charts.browser.radar.RadarChartTile
   :members:


DoughnutChart
^^^^^^^^^^^^^
.. autoclass:: cone.charts.browser.doughnut.DoughnutChartTile
   :members:


PieChart
^^^^^^^^
.. autoclass:: cone.charts.browser.pie.PieChartTile
   :members:


ScatterChart
^^^^^^^^^^^^
.. autoclass:: cone.charts.browser.scatter.ScatterChartTile
   :members:


BubbleChart
^^^^^^^^^^^
.. autoclass:: cone.charts.browser.bubble.BubbleChartTile
   :members:


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
