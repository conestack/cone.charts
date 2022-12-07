from .chart import ChartTile


class RadarChartTile(ChartTile):
    """ Tile rendering a radar chart."""

    chart_type = 'radar'
    """Setting chart type to 'radar'."""

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.

        Refer to chart.js documentation for more information.
        `radar chart documentation 
        <https://www.chartjs.org/docs/4.0.1/charts/radar.html>`_
        
        Example:
        .. code-block:: python

            return {
                labels: [
                    'Eating',
                    'Drinking',
                    'Sleeping',
                    'Designing',
                    'Coding',
                    'Cycling',
                    'Running'
                ],
                datasets: [{
                    label: 'My First Dataset',
                    data: [65, 59, 90, 81, 56, 55, 40]
                }, {
                    label: 'My Second Dataset',
                    data: [28, 48, 40, 19, 96, 27, 100]
                }]
            }
        """
        raise NotImplementedError('Chart data not implemented')
