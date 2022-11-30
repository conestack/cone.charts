from .chart import ChartTile


class PieChartTile(ChartTile):
    """Piechart options documentation:
    https://www.chartjs.org/docs/latest/charts/doughnut.html
    """

    chart_type = 'pie'
    """Setting chart type to 'pie'. """

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        See ChartTile.chart_data for details.
        """
        raise NotImplementedError('Chart data not implemented')
