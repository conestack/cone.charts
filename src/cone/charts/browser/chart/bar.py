from .chart import ChartTile


class BarChartTile(ChartTile):
    """
    barchart options documentation:
    https://www.chartjs.org/docs/latest/charts/bar.html
    """

    chart_factory = 'cone_charts.BarChartTile'
    """ Factory used for barchart creation in javascript.
    """

    chart_options ={
        'options': {
            'scales': {
                'y': {
                    'beginAtZero': True
                }
            }
        }
    }
    """ Must have required options for barchart. See chart.js documentation.
    """

    @staticmethod
    def chart_data(model, request):
        """ Return chart data as dict.
            See ChartTile.chart_data for details.
        """
        raise NotImplementedError('Chart data not implemented')
