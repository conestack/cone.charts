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

* As chartjs libary, `Chart.js <https://www.chartjs.org/>`_ (v4.0.1) is included.

* For building time and date based charts,
  `Luxon <https://github.com/moment/luxon/>`_ (v3.0.3) is included.

* Adapter for Luxon for Chart-js `chartjs-adapter-luxon <https://github.com/chartjs/chartjs-adapter-luxon>`_ (v1.2.1).


Resources
---------

The following ``cone.charts`` related application configuration options are
available :

- **cone.charts.luxon**: Flag whether to disable ``Luxon``
  plugin. Defaults to `false`.


Usage
-----

The following example shows how to use ``cone.charts`` in a ``cone.app``
application.

.. code-block:: python

        
        from cone.charts.browser.chart.line import LineChartTile
        @chart_tile(
            name='my_fancy_linechart',
            interface=MyFancyModle,
            permission='view')
        class MyFancyLinechart(LineChartTile):

            @staticmethod
            def chart_data(model, request):

                def random_data():
                    data1 = []
                    data2 = []
                    for i in range(100):
                        data1.append([str(i), random.randint(0, 100)])
                    for i in range(50):
                        data2.append([str(i), random.randint(0, 100)])
                    return [data1, data2]
                data = random_data()

                # data layout = [[x1, y1], [x2, y2], ...] x = string, y = value
                # converted: {labels: [x1, x2, ...], datasets: [{data: [y1, y2, ...]}]}
                # we can have multiple datasets
                datasets = []
                for dataset in data:
                    color = 'rgb({},{},{})'.format(
                        *[random.randint(0, 255) for _ in range(3)])
                    datasets.append({
                        'data': [point[1] for point in dataset],
                        'borderColor': color,
                        'tension': 0.3,
                        'label': 'Dataset {}'.format(len(datasets) + 1),
                    })
                return {
                    'labels': [point[0] for point in data[0]],
                    'datasets': datasets,
                }

In the template file:

.. code:: XML

        <tal:chart replace="structure tile('my_fancy_linechart')">


Contributors
============

- Robert Niederreiter
- Torben Baumgartner

