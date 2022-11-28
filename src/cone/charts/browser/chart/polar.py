from .chart import ChartTile


class PolarChartTile(ChartTile):
    """
    polarchart options documentation:
    https://www.chartjs.org/docs/latest/charts/polar.html
    """
    
    chart_factory = 'cone_charts.PolarChartTile'

    @staticmethod
    def chart_data(model, request):
        raise NotImplementedError('Chart data not implemented')