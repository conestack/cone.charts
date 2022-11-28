from .chart import ChartTile


class LineChartTile(ChartTile):
    """
    linechart options documentation:
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    
    chart_factory = 'cone_charts.LineChartTile'

    @staticmethod
    def chart_data(model, request):
        raise NotImplementedError('Chart data not implemented')

