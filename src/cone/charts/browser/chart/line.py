from .chart import ChartTile


class LineChartTile(ChartTile):
    """ Tile rendering a line chart.

    Reference: https://www.chartjs.org/docs/latest/charts/line.html
    """

    chart_factory = 'cone_charts.LineChartTile'
    """ Factory used for line-chart creation in javascript.
    """

    @staticmethod
    def chart_data(model, request):
        raise NotImplementedError('Chart data not implemented')

