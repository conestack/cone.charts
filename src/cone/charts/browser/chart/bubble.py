from .chart import ChartTile


class BubbleChartTile(ChartTile):
    """ Tile rendering a bubble chart."""

    chart_type = 'bubble'
    """Setting chart type to 'bubble'. """

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        Refer to chart.js documentation for more information.
        https://www.chartjs.org/docs/4.0.1/charts/bubble.html
        Example:
            return {
                'datasets': [{
                    'label': 'First Dataset',
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
        raise NotImplementedError('Chart data not implemented')
