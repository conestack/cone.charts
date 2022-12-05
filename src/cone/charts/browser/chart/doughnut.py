from .chart import ChartTile


class DoughnutChartTile(ChartTile):
    """ Tile rendering a doughnut chart.
    Reference: https://www.chartjs.org/docs/latest/charts/doughnut.html
    """

    chart_type = 'doughnut'
    """Setting chart type to 'doughnut'. """

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        See ChartTile.chart_data for details.
        Example:
            return {
                labels: [
                    'Red',
                    'Blue',
                    'Yellow'
                ],
                datasets: [{
                    label: 'My First Dataset',
                    data: [300, 50, 100],
                    backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(54, 162, 235)',
                    'rgb(255, 205, 86)'
                    ]
                }]
            }
        """
        raise NotImplementedError('Chart data not implemented')
