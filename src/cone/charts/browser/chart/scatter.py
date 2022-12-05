from .chart import ChartTile


class ScatterChartTile(ChartTile):
    """ Tile rendering a scatter chart.
    Reference: https://www.chartjs.org/docs/latest/charts/scatter.html
    """

    chart_type = 'scatter'
    """Setting chart type to 'scatter'. """

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        See ChartTile.chart_data for details.
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
