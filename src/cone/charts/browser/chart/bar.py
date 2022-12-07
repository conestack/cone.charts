from .chart import ChartTile


class BarChartTile(ChartTile):
    """Barchart tile."""

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
    """Must have required options for barchart. See chart.js documentation."""

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.

        Refer to chart.js documentation for more information.
        `bar chart documentation 
        <https://www.chartjs.org/docs/4.0.1/charts/bar.html>`_

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
