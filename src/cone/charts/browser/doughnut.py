from .chart import ChartTile


class DoughnutChartTile(ChartTile):
    """A doughnut chart.

    Refer to
    `documentation <https://www.chartjs.org/docs/4.0.1/charts/doughnut.html>`_
    for detailed information about valid options and data.
    """

    chart_type = 'doughnut'
    """Tell JavaScript side to render a doughnut chart."""

    @staticmethod
    def chart_data(model, request):
        """Doughnut chart data.

        Example:

        .. code-block:: python

            return {
                labels: [
                    'Red',
                    'Blue',
                    'Yellow'
                ],
                datasets: [{
                    'label': 'My First Dataset',
                    'data': [300, 50, 100],
                    'backgroundColor': [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)'
                    ]
                }]
            }
        """
        raise NotImplementedError(
            'Abstract ``DoughnutChartTile`` does not implement ``chart_data``'
        )
