from .chart import ChartTile


class ScatterChartTile(ChartTile):
    """ Tile rendering a scatter chart."""

    chart_type = 'scatter'
    """Setting chart type to 'scatter'. """

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        Refer to chart.js documentation for more information.
        https://www.chartjs.org/docs/4.0.1/charts/scatter.html
        Example:
            return {
                datasets: [{
                    label: 'Scatter Dataset',
                    data: [{
                        x: -10,
                        y: 0
                    }, {
                        x: 0,
                        y: 10
                    }, {
                        x: 10,
                        y: 5
                    }, {
                        x: 0.5,
                        y: 5.5
                    }],
                    backgroundColor: 'rgb(255, 99, 132)'
                }],
            }
        """
        raise NotImplementedError('Chart data not implemented')
