from .chart import ChartTile


class ScatterChartTile(ChartTile):
    """A scatter chart.

    Refer to
    `documentation <https://www.chartjs.org/docs/4.0.1/charts/scatter.html>`_
    for detailed information about valid options and data.
    """

    chart_type = 'scatter'
    """Tell JavaScript side to render a scatter chart."""

    @staticmethod
    def chart_data(model, request):
        """Scatter chart data.

        Example:

        .. code-block:: python

            return {
                'datasets': [{
                    'label': 'Dataset',
                    'data': [{
                        x: -10,
                        y: 0
                    }, {
                        x: 0,
                        y: 10
                    }, {
                        x: 10,
                        y: 5
                    }, {
                        x: 0.5,
                        y: 5.5
                    }],
                    'backgroundColor': 'rgb(255, 99, 132)'
                }],
            }
        """
        raise NotImplementedError(
            'Abstract ``ScatterChartTile`` does not implement ``chart_data``'
        )
