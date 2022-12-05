from .chart import ChartTile


class BubbleChartTile(ChartTile):
    """ Tile rendering a bubble chart.
    Reference: https://www.chartjs.org/docs/latest/charts/bubble.html
    """

    chart_type = 'bubble'
    """Setting chart type to 'line'. """

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        See ChartTile.chart_data for details.
        Example:
            return {
                datasets: [{
                    label: 'First Dataset',
                    data: [{
                        x: 20,
                        y: 30,
                        r: 15
                    }, {
                        x: 40,
                        y: 10,
                        r: 10
                    }],
                    backgroundColor: 'rgb(255, 99, 132)'
                }]
            }
        """
        raise NotImplementedError('Chart data not implemented')
