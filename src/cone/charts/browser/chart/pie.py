from .chart import ChartTile


class PieChartTile(ChartTile):
    """
    piechart options documentation:
    https://www.chartjs.org/docs/latest/charts/doughnut.html
    """

    chart_factory = 'cone_charts.PieChartTile'
    """ Factory used for piechart creation in javascript.
    """

    @staticmethod
    def chart_data(model, request):
        """ Return chart data as dict.
            See ChartTile.chart_data for details.
        """
        raise NotImplementedError('Chart data not implemented')
