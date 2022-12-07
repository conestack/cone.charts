from .chart import ChartTile


class BarChartTile(ChartTile):
    """Barchart tile.

    Refer to
    `documentation <https://www.chartjs.org/docs/4.0.1/charts/bar.html>`_
    for more information.
    """

    chart_type = 'bar'
    """Setting chart type to 'bar'."""

    chart_options = {
        'options': {
            'scales': {
                'y': {
                    'beginAtZero': True
                }
            }
        }
    }
    """Required options for bar chart."""

    @staticmethod
    def chart_data(model, request):
        """Chart data as dict.

        Example:

        .. code-block:: python

            return {
                'labels': labels,
                'datasets': [
                    {
                        'label': 'Dataset 1',
                        'data': [10, 20, 30],
                        'borderColor': 'rgb(255, 99, 132)',
                        'backgroundColor': 'rgba(255, 99, 132, 0.2)'
                    },
                    {
                        'label': 'Dataset 2',
                        'data': [20, 10, 40],
                        'borderColor': 'rgb(54, 162, 235)',
                        'backgroundColor': 'rgba(54, 162, 235, 0.2)'
                    }
                ]
            }
        """
        raise NotImplementedError(
            'Abstract ``BarChartTile`` does not implement ``chart_data``'
        )
