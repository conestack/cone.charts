from .chart import ChartTile


class PieChartTile(ChartTile):
    """A pie chart.

    Refer to
    `documentation <https://www.chartjs.org/docs/4.0.1/charts/doughnut.html#pie>`_
    for detailed information about valid options and data.
    """

    chart_type = 'pie'
    """Tell JavaScript side to render a pie chart."""

    @staticmethod
    def chart_data(model, request):
        """Pie chart data.

        Example:

        .. code-block:: python

            return {
                'labels': ['January', 'February', 'March']
                'datasets': [{
                    'label': 'Dataset 1',
                    'data': [10, 20, 30],
                    'borderColor': 'rgb(255, 99, 132)',
                    'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                }, {
                    'label': 'Dataset 2',
                    'data': [20, 10, 40],
                    'borderColor': 'rgb(54, 162, 235)',
                    'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                }]
            }
        """
        raise NotImplementedError(
            'Abstract ``PieChartTile`` does not implement ``chart_data``'
        )
