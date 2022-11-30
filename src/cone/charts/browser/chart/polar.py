from .chart import ChartTile


class PolarChartTile(ChartTile):
    """Polarchart options documentation:
    https://www.chartjs.org/docs/latest/charts/polar.html
    """

    chart_type = 'polarArea'
    """ Setting chart type to 'polarArea'."""

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        See ChartTile.chart_data for details.
        """
        raise NotImplementedError('Chart data not implemented')
