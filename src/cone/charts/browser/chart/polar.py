from .chart import ChartTile


class PolarChartTile(ChartTile):
    """
    polarchart options documentation:
    https://www.chartjs.org/docs/latest/charts/polar.html
    """

    chart_factory = 'cone_charts.PolarChartTile'
    """ Factory used for polarchart creation in javascript.
    """

    @staticmethod
    def chart_data(model, request):
        """ Return chart data as dict.
        """
        raise NotImplementedError('Chart data not implemented')