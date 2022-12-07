from .chart import ChartTile


class LineChartTile(ChartTile):
    """A line chart.

    Refer to
    `documentation <https://www.chartjs.org/docs/4.0.1/charts/line.html>`_
    for detailed information about valid options and data.
    """

    chart_type = 'line'
    """Tell JavaScript side to render a line chart."""

    @staticmethod
    def chart_data(model, request):
        """Line chart data.

        Example:

        .. code-block:: python

            return {
                'labels': labels,
                'datasets': [{
                    'label': 'Dataset 1',
                    'data': [10, 20, 30],
                    'borderColor': 'rgb(255, 99, 132)',
                    'backgroundColor': 'rgba(255, 99, 132, 0.2)'
                }, {
                    'label': 'Dataset 2',
                    'data': [20, 10, 40],
                    'borderColor': 'rgb(54, 162, 235)',
                    'backgroundColor': 'rgba(54, 162, 235, 0.2)'
                }]
            }
        """
        raise NotImplementedError(
            'Abstract ``LineChartTile`` does not implement ``chart_data``'
        )
