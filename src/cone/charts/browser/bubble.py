from .chart import ChartTile


class BubbleChartTile(ChartTile):
    """A bubble chart.

    Refer to
    `documentation <https://www.chartjs.org/docs/4.0.1/charts/bubble.html>`_
    for detailed information about valid options and data.
    """

    chart_type = 'bubble'
    """Tell JavaScript side to render a bubble chart."""

    @staticmethod
    def chart_data(model, request):
        """Bubble chart data.

        Example:

        .. code-block:: python

            return {
                'datasets': [{
                    'label': 'Dataset',
                    'data': [{
                        x: 20,
                        y: 30,
                        r: 15
                    }, {
                        x: 40,
                        y: 10,
                        r: 10
                    }],
                    'backgroundColor': 'rgb(255, 99, 132)'
                }]
            }
        """
        raise NotImplementedError(
            'Abstract ``BubbleChartTile`` does not implement ``chart_data``'
        )
