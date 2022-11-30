from .chart import ChartTile


class BarChartTile(ChartTile):
    """Barchart options documentation:
    https://www.chartjs.org/docs/latest/charts/bar.html
    """

    chart_type = 'bar'
    """Setting chart type to 'bar'. """

    chart_options = {
        'options': {
            'scales': {
                'y': {
                    'beginAtZero': True
                }
            }
        }
    }
    """Must have required options for barchart. See chart.js documentation."""

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        See ChartTile.chart_data for details.
        """
        raise NotImplementedError('Chart data not implemented')
