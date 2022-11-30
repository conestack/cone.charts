from .chart import ChartTile


class LineChartTile(ChartTile):
    """ Tile rendering a line chart.
    Reference: https://www.chartjs.org/docs/latest/charts/line.html
    """

    chart_type = 'line'
    """Setting chart type to 'line'. """

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        See ChartTile.chart_data for details.
        """
        raise NotImplementedError('Chart data not implemented')
