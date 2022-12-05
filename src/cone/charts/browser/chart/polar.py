from .chart import ChartTile


class PolarChartTile(ChartTile):
    """Polarchart tile."""

    chart_type = 'polarArea'
    """ Setting chart type to 'polarArea'."""

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        Refer to chart.js documentation for more information.
        https://www.chartjs.org/docs/4.0.1/charts/polar.html
        Example:
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
