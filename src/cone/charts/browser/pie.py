from .chart import ChartTile


class PieChartTile(ChartTile):
    """Piechart tile."""

    chart_type = 'pie'
    """Setting chart type to 'pie'."""

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.

        Refer to chart.js documentation for more information.
        `pie chart documentation 
        <https://www.chartjs.org/docs/4.0.1/charts/doughnut.html#pie>`_

        Example:
        .. code-block:: python

            return {
                'labels': labels,
                'datasets': [
                    {
                        'label': 'Dataset 1',
                        'data': [10, 20, 30],
                        'borderColor': 'rgb(255, 99, 132)',
                        'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                    },
                    {
                        'label': 'Dataset 2',
                        'data': [20, 10, 40],
                        'borderColor': 'rgb(54, 162, 235)',
                        'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                    }
                ]
            }
        """
        raise NotImplementedError('Chart data not implemented')
